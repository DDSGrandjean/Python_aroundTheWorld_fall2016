"""
    aroundTheWorld.py
    Novemmber 21st, 2016

    Dylan Grandjean
"""
import pygame, os, sys
directory = os.getcwd()
sys.path.append(directory + "/assets/modules")
from skiesClass import *
from groundClass import *
from cloudClass import *
from playerClass import *
from platformClass import *
from fireballClass import *
from monsterClass import *
from monsterProjectileClass import *
from electrostatics import *
from backgroundClass import *
from coinsClass import *
from livesBoxClass import *
pygame.init()
if not pygame.mixer:
    print "--Sound error--"
else:
    pygame.mixer.init()

#create game screen and import game soundtrack
screen = pygame.display.set_mode((960, 480))
pygame.display.set_caption("World Invasion!")
soundtrack = pygame.mixer.music.load("assets/sounds/worldInvasionSoundtrack.ogg")

def main():
    """ Method in which main variables are kept and from which
        both the instruction and game method are called."""
    donePlaying = False
    score = 0
    lives = 5
    best = 0
    bestDist = 0
    while not donePlaying:
        lives = 5
        score = 0
        donePlaying, data = instructions(score, lives, best, bestDist)
        if not donePlaying:
            score, distance, donePlaying = game(score, lives, best, bestDist, data)
            if score > best:
                best = score
            if distance > bestDist:
                bestDist = distance
    pygame.quit()

def instructions(score, lives, best, bestDist):
    """ Method in which the player gets acustomed with the controls and
        the environment in which the game takes place."""
    #play soundtrack
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    
    #game speed
    speed = 8
    
    #classes
    statics = Electrostatics()
    background1 = BackgroundClass("assets/images/backgrounds/background[0].png", speed, -2)
    background2 = BackgroundClass("assets/images/backgrounds/background[1].png", speed, -4)
    background3 = BackgroundClass("assets/images/backgrounds/background[2].png", speed, -6)
    skies = SkiesClass()
    grounds = GroundClass(speed)
    player = PlayerClass()
    clouds = []
    i = 0
    while i < 8:
        clouds.append(CloudClass(speed))
        i += 1

    #Create background
    background = skies.image
    background = background.convert()
    
    #variables
    clock = pygame.time.Clock()
    keepGoing = True
    jumped = False
    isJumping = False
    shot = False

    #Fonts
    insFont = pygame.font.SysFont(None, 50)
    scoreFont = pygame.font.SysFont(None, 25)
    copyFont = pygame.font.SysFont(None, 15)
    life = "Lives: %d" %lives
    liveLabel = scoreFont.render(life, 1, (255, 255, 255))
    coins = "Score: %d" %score
    scoreLabel = scoreFont.render(coins, 1, (255, 255, 255))
    bestCoins = "Best Score: %d" %best
    bestScoreLabel = scoreFont.render(bestCoins, 1, (255, 255, 255))
    bestDistance = "Best Distance: %dkm" %bestDist
    bestDistanceLabel = scoreFont.render(bestDistance, 1, (255, 255, 255))
    copy = "\xa9 2016 - All codes, sounds and images are properties of Dylan Grandjean. Not to be used without authorization."
    copyLabel = copyFont.render(copy, 1, (255, 255, 255))

    titleFont = pygame.font.Font("assets/fonts/FFF_Tusj.ttf", 75)
    titleLabel = titleFont.render("World Invasion!", 1, (255, 255, 255))

    #groups
    allSprites = pygame.sprite.OrderedUpdates(clouds, background3, background2, background1)
    groundSprite = pygame.sprite.Group(grounds)
    friendlyGroup = pygame.sprite.Group(player)
    frontGroup = pygame.sprite.Group(statics)

    #game loop
    while keepGoing:
        clock.tick(30)
        
        #check for ground collision
        grounded = pygame.sprite.spritecollide(player, groundSprite, False)
        
        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
                data = []
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True
                    data = []
                elif event.key == pygame.K_SPACE and not jumped:
                    jumped = True
                    player.playJumpSound()
                    isJumping, grounded = player.jump(grounded)
                elif event.key == pygame.K_RSHIFT and jumped and not shot:
                    shot = True
                    fireball = FireballClass(player, speed)
                    fireball.playSound()
                    friendlyGroup.add(fireball)
        
        #End instructions
        if jumped and shot:
            if fireball.rect.left > screen.get_width():
                keepGoing = False
                donePlaying = False
                data = (skies, grounds, player, clouds, statics, background1, background2, background3)

        #refresh display
        if keepGoing:
            screen.blit(background, (0, 0))

            allSprites.clear(screen, background)
            groundSprite.clear(screen, background)
            friendlyGroup.clear(screen, background)
            frontGroup.clear(screen, background)
            allSprites.update(screen, speed)
            groundSprite.update(screen, speed)
            friendlyGroup.update(grounded)
            frontGroup.update(screen)
            allSprites.draw(screen)
            groundSprite.draw(screen)
            friendlyGroup.draw(screen)
            frontGroup.draw(screen)
            
            if not jumped:
                insLabel = insFont.render("Press the SPACEBAR to jump", 1, (255, 255, 255))
                insQuit = insFont.render("or ESCAPE to quit.", 1, (255, 255, 255))
                screen.blit(insLabel, (230, 300))
                screen.blit(insQuit, (320, 350))
            elif jumped and not shot:
                insLabel = insFont.render("Press R-Shift to shoot", 1, (255, 255, 255))
                insQuit = insFont.render("or ESCAPE to quit.", 1, (255, 255, 255))
                screen.blit(insLabel, (290, 300))
                screen.blit(insQuit, (320, 350))

            screen.blit(liveLabel, (10, 10))
            screen.blit(scoreLabel, (10, 30))
            screen.blit(bestScoreLabel, (10, 50))
            screen.blit(bestDistanceLabel, (10, 70))
            screen.blit(copyLabel, (190, 470))
            screen.blit(titleLabel, (170, 100))

            pygame.display.flip()

    return donePlaying, data

