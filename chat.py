from ollama import chat

import re

def prompt_with_model(prompt):
    prompt = f"{prompt}"

    response = chat(model='smollm2:360m', messages=[
      {
        'role': 'user',
        'content': prompt,
      },
    ])

    print(response['message']['content'])

    text = re.sub(r"\*.*?\*\s*", "", response['message']['content'])

    return text
