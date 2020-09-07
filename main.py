import pygame
import player,enemy

pygame.init()

# Create Screen
screen = pygame.display.set_mode((800,600))
bkg = pygame.image.load("bkg.jpg")

# Title
pygame.display.set_caption("Space Raiders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerobj = player.Player(30,255,screen,playerImg)

# Enemy
enemyImg = pygame.image.load('monster.png')
enemyobj = enemy.MoonVader(750, 10, screen,enemyImg)

# Bullet Image
bulletImg = pygame.image.load('bullet.png')

def handle_keydown(eventkey):
    default_change = 7
    if(eventkey == pygame.K_LEFT):
        playerobj.updateXchange(-default_change)
    if(eventkey == pygame.K_RIGHT):
        playerobj.updateXchange(default_change)
    if(eventkey == pygame.K_UP):
        playerobj.updateYchange(-default_change)
    if(eventkey == pygame.K_DOWN):
        playerobj.updateYchange(default_change)
    if(eventkey == pygame.K_SPACE):
        playerobj.createBullet(bulletImg)


def handle_keyup(eventkey):
    if(eventkey == pygame.K_LEFT or eventkey == pygame.K_RIGHT):
        playerobj.updateXchange(0)
    elif (eventkey == pygame.K_UP or eventkey == pygame.K_DOWN):
        playerobj.updateYchange(0)


running = True

# NOTE to get events use pygame.event.get()

while running:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False

        if(event.type == pygame.KEYDOWN):
            handle_keydown(event.key)
        
        if (event.type == pygame.KEYUP):
            handle_keyup(event.key)
        

    # screen.fill((255,255,255))
    screen.fill((0,0,0))

    # Background
    screen.blit(bkg,(0,0))

    playerobj.updateX()
    playerobj.updateY()
    playerobj.playercontrol()

    if(playerobj.bulletstate):
        playerobj.fireBullet()

    enemyobj.moveEnemy()
    enemyobj.display()

    # Update display after every iteration.
    pygame.display.update()

