import pygame
import sys


print("hello")
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Test Pygame")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))
    pygame.display.flip()