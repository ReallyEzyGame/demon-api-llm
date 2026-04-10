"""
# Source code structure
# Call Local API
# Call public API
"""

"""# Call Local API"""

import requests
# API
API_URL = "http://127.0.0.1:8000/"
#
parameters = {"prompt": "Thầy Lê Đức K ở trường Đại học Khoa học Tự nhiên có đẹp trai không?", "max_length": 512}
# Kiểm tra 'post' method
response1 = requests.post(API_URL + "generate", json=parameters)
print(f'Kết quả của "post": {response1.json()}\n')
# Kiểm tra 'get' method
response2 = requests.get(API_URL)
print(f'Kết quả của "get": {response2.json()}\n')
# kiểm tra 'get' health method
response3 = requests.get(API_URL + "health")
print(f'Kết quả của "get" health: {response3.json()}\n')