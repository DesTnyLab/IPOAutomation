from django.shortcuts import render
from .models import Report
from account.models import AccountDetials
from .meroshare import get_shares_reports, check_results
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse





@login_required
# Create your views here.
def list_account(request):
    accounts = AccountDetials.objects.all()
    context = {
        'accounts': accounts
    }
    return render(request, 'result/account-list.html', context)




@login_required
def view_results(request, account_id):
    user = AccountDetials.objects.get(id=account_id)

    payload = {
        "clientId": user.clientId,
        "username": user.username,
        "password": user.password
    }

    response = get_shares_reports(payload)
    print(response)
    reports = response.get('object', [])
    first_ten_reports = reports[:10]

    results = []
    for report in first_ten_reports:
        try:
            result = {
                "name": report.get('companyName'),
                "scrip": report.get('scrip'),
                "shareTypeName": report.get('shareTypeName'),
                "groupName": report.get('shareGroupName'),
            }
            applicant_form_id = report['applicantFormId']
            response1 = check_results(applicant_form_id, payload)
            if response1 is not None:
                result["status"] = response1.get('statusName', "Unknown")
            else:
                result["status"] = "Unknown"

            results.append(result)
        except Exception as e:
            print(f"Error processing report {report}: {e}")
            continue

    return render(request, 'result/view-results.html', {
        'user': user,
        'reports': results
    })

        # Report.objects.update_or_create(
        #     user=user,
        #     applicant_form_id=report['applicantFormId'],
        #     defaults={
        #         'scrip': report['scrip'],
        #         'company_name': report['companyName'],
        #  
        #        'share_type_name': report['shareTypeName'],
        #         'share_group_name': report['shareGroupName'],
        #     }
        # )
        
    



