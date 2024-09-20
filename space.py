#Space Invaders Game using PyGame

import pygame

from pygame.locals import(
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    RLEACCEL,
)

pygame.init()

screenWidth = 800
screenHeight = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("spaceship.png").convert()
        self.surf = pygame.transform.scale(self.surf, (60, 60))
        self.surf.set_colorkey((255, 255, 255,), RLEACCEL)
        self.rect = self.surf.get_rect()

#Set up the game window.
screen = pygame.display.set_mode([screenWidth, screenHeight])

player = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Fill the screen with black.
    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (0, 0, 255), (400, 300), 25)

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    #Flip the display - nothing shows up without this.
    pygame.display.flip()
