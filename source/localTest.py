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
response = requests.post(API_URL + "generate", json=parameters)
print(response.json())
# Kiểm tra 'get' method
response2 = requests.get(API_URL)
print(response2.json())
# kiểm tra 'get' health method
response3 = requests.get(API_URL + "health")
print(response3.json())

