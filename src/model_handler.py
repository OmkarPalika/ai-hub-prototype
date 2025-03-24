from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

MODEL_PATH = "/content/drive/MyDrive/AI-Hub/models/mistral-7b"

def load_model():
    print("Loading Mistral 7B...")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    quantization_config = BitsAndBytesConfig(load_in_4bit=True)

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        quantization_config=quantization_config
    ).cuda()

    print("Model loaded successfully.")
    return model, tokenizer
