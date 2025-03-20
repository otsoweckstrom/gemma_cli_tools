import ollama

response = ollama.chat(model='gemma3:1b', messages=[{"role": "user", "content": "What is the capital of Finland?"}])

print("Gemma's Response:")
print(response['message']['content'])
