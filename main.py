import download_tts
import os

if not os.path.isdir("piper"):
    download_tts.start()



import ollama
import torch

# Check CUDA availability
print(torch.version.cuda)
print(torch.cuda.is_available())
import tts
import chat
import download_ollama
import subprocess





def is_model_installed(model_name):
    result = subprocess.run(["ollama", "list"], capture_output=True, text=True)

    return model_name in result.stdout

ret_value = os.system("ollama --version")
if ret_value != 0:
    print(f"Ollama not installed")
    download_ollama.download_ollama()


if not is_model_installed("smollm2:360m"):
    print("Model not installed!")
    ollama.pull("smollm2:360m")

while True:
    prompt = input("> ")
    answer = chat.prompt_with_model(prompt)

    tts.talk(answer)




