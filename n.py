import requests

API_KEY = "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"
API_ENDPOINT = "https://api.openai.com/v1/engines/davinci/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

data = {
    "prompt": "Once upon a time",
    "max_tokens": 50
}

response = requests.post(API_ENDPOINT, headers=headers, json=data)

print(response.json())
