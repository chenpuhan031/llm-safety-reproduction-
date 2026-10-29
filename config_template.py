import os

# --- Target Model Configuration (The model to attack) ---
TARGET_CONFIG = {
    "api_key": os.getenv("TARGET_API_KEY", "input_your_api_key"),
    "base_url": "https://your_url/v1",  # e.g., https://openrouter.ai/api/v1
    "model_name": "glm-4"  # Example model
}

# --- Evaluator Model Configuration (LLM-as-a-Judge) ---
EVALUATOR_CONFIG = {
    "api_key": os.getenv("EVALUATOR_API_KEY", "input_your_api_key"),
    "base_url": "https://your_url/v1",
    "model_name": "gpt-4o"  # Example model
}

# --- Helper Model Configuration (For generating steganographic text) ---
HELPER_CONFIG = {
    "api_key": os.getenv("HELPER_API_KEY", "input_your_api_key"),
    "base_url": "https://your_url/v1",
    "model_name": "gpt-4o"
}

def initialize_clients():
    """Initialize OpenAI clients for all three roles."""
    from openai import OpenAI
    try:
        target_client = OpenAI(api_key=TARGET_CONFIG["api_key"], base_url=TARGET_CONFIG["base_url"])
        helper_client = OpenAI(api_key=HELPER_CONFIG["api_key"], base_url=HELPER_CONFIG["base_url"])
        evaluator_client = OpenAI(api_key=EVALUATOR_CONFIG["api_key"], base_url=EVALUATOR_CONFIG["base_url"])
        print(f"Configuration complete. Target: {TARGET_CONFIG['model_name']}, Evaluator: {EVALUATOR_CONFIG['model_name']}")
        return target_client, helper_client, evaluator_client
    except Exception as e:
        print(f"API client initialization failed: {e}")
        return None, None, None

if __name__ == "__main__":
    initialize_clients()
