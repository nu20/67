import requests
api_url = "https://api-inference.huggingface.co/models/distilbert-base-uncased"
headers = {
    "Authorization": "Bearer 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"
}
text = "I love this movie! It was fantastic."
response = requests.post(api_url, headers=headers, json={"inputs": text})
if response.status_code == 200:
    result = response. json()
    print(f"Sentiment: {result[0]['label']} with confidence score: {result[0]['score' ]}")
else:
    print(f"Error: {response.status_code}")