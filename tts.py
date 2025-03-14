import os
import pygame
import download_tts

if os.path.isdir("piper") is False:
    download_tts.start()

pygame.mixer.init()

os.chdir("piper")

def talk(text):

    os.system(f'echo "{text}" | piper.exe --model en_GB-cori-high.onnx --output-file audio.wav')

    pygame.mixer.music.load("audio.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()

