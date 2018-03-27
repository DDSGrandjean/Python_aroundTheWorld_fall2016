"""
    monsterClass.py
    December 5th, 2016

    Class which creates instances of monsters, each
    with their own speed and characteristics as well
    as behaviors.

    Dylan Grandjean
"""
import pygame, random
if not pygame.mixer:
    print "--Sound error--"
else:
    pygame.mixer.init()
    
class MonsterClass(pygame.sprite.Sprite):
    def __init__(self, speed):
        """ Initialize the monsterClass and pass the current speed
            of the game."""
        pygame.sprite.Sprite.__init__(self)

        #create an image list, load images into it, and converts them
        self.images = []
        self.images.append(pygame.image.load("assets/images/monsters/monster[0].png"))
        self.images.append(pygame.image.load("assets/images/monsters/monster[1].png"))
        self.images.append(pygame.image.load("assets/images/monsters/monster[2].png"))
        self.images.append(pygame.image.load("assets/images/monsters/monster[3].png"))
        self.n = 0
        while self.n < 4:
            self.images[self.n] = self.images[self.n].convert()
            self.images[self.n].set_colorkey((255, 255, 255))
            self.n += 1

        #load sound
        self.hitSound = pygame.mixer.Sound("assets/sounds/ennemyHit.ogg")
        
        #realm of y-coordinate where the monsters can appear
        self.coord = [32, 160, 288, 416]

        #instantiate values for reset purposes
        self.i = random.randint(30, 300)
        self.s = random.randint(30, 120)
        self.resetSec = 0
        self.shootSec = 0
        self.canShoot = random.randint(0,3)
        self.shoot = False
        self.bomb = False

        #assigns image self.images[self.canShoot] to self.image
        self.image = self.images[self.canShoot]
        self.image = self.image.convert()
        self.image.set_colorkey((255, 255, 255))

        #create rectangle
        self.rect = self.image.get_rect()

        #determines the coordinates
        if self.canShoot == 3:
            self.rect.centery = 32
        else:
            self.rect.centery = random.choice(self.coord)
        self.rect.centerx = random.randint(960, 3000)

        #determines the speed
        if self.canShoot == 0:
            self.dx = speed + 10
        elif self.canShoot == 1:
            self.dx = speed + 25
        else:
            self.dx = speed + 4

    def update(self, screen, speed):
        """ Moves the monster towards the left at a given
            speed relative to the game's speed and handles
            certain sets of action for certain type of monsters."""
        #move towards the left
        self.rect.centerx -= self.dx
        if self.rect.right < 0:
            self.resetSec += 1
            if self.resetSec == self.i:
                self.resetSec = 0
                self.reset(screen, speed)

        #shoots forward if monster is of type 2
        if self.canShoot == 2:
            self.shootSec += 1
            if self.shootSec == 60:
                self.shootSec = 0
                self.shoot = True
        #shoots downwards if monster is of type 3
        elif self.canShoot == 3:
            self.shootSec += 1
            if self.shootSec == 60:
                self.shootSec = 0
                self.bomb = True
                
    def fire(self):
        """ Helps main determins whether it is time
            for this monster of type 2 to shoot."""
        if self.shoot == True:
            self.shoot = False
            return True
        else:
            return False

    def drop(self):
        """ Helps main determins whether it is time
            for this monster of type 3 to shoot."""
        if self.bomb == True:
            self.bomb = False
            return True
        else:
            return False
        
    def reset(self, screen, speed):
        """ Resets and modifies the monster whenever it is
            shot down or exists the screen."""
        #creates new random variable for reset time
        self.i = random.randint(30, 300)

        #resets the x-coordinate
        self.rect.centerx = random.randint(960, 3000)

        #reset the monster type and image
        self.canShoot = random.randint(0, 3)
        self.image = self.images[self.canShoot]

        #determine monster speed
        if self.canShoot == 0:
            self.dx = speed + 10
        elif self.canShoot == 1:
            self.dx = speed + 25
        else:
            self.dx = speed + 4

        #determine possible y-coordinates
        if self.canShoot == 3:
            self.rect.centery = 32
        else:
            self.rect.centery = random.choice(self.coord)

    def playSound(self):
        """ Play sound when ennemy is hit."""
        self.hitSound.play()
        








        
