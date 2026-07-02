"""
Snake Game
Author: baczl
A simple Snake game built with Python 3.12 and pygame.
"""

import pygame
# pygame setup
pygame.initscreen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.Quit event means user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from the last fame
    screen.fill("purple")

    # Render game here

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(24) # limits FPS to 24 

pygame.quit()