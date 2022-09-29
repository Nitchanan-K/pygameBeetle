import pygame
from sys import exit



pygame.init()
screen = pygame.display.set_mode((800,400))

# game title
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('../pygameBeetle/basicgamelogic/font/Pixeltype.ttf',50)


# make surface from png
# background and text
sky_surface = pygame.image.load('../pygameBeetle/basicgamelogic/graphics/Sky.png').convert()
ground_surface = pygame.image.load('../pygameBeetle/basicgamelogic/graphics/ground.png').convert()


# score 
score_surface = test_font.render('My game', False,(64,64,64)).convert()
# score rectangle 
score_rect = score_surface.get_rect(center = (400,50))


# snail 
snail_surface = pygame.image.load('../pygameBeetle/basicgamelogic/graphics/snail/snail1.png').convert_alpha()
# snail rectangle
snail_rect = snail_surface.get_rect(midbottom = (600,300))


# player
player_surface = pygame.image.load('../pygameBeetle/basicgamelogic/graphics/Player\player_walk_1.png').convert_alpha()
# make rectangle 
player_rect = player_surface.get_rect(midbottom = (80,300))
# set garvity
player_gravity = 0



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        # is mouse pressed  and mouse is on player than jump    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                player_gravity = -20
                
                        
        # is botton pressed or release  
        # event type is look for event // event.key look for key being press      
        if event.type == pygame.KEYDOWN and player_rect.bottom == 300:
            if event.key == pygame.K_SPACE:
                player_gravity = -20 # get player move up 
                print('jump')
        if event.type == pygame.KEYUP:
            print('keyup')


        # mouse collision 
    '''if event.type == pygame.MOUSEMOTION:
            print(event.pos)
            if player_rect.collidepoint(event.pos):
                print('mouse is at same postion as player')'''

    # blit is put one surface to another surface(surface,position)
    # background blit
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))


    # text blit with rect
    pygame.draw.rect(screen,'#c0e8ec',score_rect) # fill space  
    pygame.draw.rect(screen,'#c0e8ec',score_rect,width=10) # add margin around it 
    screen.blit(score_surface,score_rect)


    # snail blit 
    # snail animation
    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surface,snail_rect,)


    # player blit and player animation
    # move rectangle that contain the surface instance of move image itslef
    
    # make player garvity 
    # first loop y == 300 + 1 // second loop y == 300 + 2 player_gravity increment 1 by each loop
    player_gravity += 1
    player_rect.y += player_gravity
    # make floor // if player pos > 300(falldown) reset to 300 
    if player_rect.bottom >= 300: 
        player_rect.bottom = 300
    screen.blit(player_surface,player_rect)
    
   
    
 
 
    # keybroad input // codition for input
    '''keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print('jump')'''
        
                      

    # make collision
    #if player_rect.colliderect(snail_rect): # return 0 if no collision / 1 if is collision 
    #   print('collision')


    # check mouse pressed 
    '''mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint((mouse_pos)):
        print(pygame.mouse.get_pressed())'''


    # draw all our elements
    # update everything
    pygame.display.update()
    clock.tick(60)