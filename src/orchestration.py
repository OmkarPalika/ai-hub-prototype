def generate_response(user_input, model, tokenizer):
    inputs = tokenizer(user_input, return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, max_new_tokens=100)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response
