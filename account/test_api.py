import requests



payload1 = {
	"accountBranchId": 8474,
	"accountNumber": "25707010131582",
	"accountTypeId": 1,
	"appliedKitta": "10",
	"bankId": "14",
	"boid": "03910018",
	"companyShareId": "713",
	"crnNumber": "R000642877",
	"customerId": 4312880,
	"demat": "1301120003910018",
	"transactionPIN": "1069"
}


# Now you can use this information to apply for shares
headers ={

}
response = requests.post("https://webbackend.cdsc.com.np/api/meroShare/applicantForm/share/apply", json=payload1, headers=headers)

print(response.status_code)
print(response.json())
