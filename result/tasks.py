# # tasks.py
# from celery import shared_task
# import requests, logging
# from requests.exceptions import RequestException, Timeout

# logger = logging.getLogger(__name__)

# import os, json
# from .meroshare import get_authorization
# from dotenv import load_dotenv

# load_dotenv()  # loads variables from .env


# headers = json.loads(os.getenv("MEROSHARE_HEADERS_GET"))

# CHECK_STATUS_URL = os.getenv("CHECK_STATUS_URL")


# @shared_task(bind=True, max_retries=3)
# def check_results_task(self, applicant_form_id, payload):
#     """Check report results with retries (runs in background)."""
#     try:
#         authorization = get_authorization(payload)
#         headers['Authorization'] = authorization

#         url = f"{CHECK_STATUS_URL}{applicant_form_id}"
#         logger.info(f"Request URL: {url}")
#         response = requests.get(url, headers=headers, timeout=10)
#         logger.info(f"Status code: {response.status_code}")
#         logger.info(f"Response: {response.json()}")
#         if response.status_code == 200:
#             return response.json()
#         else:
#             logger.warning(f"Failed to fetch status for applicantFormId={applicant_form_id}. Status code: {response.status_code}")
#             return None

#     except (Timeout, RequestException) as exc:
#         logger.error("Request failed for applicantFormId=%s. Error: %s", applicant_form_id, exc)
#         self.retry(exc=exc, countdown=2)

#     except Exception as e:
#         logger.exception("Unexpected error: %s", e)
#         return None

from celery import shared_task

@shared_task
def i_am_a_task():
    return "Hello from result.tasks.i_am_a_task"