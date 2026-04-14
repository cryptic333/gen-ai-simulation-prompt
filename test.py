from google import genai

client = genai.Client(
    api_key="xxxx",
    http_options={"api_version": "v1"}
)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Say hello"
)

print(response.text)
