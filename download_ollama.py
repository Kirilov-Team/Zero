import os
import subprocess
import urllib.request



def download_ollama():

    done = False
    while not done:

        install_dir = input("Select install dir")
        if os.path.isdir(install_dir):
            done = True
        else:
            print("Folder doesn't exist")



    # Define the URL and the filename
    url = "https://ollama.com/download/OllamaSetup.exe"
    filename = "OllamaSetup.exe"

    # Download the installer
    print("Downloading the installer... (wait patiently it may be slow)")
    urllib.request.urlretrieve(url, filename)
    print("Download complete.")

    # Install the program silently
    print("Installing... (wait patiently it may be slow)")
    import subprocess

    new_path = f'{install_dir}\\.ollama'

    # Construct the command to append to PATH
    command = f'setx PATH "%PATH%;{new_path}"'

    # Run the command
    subprocess.run(command, shell=True)

    print(f"Added {new_path} to PATH. Restart your terminal or system for changes to take effect.")

    os.environ["OLLAMA_MODELS"] = f'{install_dir}\\.ollama'

    os.system(f'ollamasetup.exe /verysilent /DIR="{install_dir}\\ollama"')

    # Delete the setup file
    os.remove(filename)
    print("Setup file deleted.")
