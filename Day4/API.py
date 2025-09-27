import os
import requests

API_URL = "https://router.huggingface.co/hf-inference/models/distilbert/distilbert-base-uncased"

headers = {"Authorization":f"Bearer {os.environ['HF_TOKEN']}"}

def query(payload):
    response = requests.post(API_URL,headers=headers,json=payload)
    try:
        return response.json()
    except Exception as e:
        print("Raw Response: ", response.text)
        raise e

output = query({"inputs":"What Is the [MASK] of India"})

print(output)
  
