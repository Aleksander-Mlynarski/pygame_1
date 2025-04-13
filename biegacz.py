import pygame
import os
import math
os.chdir(os.path.expanduser("~/Documents/gra"))
from sys import exit

pygame.init()
screen = pygame.display.set_mode((576,324))
pygame.display.set_caption('Biegacz')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Rainbow Memories.otf', 50)

tlo = pygame.image.load('graphics/background/1 background/orig.png').convert_alpha() #dodano convert_alpha(), w celu optymalizacji gry
bohater1 = pygame.image.load('graphics/player/1 Pink_Monster/Pink_Monster.png').convert_alpha()
text_surface = test_font.render('Start', True, 'White')
crystal1 = pygame.image.load('graphics/objects/4.png').convert_alpha()

bohater1 = pygame.transform.scale(bohater1, (64, 64)) #skalowanie obiektu
crystal1 = pygame.transform.scale(crystal1, (64, 64))
crystal1_x_pos = 0
crystal1_y_pos = 0
center_x = 250
center_y = 115
radius = 100
angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(tlo,(0,0))
    screen.blit(crystal1,(crystal1_x_pos,crystal1_y_pos))
    crystal1_x_pos = center_x + radius * math.cos(angle)
    crystal1_y_pos = center_y + radius * math.sin(angle)
    angle += 0.03
    screen.blit(text_surface,(40,15))

    pygame.display.update()
    clock.tick(60)
