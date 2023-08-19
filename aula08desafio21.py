import webbrowser
import pygame
#pygame
pygame.mixer.init()
pygame.mixer.music.load('1som.wav')
pygame.mixer.music.play()
input()
pygame.event.wait()
#webbrowser
webbrowser.open("1som.wav")


