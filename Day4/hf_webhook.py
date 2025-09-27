from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

HF_API_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn"
HF_HEADERS = {"Authorization": f"Bearer {os.environ['HF_TOKEN']}"}

def summarize_text(text):
    payload = {"inputs": text}
    response = requests.post(HF_API_URL, headers=HF_HEADERS, json=payload)
    if response.status_code != 200:
        return {"error": response.text}
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e)}

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json  # <-- Use 'request' from Flask
    text = data.get("text")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    result = summarize_text(text)
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=5000)
