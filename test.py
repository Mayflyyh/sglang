import requests

# url = "http://127.0.0.1:30000/v1/chat/completions"
url = "http://127.0.0.1:8000/v1/chat/completions"


data = {
    "model": "Llama-3.2-1B-Instruct.fp16.gguf",
    # "model": "./qwen2-0_5b-instruct-fp16.gguf",
    # "model": "./qwen2-0_5b-instruct-q5_k_m.gguf",
    "messages": [{"role": "user", "content": "Who are you? answer me in one word."}],
    # "response_format": { "type": "json_object" },
}

response = requests.post(url, json=data)
print(response.json())
