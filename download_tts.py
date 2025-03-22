import os
import zipfile
import requests


zip_url = "https://github.com/rhasspy/piper/releases/download/2023.11.14-2/piper_windows_amd64.zip"
onnx_json_url = "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_GB/southern_english_female/low/en_GB-southern_english_female-low.onnx.json?download=true"
onnx_url = "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_GB/southern_english_female/low/en_GB-southern_english_female-low.onnx?download=true"



def download_file(url, filename):
    print(f"Downloading {filename}...")
    response = requests.get(url)
    with open(filename, "wb") as file:
        file.write(response.content)



def unzip_file(zip_filename, extract_to):
    print(f"Unzipping {zip_filename} to {extract_to}...")
    with zipfile.ZipFile(zip_filename, "r") as zip_ref:
        zip_ref.extractall(extract_to)



def download_piper_files(directory):
    print(f"Downloading additional files into {directory}...")
    onnx_json_filename = os.path.join(directory, "en_GB-southern_english_female-low.onnx.json")
    onnx_filename = os.path.join(directory, "en_GB-southern_english_female-low.onnx")

    download_file(onnx_json_url, onnx_json_filename)
    download_file(onnx_url, onnx_filename)



def start():

    zip_filename = "piper_windows_amd64.zip"
    extract_dir = "piper"


    download_file(zip_url, zip_filename)


    unzip_file(zip_filename, ".")


    if not os.path.exists(extract_dir):
        print(f"Error: The folder '{extract_dir}' does not exist.")
        return


    download_piper_files(extract_dir)

    os.remove(zip_filename)
    print(f"Removed the zip file: {zip_filename}")

    print("All downloads are complete.")

