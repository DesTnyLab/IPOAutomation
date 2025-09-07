
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import AccountDetailsForm
from .models import AccountDetials, DpIdReverse
from .meroshare import validate_user

def create_account(request):
    if request.method == 'POST':
        form = AccountDetailsForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        if form.is_valid():
            form.save()
            account =  AccountDetials.objects.get(username=username)
            if validate_account(account):
                return redirect('account:home')  # redirect somewhere
            else:
                account.delete()  # Remove invalid account
                print("Invalid credentials for MeroShare")
    else:
        form = AccountDetailsForm()
    return render(request, 'account/create_account.html', {'form': form})


# Create your views here.

def home(request):
    account_details = AccountDetials.objects.all()
    dp_id = account_details.first().dp_id
    dp_id_reverses = DpIdReverse.objects.get(dp_id=dp_id)
    dp_id_rev = dp_id_reverses.get_clientId()
    print(dp_id_rev)
    return render(request, 'account/home.html', {
        'account_details': account_details,
        'dp_id_reverses': dp_id_reverses
    })



def validate_account(object):
    """ Validate user account if they got logged in to meroshare """
    clientid, username, password = object.clientId, object.username, object.password

    payload = {
        "clientId": clientid,
        "username": username,
        "password": password
    }
    if validate_user(payload):
        return True
    else:
        return False


    
    





    
