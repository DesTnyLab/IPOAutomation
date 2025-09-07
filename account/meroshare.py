
import requests, time
import os, json
from .utils import add_bank_details
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env


headers = json.loads(os.getenv("MEROSHARE_HEADERS"))

MEROSHARE_LOGIN_URL = os.getenv("MEROSHARE_LOGIN_URL")
MEROSHARE_BANK_URL = os.getenv("MEROSHARE_BANK_URL")



def validate_user(payload):
    """ Validate user account if they got logged in to meroshare """
    try: 
        response = requests.post(MEROSHARE_LOGIN_URL, json=payload)
        if response.status_code == 200:
            authorization_token = response.headers.get('Authorization')
            time.sleep(3)
            if get_bank_details(authorization_token):
                return True
            else:
                return False
        else:
            return False
  
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False


def get_bank_details(authorization_token):
    """ Fetch bank details using the provided headers """
    try: 
        headers['Authorization'] = authorization_token
        response = requests.get(MEROSHARE_BANK_URL, headers=headers)

        if response.status_code == 200:
            banks = response.json()
            for bank in banks:
                id = bank['id']
            time.sleep(3)
            response = requests.get(f"{MEROSHARE_BANK_URL}{id}", headers=headers, verify=True)
            if add_bank_details(id, response):
                return True
            else:
                return False
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching bank details: {e}")
        return False


        