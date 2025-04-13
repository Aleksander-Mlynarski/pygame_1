import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Biegacz')
clock = pygame.time.Clock()

test_surface = pygame.Surface((120,56))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit()

    pygame.display.update()
    clock.tick(60)