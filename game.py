import pygame 
import random
import os

#initialise pygame modules
pygame.init()

#create screen width and height
screen_width, screen_height = 1040, 680
screen = pygame.display.set_mode((screen_width, screen_height))

#create play, prize and enemy
current_path = os.path.dirname("/Users/lucmaingard/Dropbox/Luc Maingard-50841/Introduction to Programming/Task 15/game.py")
image_path_player = os.path.join(current_path, 'player.png')
image_path_enemy1 = os.path.join(current_path, 'monster2.png')
image_path_enemy_still = os.path.join(current_path, 'enemy2.png')
image_path_enemy2 = os.path.join(current_path, 'enemy3.jpg')
image_path_prize = os.path.join(current_path, 'prize1.png')

player = pygame.image.load(image_path_player)
enemy1 =  pygame.image.load(image_path_enemy1)
enemy2 =  pygame.image.load(image_path_enemy2)
enemy_still =  pygame.image.load(image_path_enemy_still)
prize = pygame.image.load(image_path_prize)

#get heights and widths of player, prize and enemy
player_height, player_width = player.get_height(), player.get_width()
enemy1_height, enemy1_width = enemy1.get_height(), enemy1.get_width()
enemy2_height, enemy2_width = enemy2.get_height(), enemy2.get_width()
enemy_still_height, enemy_still_width = enemy_still.get_height(), enemy_still.get_width()
prize_height, prize_width = prize.get_height(), prize.get_width()

print(f"The height of the player is {player_height}, and width is {player_width}")    
print(f"The height of the enemy1 is {enemy1_height}, and width is {enemy1_width}")
print(f"The height of the enemy2 is {enemy2_height}, and width is {enemy2_width}") 
print(f"The height of the still enemy is {enemy_still_height}, and width is {enemy_still_width}")       
print(f"The height of the prize is {prize_height}, and width is {prize_width}")      

#initialise player, enemy and prize locations (Initialise prize and enemy locations to be random)
playerXlocation, playerYlocation = 100, 500
enemy1Xlocation, enemy1Ylocation = screen_width, random.randint(0, screen_height - enemy1_height) 
enemy2Xlocation, enemy2Ylocation = random.randint(0, screen_width - enemy2_width), screen_height
enemy_stillXlocation, enemy_stillYlocation = random.randint(300, 800), random.randint(200, 400)
prizeXlocation, prizeYlocation = random.randint(0, screen_width - prize_height), random.randint(0, screen_height - prize_height)

#check that enemy and prize locations are not the same location as player location
#if they the same -> make new locations 
if enemy1Xlocation == playerXlocation or enemy1Ylocation == playerYlocation:
    enemy1Xlocation, enemy1Ylocation = screen_width, random.randint(0, screen_height - enemy1_height)
elif enemy2Xlocation == playerXlocation or enemy2Ylocation == playerYlocation:
    enemy2Xlocation, enemy2Ylocation = random.randint(0, screen_width - enemy2_width), screen_height
elif prizeXlocation == playerXlocation or prizeYlocation == playerYlocation:
    prizeXlocation, prizeYlocation = random.randint(0, screen_width - prize_height), random.randint(0, screen_height - prize_height)

#check if keys are pressed (initialise them as false)
keyUp = False
keyDown = False
keyL = False
keyR = False

#start game loop
while 1:

    #clear screen and draw characters on screen
    screen.fill(0)
    screen.blit(player, (playerXlocation, playerYlocation))
    screen.blit(enemy1, (enemy1Xlocation, enemy1Ylocation))
    screen.blit(enemy2, (enemy2Xlocation, enemy2Ylocation))
    screen.blit(enemy_still, (enemy_stillXlocation, enemy_stillYlocation))
    screen.blit(prize, (prizeXlocation, prizeYlocation))

    #update screen
    pygame.display.flip()

    #loop through game events
    for event in pygame.event.get():

        #check if user wants to quit
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        
        #check if user presses a key down
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyL = True
            if event.key == pygame.K_RIGHT:
                keyR = True
        
        #check if key is up
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyL = False
            if event.key == pygame.K_RIGHT:
                keyR = False
            
    #after checking event key -> move player accordingly
    #add random movement for enemy_still depending on key pressed by user to make more unpredictable
    if keyUp == True:
        if playerYlocation > 0:
            playerYlocation -= 1.5
            enemy_stillYlocation -= random.randint(-15, 15)
            enemy_stillXlocation -= random.randint(-30, 30)

    if keyDown == True:
        if playerYlocation < (screen_height - player_height): 
            playerYlocation += 1.5
            enemy_stillYlocation -= random.randint(-15, 15)
            enemy_stillXlocation -= random.randint(-30, 30)

    if keyL == True:
        if playerXlocation > 0:
            playerXlocation -= 1.5
            enemy_stillYlocation -= random.randint(-15, 15)
            enemy_stillXlocation -= random.randint(-30, 30)

    if keyR == True:
        if playerXlocation < (screen_width - player_width):
            playerXlocation += 1.5
            enemy_stillYlocation -= random.randint(-15, 15)
            enemy_stillXlocation -= random.randint(-30, 30)

    #get boxes for player, enemy, and prize
    playerBox = pygame.Rect(player.get_rect())
    playerBox.top = playerYlocation
    playerBox.left = playerXlocation

    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1Ylocation
    enemy1Box.left = enemy1Xlocation

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2Ylocation
    enemy2Box.left = enemy2Xlocation

    enemy_stillBox = pygame.Rect(enemy_still.get_rect())
    enemy_stillBox.top = enemy_stillYlocation
    enemy_stillBox.left = enemy_stillXlocation

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYlocation
    prizeBox.left = prizeXlocation

    #check if player collides with enemy
    if playerBox.colliderect(enemy1Box) or playerBox.colliderect(enemy2Box) or playerBox.colliderect(enemy_stillBox):

        print("\nYou lose :(\n")

        pygame.quit()
        exit(0)

    #if player collides with prize player wins
    if playerBox.colliderect(prizeBox):
            
        print("\nYou win :)\n")

        pygame.quit()
        exit(0)

    #move enemy and prize
    enemy1Xlocation -= 0.25

    enemy2Ylocation -= 0.25
