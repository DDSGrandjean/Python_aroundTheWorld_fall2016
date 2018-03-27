"""
    playerClass.py
    November 21st, 2016

    Class which contains player info

    Dylan Grandjean
"""
import pygame
if not pygame.mixer:
    print "--Sound error--"
else:
    pygame.mixer.init()

class PlayerClass(pygame.sprite.Sprite):
    def __init__(self):
        """ Initialize the player class."""
        pygame.sprite.Sprite.__init__(self)

        #load images and create rectangle
        self.images = []
        self.images.append(pygame.image.load("assets/images/player/player[0].png"))
        self.images.append(pygame.image.load("assets/images/player/player[1].png"))
        self.i = 0
        while self.i < 2:
            self.images[self.i] = self.images[self.i].convert()
            self.images[self.i].set_colorkey((255, 255, 255))
            self.i += 1
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        #load sounds
        self.hitSound = pygame.mixer.Sound("assets/sounds/friendlyHit.ogg")
        self.jumpSound = pygame.mixer.Sound("assets/sounds/jumpSound.ogg")

        #place the player at its designated starting position
        self.rect.centerx = 100
        self.rect.bottom = 449

        #set all variables to default values
        self.damage = False
        self.isJumping = False
        self.velocity = 8
        self.mass = 2

    def jump(self, grounded):
        """ Determines whether the player can jump."""
        if grounded:
            self.isJumping = True
            return True, False

    def hit(self):
        """ Determines if the player was hit and changes
            the sprite if it was."""
        self.damage = not self.damage
        if self.damage:
            self.image = self.images[1]
        else:
            self.image = self.images[0]

    def update(self, grounded):
        """ Handles the player's constraint in each
            frame and whether certain actions are
            accessible or not."""
        #determine if player is jumping and resets values to default
        #if the player has touched the ground in addition to adding
        #gravity as a downwards force during the jump
        if self.isJumping:
            if grounded:
                self.isJumping = False
                self.velocity = 8
            else:    
                if self.velocity > 0:
                    F = (0.5 * self.mass * (self.velocity * self.velocity))
                else:
                    F = -(0.5 * self.mass * (self.velocity * self.velocity))
                    if F <= -64:
                        F = -64
         
                self.rect.centery -= F
                self.velocity = self.velocity - 1
        #if the player is not jumping, adds gravity as a downward force
        #whenever the player is not grounded and resets values if it is
        else:
            if not grounded:
                F = -(0.5 * self.mass * ((self.velocity - 9) * (self.velocity - 9)))
                if F <= -64:
                    F = -64
                self.rect.centery -= F
                self.velocity = self.velocity - 1
            else:
                self.velocity = 8

        #ensure the player never ends up lower than a platform or grounds surface
        if grounded:
            if self.rect.bottom > grounded[0].rect.top + 1:
                self.rect.bottom = grounded[0].rect.top + 1

    def playHitSound(self):
        """ Play sound when player gets hit."""
        self.hitSound.play()

    def playJumpSound(self):
        """ Play sound when player jumps."""
        self.jumpSound.play()
                
                    
                

        
