from datasets import load_dataset

def load_data():
    dataset = load_dataset("wikitext", "wikitext-2-raw-v1")
    print("Dataset loaded.")
    return dataset
