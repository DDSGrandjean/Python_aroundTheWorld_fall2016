"""
    monsterProjectileClass.py
    December 7th, 2016

    Class which creates projectile for monsters when
    it is time for the to shoot bullets or drop bombs.

    Dylan Grandjean
"""
import pygame
if not pygame.mixer:
    print "--Sound error--"
else:
    pygame.mixer.init()
    
class MonsterProjectileClass(pygame.sprite.Sprite):
    def __init__(self, data):
        """ Initialize class and pass a set of data containing the
            coordinates of the monster that is shoting."""
        pygame.sprite.Sprite.__init__(self)

        #load images and create rectangle
        self.images = []
        self.images.append(pygame.image.load("assets/images/misc/monsterProjectile[0].png"))
        self.images.append(pygame.image.load("assets/images/misc/monsterProjectile[1].png"))
        self.i = 0
        while self.i < 2:
            self.images[self.i] = self.images[self.i].convert()
            self.images[self.i].set_colorkey((0, 0, 0))
            self.i += 1
        self.rect = self.images[0].get_rect()

        #load sound
        self.fireSound = pygame.mixer.Sound("assets/sounds/ennemyFire.ogg")

        #assigns data values
        speed, self.rect.centery, self.rect.centerx, self.type = data

        #determines the appearance of the projectile
        if self.type == 0:
            self.image = self.images[0]
        elif self.type == 1:
            self.image = self.images[1]

        #create a starting speed relative to game speed
        self.dx = speed + 10

    def update(self, speed):
        """ Moves the projectile in the direction it
            is meant to move according to its type."""
        if self.type == 0:
            self.rect.centerx -= self.dx
        elif self.type == 1:
            self.rect.centerx -= self.dx/2
            self.rect.centery += speed
        
    def playSound(self):
        """ Play sound when ennemy fires."""
        self.fireSound.play()        
