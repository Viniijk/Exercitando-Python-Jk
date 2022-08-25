from pygame import mixer
#Faça um programa em Python que abra e
# reproduza o audio de um arquivo MP3.

mixer.init()
mixer.music.load('Aurora - Runaway.mp3')

mixer.music.play()

import time

time.sleep(360)

