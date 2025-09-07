from django.http import JsonResponse
from django.shortcuts import render
from account.models import AccountDetials
from .models import CompanyShare
from .meroshare import get_applicable_shares
from .utils import parse_date
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):
    return None



def auto_applicable_shares(request):
    """ Fetch the applicable shares for the logged in user """
    try:
        account_details = AccountDetials.objects.random()
        payload = {
            "clientId": account_details.clientId,
            "username": account_details.username,
            "password": account_details.password
        }
        
        response = get_applicable_shares(payload)
        for share in response['object']:
            obj, created = CompanyShare.objects.update_or_create(
                company_share_id=share['companyShareId'],
                defaults={
                    'scrip': share['scrip'],
                    'company_name': share['companyName'],
                    'share_type_name': share['shareTypeName'],
                    'share_group_name': share['shareGroupName'],
                    'sub_group': share['subGroup'],
                    'status_name': share['statusName'],
                    'issue_open_date': parse_date(share['issueOpenDate']),
                    'issue_close_date': parse_date(share['issueCloseDate']),
                }
            )
    except Exception as e:
        print(f"An error occurred: {e}")



def view_applicable_shares(request):
    shares = CompanyShare.objects.all().order_by('-issue_open_date')
    return render(request, 'apply/share-list.html', {'shares': shares})




def apply_share(request, share_id):
    accounts = AccountDetials.objects.all()
    share = CompanyShare.objects.get(company_share_id=share_id)
    return render(request, 'apply/apply-share.html', {'accounts': accounts, 'share': share})
   


@require_GET
@csrf_exempt   
def check_status(request, user_id, share_id):
    user = AccountDetials.objects.get(id=user_id)
    share = CompanyShare.objects.get(id=share_id)

    payload = {
        "clientId": user.clientId,
        "username": user.username,
        "password": user.password
    }
    print(payload)
    response = get_applicable_shares(payload)
    print(response['object'])

    for item in response['object']:
        print(item.get('action'))
        if item['companyShareId'] == share.company_share_id:
            if item.get('action') == 'edit':
                return JsonResponse({'status': 'False'})
            else:
                return JsonResponse({'status': 'True'})

    return JsonResponse({'status': 'True'})


