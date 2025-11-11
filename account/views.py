
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import AccountDetailsForm
from .models import AccountDetials
from .meroshare import validate_user1
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required






def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('account:home')  # Redirect to a success page.
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('account:login')

class AccountView(LoginRequiredMixin,TemplateView):
    template_name = "account/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = context.get("form") or AccountDetailsForm()
        context["account_details"] = AccountDetials.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = AccountDetailsForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            try:
            
                account = form.save(commit=False)
                account.save()
                print("Account saved to database")
                # Optional: custom validation
                if validate_account(account):
                    print("Account is valid")
                    # AJAX success response
                    return JsonResponse({
                        "success": True,
                        "message": "Account added successfully!"
                    })
                else:
                    account.delete()
                    form.add_error(None, "Invalid credentials for MeroShare")

            except Exception as e:
                print(f"An error occurred: {e}")
                form.add_error(None, f"Error saving account: {str(e)}")
        else:
            # Return form errors as JSON 
            print("Form is not valid")   
            print(form.errors)
            errors = form.errors.get_json_data()
            non_field_errors = form.non_field_errors()
            return JsonResponse({
                "success": False,
                "errors": errors,
                "non_field_errors": list(non_field_errors)
            })
          
        print(form.errors)
        return JsonResponse({
            "success": False,
            "errors": "Invalid credentials for MeroShare",

        })


@login_required
def delete_Account(request, account_id):
    try:
        account = AccountDetials.objects.get(id=account_id)
        account.delete()
        messages.success(request, "Account deleted successfully.")
    except AccountDetials.DoesNotExist:
        messages.error(request, "Account not found.")
    return redirect('account:home')


# def create
# 
# _account(request):
#     if request.method == 'POST':
#         form = AccountDetailsForm(request.POST)
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         if form.is_valid():
#             form.save()
#             account =  AccountDetials.objects.get(username=username)
#             if validate_account(account):
#                 return redirect('account:home')  # redirect somewhere
#             else:
#                 account.delete()  # Remove invalid account
#                 print("Invalid credentials for MeroShare")
#     else:
#         form = AccountDetailsForm()
#     return render(request, 'account/create_account.html', {'form': form})


# # Create your views here.

# def home(request):
#     account_details = AccountDetials.objects.all()
#     return render(request, 'account/home.html', {
#         'account_details': account_details,
#     })


@login_required
def validate_account(object):
    """ Validate user account if they got logged in to meroshare """
    clientid, username, password = object.clientId, object.username, object.password

    payload = {
        "clientId": clientid,
        "username": username,
        "password": password
    }
    if validate_user1(payload, object):
        print("User validated successfully")
        return True
    else:
        print("User validation failed")
        return False


    
    





    
def index(request):
    return render(request, 'index.html')

def docs(request):
    return render(request, 'new.html')