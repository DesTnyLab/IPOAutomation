


import requests, time
import os, json

from dotenv import load_dotenv

load_dotenv()  # loads variables from .env


headers = json.loads(os.getenv("MEROSHARE_HEADERS"))

MEROSHARE_LOGIN_URL = os.getenv("MEROSHARE_LOGIN_URL")
ISSUE_REPORT_URL = os.getenv("ISSUE_REPORT_URL")
CHECK_STATUS_URL = os.getenv("CHECK_STATUS_URL")


def get_authorization(payload):
    """ Validate user account if they got logged in to meroshare """
    try: 
        response = requests.post(MEROSHARE_LOGIN_URL, json=payload)
        if response.status_code == 200:
            authorization_token = response.headers.get('Authorization')
            return authorization_token
  
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    



def get_applicable_shares(payload):
    """ Get applicable shares for the user """
    try:
        payload1 = {
            "filterDateParams": [
                {
                    "alias": "",
                    "condition": "",
                    "key": "appliedDate",
                    "value": ""
                },
                {
                    "alias": "",
                    "condition": "",
                    "key": "appliedDate",
                    "value": ""
                }
            ],
            "filterFieldParams": [
                {
                    "alias": "Scrip",
                    "key": "companyShare.companyIssue.companyISIN.script"
                },
                {
                    "alias": "Company Name",
                    "key": "companyShare.companyIssue.companyISIN.company.name"
                }
            ],
            "page": 1,
            "searchRoleViewConstants": "VIEW_APPLICANT_FORM_COMPLETE",
            "size": 200
        }
        
        authorization = get_authorization(payload)
        headers['Authorization'] = authorization
        time.sleep(3)
        response = requests.post(ISSUE_REPORT_URL, json=payload1, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    



