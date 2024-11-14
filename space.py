#Space Invaders Game using PyGame

import pygame

from pygame.locals import(
    K_LEFT,
    K_RIGHT,
    K_SPACE,
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
        if self.rect.right > screenWidth:
            self.rect.right = screenWidth

        #Add shooting for player when spacebar is pressed
        #Need to implement - spacebar pressed does work tho
        #if pressed_keys[K_SPACE]:
           # self.rect.move_ip(-5, 0)

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([4, 10])
        self.image.fill((255, 255, 255))

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 3


class Enemy(pygame.sprite.Sprite):
    def __init__(self): #add x,y to add multiple later
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("enemy3.png").convert()
        self.surf = pygame.transform.scale(self.surf, (60, 60))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center = (screenWidth/2, screenHeight/2))
        #self.rect = self.surf.get_rect()
        #self.rect.center[x, y]


#Set up the game window.
screen = pygame.display.set_mode([screenWidth, screenHeight])

#Instantiate Player
player = Player()

enemy = Enemy()

#Groups to hold different sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player, enemy)

bullet_group = pygame.sprite.Group()
#alien_group = pygame.sprite.Group()

#Keep getting this error if I try this way to add enemies
#TypeError: tuple indices must be integers or slices, not tuple
"""
def addEnemies():
    for rows in range(5):
        for item in range(5):
            enemy = Enemy(100, 70)
            alien_group.add(enemy)

addEnemies()
"""

#Variable that keeps the main loop running
running = True

#Clock for decent framerate
clock = pygame.time.Clock()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == K_SPACE:
            bullet = Bullet()
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y

            all_sprites.add(bullet)
            bullet_group.add(bullet)

    #Detect keys pressed by user
    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys)

    #Add background image
    background = pygame.image.load('space.jpg')
    background = pygame.transform.scale(background, (800, 600))

    #Fill the screen with black.
    screen.blit(background, (0, 0))

    #Draw all the sprites to screen
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    #Flip the display - nothing shows up without this.
    pygame.display.flip()

    #This ensures program maintains a rate of 30 frames per second
    clock.tick(30)
