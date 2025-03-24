from model_handler import load_model
from orchestration import generate_response
from dev_mode import init_dev_mode

def main():
    print("Initializing AI-Hub...")

    # Load model
    model, tokenizer = load_model()

    # Developer Mode Setup
    init_dev_mode()

    # Test Response
    user_input = input("Ask AI-Hub: ")
    response = generate_response(user_input, model, tokenizer)
    print(f"AI-Hub: {response}")

if __name__ == "__main__":
    main()
