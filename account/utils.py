

from .models import BankDetails

def add_bank_details(id, response):
    """ Handle adding bank details safely """
    try:
        data = response.json()
        
        # If response is a list, pick the first element
        if isinstance(data, list):
            if not data:  # empty list check
                print("No bank details found")
                return False
            bank_details = data[0]
        else:
            bank_details = data

        bank_id = id
        customer_id = bank_details['id']
        account_number = bank_details['accountNumber']
        account_type_id = bank_details['accountTypeId']
        account_branch_id = bank_details['accountBranchId']

        obj, created = BankDetails.objects.update_or_create(
            customer_id=customer_id,
            defaults={
                'account_number': account_number,
                'account_type_id': account_type_id,
                'bank_id': bank_id,
                'account_branch_id': account_branch_id
            }
        )
        return True
    except Exception as e:
        print(f"An error occurred while adding bank details: {e}")
        return False
