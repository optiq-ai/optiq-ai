import os, yaml, requests, logging

CONFIG_PATH = os.getenv("LLM_CONFIG", "config/llm_config.yaml")

def load_config():
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f).get("llms", {})

def route_to_llm(prompt: str, model_name: str) -> dict:
    llms = load_config()
    model = llms.get(model_name)
    if not model:
        raise Exception(f"Model '{model_name}' nie istnieje w konfiguracji.")

    model_type = model.get("type")
    endpoint = model.get("endpoint")

    # OpenAI-like
    if model_type == "openai":
        headers = {
            "Authorization": f"Bearer {os.getenv(model.get('key_env'))}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": model.get("model"),
            "messages": [{"role": "user", "content": prompt}]
        }
        res = requests.post(endpoint, headers=headers, json=payload)
        res.raise_for_status()
        text = res.json()["choices"][0]["message"]["content"]
        return extract_code_and_comment(text)

    # Together
    elif model_type == "together":
        headers = {
            "Authorization": f"Bearer {os.getenv(model.get('key_env'))}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": model.get("model"),
            "messages": [{"role": "user", "content": prompt}]
        }
        res = requests.post(endpoint, headers=headers, json=payload)
        res.raise_for_status()
        text = res.json()["choices"][0]["message"]["content"]
        return extract_code_and_comment(text)

    # Ollama
    elif model_type == "ollama":
        payload = {
            "model": model.get("model"),
            "prompt": prompt
        }
        res = requests.post(endpoint + "/api/generate", json=payload)
        res.raise_for_status()
        return extract_code_and_comment(res.json()["response"])

    # Custom REST API
    elif model_type == "custom":
        headers = model.get("headers", {})
        for k, v in headers.items():
            headers[k] = v.replace("{{API_KEY}}", os.getenv("CUSTOM_API_KEY", ""))
        body = model.get("body_template", {"prompt": "{{prompt}}"})
        body = {k: v.replace("{{prompt}}", prompt) for k, v in body.items()}
        res = requests.post(endpoint, headers=headers, json=body)
        res.raise_for_status()
        return extract_code_and_comment(res.text)

    else:
        raise Exception(f"Nieobsługiwany typ modelu: {model_type}")

def extract_code_and_comment(text: str) -> dict:
    if "```" in text:
        parts = text.split("```")
        code = parts[1] if len(parts) > 1 else text
        commentary = parts[0].strip()
    else:
        code = text
        commentary = ""
    return {"code": code.strip(), "commentary": commentary.strip()}
