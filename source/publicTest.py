import requests



"""# Call Public API"""

API_URL = "https://aqtmg-34-16-215-174.run.pinggy-free.link"
if API_URL:
    print(f"Thực hiện gọi API qua Pinggy: {API_URL}/generate")

    payload_tunnel = {
        "prompt": "Thủ đô của Việt Nam là gì?",
        "max_new_tokens": 512
    }

    # kiểm tra 'get' và 'post' method
    try:
        responsePost = requests.post(f"{API_URL}/generate", json=payload_tunnel)
        responseGet = requests.get(f"{API_URL}/")
        responseGetHealth = requests.get(f"{API_URL}/health")

        print("\nKết quả 'post' method:\n", responsePost.json().get("response", responsePost.text))
        print("\n Kết quả 'get' method:\n", responseGet.json().get("detail", responseGet.text))
        print("\n Kết quả 'get' health method:\n", responseGetHealth.json().get("status", responseGetHealth.text))
    except Exception as e:
        print("Lỗi khi gọi qua tunnel:", str(e))
else:
    print("Chưa có URL Pinggy để test.")