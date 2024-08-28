#Space Invaders Game using PyGame

import pygame
pygame.init()

#Set up the game window.
screen = pygame.display.set_mode([800, 600])

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Fill the screen with black.
    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (0, 0, 255), (400, 300), 25)

    #Flip the display - nothing shows up without this.
    pygame.display.flip()

#Quit the game if the close button is pressed.
pygame.quit()