def game(score, lives, best, bestDist, data):
    """ Method in which the player can freely play until their character dies."""
    #game speed
    speed = 8
    
    #classes
    skies, grounds, player, clouds, statics, background1, background2, background3 = data
    monster = MonsterClass(speed)
    lifeBox = LivesBoxClass()
    row = [96, 224, 352]
    platforms = []
    i = 0
    while i < 3:
        platforms.append(PlatformClass(row[i], speed))
        i +=1
    coinsList = []
    i = 0
    while i < 5:
        coinsList.append(CoinsClass(speed))
        i += 1
        
    #Create background
    background = skies.image
    background = background.convert()
    
    #variables
    ennemyList = []
    gameScore = 0
    gameLives = 5
    clock = pygame.time.Clock()
    keepGoing = True
    isJumping = False
    donePlaying = False
    canShoot = True
    canBeHit = True
    distance = 0
    distCount = 0
    liveSec = 0
    sec = 0

    #Fonts
    scoreFont = pygame.font.SysFont(None, 25)
    life = "Lives: %d" %gameLives
    liveLabel = scoreFont.render(life, 1, (255, 255, 255))
    coins = "Score: %d" %gameScore
    scoreLabel = scoreFont.render(coins, 1, (255, 255, 255))
    bestScore = "Best Score: %d" %best
    bestScoreLabel = scoreFont.render(bestScore, 1, (255, 255, 255))
    dist = "%d km" %distance
    distLabel = scoreFont.render(dist, 1, (255, 255, 255))
    bestDistance = "Best Distance: %dkm" %bestDist
    bestDistanceLabel = scoreFont.render(bestDistance, 1, (255, 255, 255))

    #groups
    forgroundGroup = pygame.sprite.Group(grounds, platforms)
    backgroundGroup = pygame.sprite.OrderedUpdates(clouds, background3, background2, background1)
    friendlyGroup = pygame.sprite.Group(player)
    ennemyGroup = pygame.sprite.Group(monster)
    ennemyList.append(monster)
    projectileGroup = pygame.sprite.Group()
    coinGroup = pygame.sprite.Group(coinsList)
    lifeBoxGroup = pygame.sprite.Group(lifeBox)
    frontGroup = pygame.sprite.Group(statics)

    #game loop
    while keepGoing:
        clock.tick(30)
        sec += 1
        if sec == 30:
            distance += 1
            distCount += 1
            sec = 0

        #Check for projectiles
        for monster in range(len(ennemyList)):
            if ennemyList[monster].canShoot == 2 or ennemyList[monster].canShoot == 3:
                if ennemyList[monster].fire():
                    data = (ennemyList[monster].dx, (ennemyList[monster].rect.centery + 16), ennemyList[monster].rect.centerx, 0)
                    fire1 = MonsterProjectileClass(data)
                    data = (ennemyList[monster].dx, (ennemyList[monster].rect.centery - 16), ennemyList[monster].rect.centerx, 0)
                    fire2 = MonsterProjectileClass(data)
                    fire1.playSound()
                    projectileGroup.add(fire1)
                    projectileGroup.add(fire2)
                if ennemyList[monster].drop():
                    data = (ennemyList[monster].dx, ennemyList[monster].rect.centery, ennemyList[monster].rect.centerx, 1)
                    fire = MonsterProjectileClass(data)
                    fire.playSound()
                    projectileGroup.add(fire)
                
        #check for ground/platform collision
        grounded = pygame.sprite.spritecollide(player, forgroundGroup, False)
        
        #check for ennemies shot
        if not canShoot:
            index = 0
            while index < len(ennemyList):
                ennemyHit = pygame.sprite.spritecollide(ennemyList[index], friendlyGroup, False)
                if not ennemyHit == []:
                    ennemyList[index].playSound()
                    ennemyList.remove(ennemyList[index])
                index += 1
            ennemyShot = pygame.sprite.spritecollide(fireball, ennemyGroup, True)
            if fireball.rect.left > screen.get_width():
                canShoot = True
            if not ennemyShot == []:
                gameScore += 10
                monster = MonsterClass(speed)
                ennemyGroup.add(monster)
                ennemyList.append(monster)
                coins = "Score: %d" %gameScore
                scoreLabel = scoreFont.render(coins, 1, (255, 255, 255))
        
        #Check if player hit an ennemy
        hit = pygame.sprite.spritecollide(player, ennemyGroup, False)
        hasBeenShot = pygame.sprite.spritecollide(player, projectileGroup, True)
        if (not hit == [] or not hasBeenShot == []) and canBeHit:
            canBeHit = False
            player.hit()
            player.playHitSound()
            gameLives -= 1
            life = "Lives: %d" %gameLives
            liveLabel = scoreFont.render(life, 1, (255, 255, 255))
        if not canBeHit:
            liveSec += 1
            if liveSec == 30:
                liveSec = 0
                canBeHit = True
                player.hit()

        #check for collision with coins or lives
        coinHit = pygame.sprite.spritecollide(player, coinGroup, True)
        if not coinHit == []:
            gameScore += 5
            newCoin = CoinsClass(speed)
            coinGroup.add(newCoin)
            newCoin.playSound()
            coins = "Score: %d" %gameScore
            scoreLabel = scoreFont.render(coins, 1, (255, 255, 255))
        boxHit = pygame.sprite.spritecollide(player, lifeBoxGroup, True)
        if not boxHit == []:
            gameLives += 1
            newBox = LivesBoxClass()
            newBox.playSound()
            lifeBoxGroup.add(newBox)
            life = "Lives: %d" %gameLives
            liveLabel = scoreFont.render(life, 1, (255, 255, 255))
        
        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True
                elif event.key == pygame.K_SPACE and grounded and not isJumping:
                    player.playJumpSound()
                    isJumping, grounded = player.jump(grounded)
                elif event.key == pygame.K_RSHIFT and canShoot:

                    canShoot = False
                    fireball = FireballClass(player, speed)
                    fireball.playSound()
                    friendlyGroup.add(fireball)

        #set isJumping to False when the player touched the ground
        if grounded:
            isJumping = False

        #increase the game speed every 10km and adds a monster to the game
        if distCount == 10:
            distCount = 0
            speed += 1
            addMonster = MonsterClass(speed)
            ennemyGroup.add(addMonster)
            ennemyList.append(addMonster)

        #update the distance label
        dist = "%d km" %distance
        distLabel = scoreFont.render(dist, 1, (255, 255, 255))

        #Check for player lives
        if gameLives == 0:
            keepGoing = False
            donePlaying = False
    
        #refresh display
        screen.blit(background, (0, 0))

        #clears screen from all sprites
        backgroundGroup.clear(screen, background)
        forgroundGroup.clear(screen, background)
        lifeBoxGroup.clear(screen, background)
        coinGroup.clear(screen, background)
        ennemyGroup.clear(screen, background)
        projectileGroup.clear(screen, background)
        friendlyGroup.clear(screen, background)
        frontGroup.clear(screen, background)

        #updates groups
        backgroundGroup.update(screen, speed)
        forgroundGroup.update(screen, speed)
        lifeBoxGroup.update(screen, speed)
        coinGroup.update(screen, speed)
        ennemyGroup.update(screen, speed)
        projectileGroup.update(speed)
        friendlyGroup.update(grounded)
        frontGroup.update(screen)

        #draw groups at their new location on the screen
        backgroundGroup.draw(screen)
        forgroundGroup.draw(screen)
        lifeBoxGroup.draw(screen)
        coinGroup.draw(screen)
        ennemyGroup.draw(screen)
        projectileGroup.draw(screen)
        friendlyGroup.draw(screen)
        frontGroup.draw(screen)

        #display labels
        screen.blit(liveLabel, (10, 10))
        screen.blit(scoreLabel, (10, 30))
        screen.blit(bestScoreLabel, (10, 50))
        screen.blit(bestDistanceLabel, (10, 70))
        screen.blit(distLabel, (430, 10))
        
        pygame.display.flip()

    return gameScore, distance, donePlaying
    
if __name__ == "__main__":
    main()
        
        
