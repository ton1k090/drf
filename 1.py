

import requests
response = requests.post('http://127.0.0.1:8000/api-token-auth/', data={'username':
'admin', 'password': 'admin'})
print(response.status_code) # {'token': '2efa08beed5727856319740df3747df4e0a3655e'}
print(response.json())