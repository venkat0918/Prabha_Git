import requests
LoanId_List=['fd595828-dcc9-491c-a807-f3caad7abb37',
'9b8ddc9f-6a33-4db6-bbef-58475910dfca',
'285a882f-02ff-4b01-aa1b-2ed097c19a17',
'528b62f6-6354-41c0-8339-10f6abda6e7f',
'd5d00108-06f0-4742-9ba1-b6a6163eceb5',
'15bdf4ea-c38e-4db6-855f-aad9640ebdc8',
'209b4b72-a736-4ec2-9da2-f6dc6e8dc23e',
'd253e16f-6230-47b3-a0db-05c168b89d71',
'a1916235-368a-4dc0-9338-4648ace54672',
'7a51c58f-88ae-4ad7-9ef3-609c95fe8dbe',
'6306320a-8175-473f-ad5b-9938962af6c4',
'e1e00879-cf06-46be-8630-07e34c8d2a92',
'699917b4-3344-4b3f-a199-f295316a0b17',
'3aa7c598-c6e1-4a07-a4ed-4d5d3137a287',
'bddc2b45-e365-4959-9cbf-1d5725d0d9f6',
'755ac324-b35b-4423-8d30-5fd65dd7febe',
'8e9c6ef6-e736-48ac-adcf-ece050616a57',
'3a1fe917-ad8a-45b6-b816-8fcbde83db9c',
'466f41cf-8236-4c37-84be-7e09b04cd2ac',
'd60273c1-3c5a-469c-acd7-be550933567d']

for id in LoanId_List:
    payload = "{\r\n\t \"LoanGuid\": \"00afb00-8173-4d17-99d1-c02237cd34aa\"\r\n}"
    pass

url = "https://na1.ai.dm-us.informaticacloud.com/active-bpel/rt/p_API_ssvr_Loan_Stipdetails_Mailroom"


headers = {
  'Authorization': 'Basic aW5mb3JtYXRpY2EtZGV2LmR3QHBubWFjLmNvbTpqallhSG8zZU1PaFY=',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
