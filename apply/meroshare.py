


import requests, time
import os, json

from dotenv import load_dotenv

load_dotenv()  # loads variables from .env


headers = json.loads(os.getenv("MEROSHARE_HEADERS"))

MEROSHARE_LOGIN_URL = os.getenv("MEROSHARE_LOGIN_URL")
MEROSHARE_APPLICABLE_SHARES_URL = os.getenv("MEROSHARE_APPLICABLE_SHARES_URL")



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
			"key": "minIssueOpenDate",
			"value": ""
		},
		{
			"alias": "",
			"condition": "",
			"key": "maxIssueCloseDate",
			"value": ""
		}
	],
	"filterFieldParams": [
		{
			"alias": "Scrip",
			"key": "companyIssue.companyISIN.script"
		},
		{
			"alias": "Company Name",
			"key": "companyIssue.companyISIN.company.name"
		},
		{
			"alias": "Issue Manager",
			"key": "companyIssue.assignedToClient.name",
			"value": ""
		}
	],
	"page": 1,
	"searchRoleViewConstants": "VIEW_APPLICABLE_SHARE",
	"size": 10
}
        
        authorization = get_authorization(payload)
        headers['Authorization'] = authorization
        time.sleep(3)
        response = requests.post(MEROSHARE_APPLICABLE_SHARES_URL, json=payload1, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    



def get_share_applied(payload, payload2):
	""" Apply for shares """
	try:
		APPLY_SHARE_URL = os.getenv("APPLY_SHARE_URL")
		authorization = get_authorization(payload)
		print(authorization)
		headers['Authorization'] = authorization
		time.sleep(3)
		response = requests.post(APPLY_SHARE_URL, json=payload2, headers=headers)
		print(response.status_code)
		print(response)
		if response.status_code == 201:
			print(response.json())
			return response.json()
	except requests.exceptions.RequestException as e:
		print(f"An error occurred: {e}")
		return None