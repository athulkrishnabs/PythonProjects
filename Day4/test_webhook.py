import requests

url = "http://127.0.0.1:5000/summarize"
data = {"text":"I am Learning ai automation and I would love to learn it"}

response= requests.post(url,json=data)

try:
    print(response.json())
    
except Exception:
    print("Raw Message:", response.text)

