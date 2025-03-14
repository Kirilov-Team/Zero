from ollama import chat

def prompt_with_model(prompt):
    prompt = f"{prompt} (give me a short answer)"

    response = chat(model='smollm2:360m', messages=[
      {
        'role': 'user',
        'content': prompt,
      },
    ])

    return response['message']['content']
