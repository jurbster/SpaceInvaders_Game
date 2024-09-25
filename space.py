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

#Define a Player object
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("spaceship.png").convert()
        self.surf = pygame.transform.scale(self.surf, (60, 60))
        self.surf.set_colorkey((255, 255, 255,), RLEACCEL)
        self.rect = self.surf.get_rect(center=(screenWidth/2, 550))

    #Move player left and right
    def update(self, pressed_keys):
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        #Keeps player on screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screenWidth:
            self.rect.right = screenWidth


#Set up the game window.
screen = pygame.display.set_mode([screenWidth, screenHeight])

#Instantiate Player
player = Player()

#Groups to hold different sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

#Variable that keeps the main loop running
running = True

#Clock for decent framerate
clock = pygame.time.Clock()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Detect keys pressed by user
    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys)

    #Fill the screen with black.
    screen.fill((0, 0, 0))

    #Draw all the sprites to screen
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    #Flip the display - nothing shows up without this.
    pygame.display.flip()

    #This ensures program maintains a rate of 30 frames per second
    clock.tick(30)
