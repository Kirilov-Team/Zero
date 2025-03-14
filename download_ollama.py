import os
import subprocess
import urllib.request

def download_ollama():

    # Define the URL and the filename
    url = "https://ollama.com/download/OllamaSetup.exe"
    filename = "OllamaSetup.exe"

    # Download the installer
    print("Downloading the installer... (wait patiently it may be slow)")
    urllib.request.urlretrieve(url, filename)
    print("Download complete.")

    # Install the program silently
    print("Installing... (wait patiently it may be slow)")
    subprocess.run([filename, "/verysilent"], check=True)

    # Delete the setup file
    os.remove(filename)
    print("Setup file deleted.")
