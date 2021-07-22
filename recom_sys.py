import pygame


pygame.mixer.init()

song = f'D:/studies/cse/music recommendation/test music/blink-182 - All The Small Things (Official Video).mp3'
pygame.mixer.music.load(song)
pygame.mixer.music.play(loops=0)

while True:
    if not pygame.mixer.music.get_busy():
        break

song1 = f'D:/studies/cse/music recommendation/test music/Katy Perry - Daisies.mp3'
pygame.mixer.music.load(song1)
pygame.mixer.music.play(loops=0)
