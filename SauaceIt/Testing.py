import pygame
import random
import time
import math

# initialize
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))


BGImg = pygame.image.load("BG.png")


# Icon and the title

pygame.display.set_caption("Testing Bruh")
pygame.display.set_icon(pygame.image.load("fast-food.png"))

# Player
playerImg = pygame.image.load("ketchup.png")
playerX = 370
playerY = 480
playerX_change = 0

endge = False

def player(x, y):
    screen.blit(playerImg, (x, y))



friend1Img = pygame.image.load("samosa.png")
friend1X = random.randint(0,800)
friend1Y = random.randint(50,150)
friend1X_change = 0

def enemy1(x, y):
    screen.blit(friend1Img, (x, y))


bullet = pygame.image.load("drop.png")
bulletX = 370
bulletY = 480
bullet_state = "NF" # NF not fired and Fired

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "F"
    screen.blit(bullet,(x+16,y+10))


def collide(x1,y1,x2,y2):
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distance

# Game loop
running = True
while running:

    screen.fill((0, 150, 255))

    screen.blit(BGImg,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_SPACE and bullet_state == "NF":
            bulletX = playerX
            fire_bullet(bulletX, bulletY)

        if event.key == pygame.K_LEFT:
            playerX_change = -0.9
        if event.key == pygame.K_LEFT and pygame.key.get_mods() & pygame.KMOD_SHIFT:
            playerX_change = -3

        if event.key == pygame.K_RIGHT:
            playerX_change = +0.9
        if event.key == pygame.K_RIGHT and pygame.key.get_mods() & pygame.KMOD_SHIFT:
            playerX_change = +3

        if event.key == pygame.K_RIGHT and pygame.key.get_mods() & pygame.K_LEFT:
            break

    if event.type == pygame.KEYUP:
        playerX_change = 0

    playerX += playerX_change

    if float(playerX) >= 730:
        playerX = 730

    if float(playerX) <= 0:
        playerX = 0

    if float(friend1X) <= 730 and endge == True:
        friend1X -= 1.5
        if float(friend1X) <= 30:
            friend1X = 30
            endge = False


    elif float(friend1X) >= 0 and endge == False:
        friend1X += 1.5
        if float(friend1X) >= 730:
            friend1X = 730
            endge = True

    if bullet_state == "F":
        fire_bullet(bulletX, bulletY)
        bulletY-=10

    if bullet_state == "F" and bulletY <=0:
        bullet_state = "NF"
        bulletY = 450

    if collide(bulletX,bulletY, friend1X, friend1Y)  < 30:
        print("HIT!!!!!!!!!!")
        bullet_state = "NF"
        bulletY = 450
        friend1X = random.randint(0, 800)
        friend1Y = random.randint(50, 150)
        endge = False



    friend1Y += 0.1
    enemy1(friend1X, friend1Y)
    player(playerX, playerY)


    pygame.display.update()
