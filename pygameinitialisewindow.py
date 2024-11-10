#This simple code initialises a pygame window.

import sys
import pygame
#initialise pygame
pygame.init()
#window name
pygame.display.set_caption("Insert name here")
#initialise game window with resolution
screen = pygame.display.set_mode((600,480))
#initialise clock
clock = pygame.time.Clock()

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.ext()


    pygame.display.update()
    #lock to 60fps
    clock.tick(60)
