import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        # inherit from sprite clsee to __init__\
        super().__init__()

        player_walk1 = pygame.image.load('../pygameBeetle/basicgamelogic/graphics/Player\player_walk_1.png').convert_alpha()
        player_walk2 = pygame.image.load('../pygameBeetle/basicgamelogic/graphics/Player\player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk1,player_walk2]
        self.player_index = 0
        self.player_jump = pygame.image.load('../pygameBeetle/basicgamelogic/graphics/Player\jump.png').convert_alpha()
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom =(80,300))
        self.gravity = 0
    
        self.jump_sound = pygame.mixer.Sound('../pygameBeetle/basicgamelogic/audio/jump.mp3')
        self.jump_sound.set_volume(0.2) # lower sound max is 1 

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300: self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300 :
        # jump
            self.image = self.player_jump
        else:
        # walk
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk): self.player_index =0
            self.image = self.player_walk[int(self.player_index)] 
        
        return player_surface
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        # import differ typr of obstacle depends on the type parameter

        if type == 'fly':
            fly_1 = pygame.image.load('../pygameBeetle/basicgamelogic/graphics/fly/fly1.png').convert_alpha()
            fly_2 = pygame.image.load('../pygameBeetle/basicgamelogic/graphics/fly/fly2.png').convert_alpha()
            self.frames = [fly_1,fly_2] # make list with all frames
            y_pos = 210
        else:
            snail_1 = pygame.image.load('../pygameBeetle/basicgamelogic/graphics/snail/snail1.png').convert_alpha()
            snail_2 = pygame.image.load('../pygameBeetle/basicgamelogic/graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_1,snail_2] # make list with all frames
            y_pos = 300
        
        self.animation_index = 0
        self.image = self.frames[self.animation_index] # make surface by using list 
        self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))

    def animation_state(self):
        # animate 
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <=-100:
            self.kill # this .kill will destroy this "sprite"

# fucntion for score
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surface.get_rect(center=(400,50))
    screen.blit(score_surface,score_rect)
    return current_time
   
 # fucntion for obstacle 
def obstacle_movement(obstacle_list):
    if obstacle_list: # if list empty not run
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            
            # distint fly and snail to blit by bottom pos 
            if obstacle_rect.bottom == 200:
                screen.blit(fly_surface,obstacle_rect)
            else:   
                screen.blit(snail_surface,obstacle_rect)
        
        # list will copy the item only if obstacle is on screen so x pos > -100
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        
        return obstacle_list
    else: return[]

# function for collision 
# logic = if player rect collided with one of the obstacle in list game = end 
def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite,obstacle_group,False): # this reture a list 
        obstacle_group.empty()
        return False
    else: 
        return True

# player animation
def player_animation():
    global player_index,player_surface
    # play walking animation if the player on the floor 
    # play jump if player is not on floor
    if player_rect.bottom < 300 :
        # jump
        player_surface = player_jump
    else:
        # walk
        player_index += 0.1
        if player_index >= len(player_walk):player_index =0
        player_surface = player_walk[int(player_index)] 
        
        return player_surface

pygame.init()
screen = pygame.display.set_mode((800,400))
# game title
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('../pygameBeetle/basicgamelogic/font/Pixeltype.ttf',50)
# state of game 
game_active = False
# start time 
start_time = 0
# score
score = 0
# bg music 
bg_music = pygame.mixer.Sound('../pygameBeetle/basicgamelogic/audio/music.wav') 
bg_music.set_volume(0.1)
bg_music.play(loops = -1) # -1 is forever loops 

# initiate player class group
player = pygame.sprite.GroupSingle()
player.add(Player()) # add intance of player

# initiate obstacle class group
obstacle_group = pygame.sprite.Group()


# make surface from png
# background and text
sky_surface = pygame.image.load('../pygameBeetle/basicgamelogic/graphics/Sky.png').convert()
ground_surface = pygame.image.load('../pygameBeetle/basicgamelogic/graphics/ground.png').convert()


# score 
score_surface = test_font.render('My game', False,(64,64,64)).convert()
# score rectangle 
score_rect = score_surface.get_rect(center = (400,50))

## obstacles
# snail 
snail_surface_1 = pygame.image.load('../pygameBeetle/basicgamelogic/graphics/snail/snail1.png').convert_alpha()
snail_surface_2 = pygame.image.load('../pygameBeetle/basicgamelogic/graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_surface_1,snail_surface_2]
snail_frame_index = 0
snail_surface = snail_frames[snail_frame_index]

# fly 
fly_surface_1 = pygame.image.load('../pygameBeetle/basicgamelogic/graphics/fly/fly1.png').convert_alpha()
fly_surface_2 = pygame.image.load('../pygameBeetle/basicgamelogic/graphics/fly/fly2.png').convert_alpha()
fly_frames = [fly_surface_1,fly_surface_2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]

# list of obstacles
obstacle_rect_list = []

# player
player_walk1 = pygame.image.load('../pygameBeetle/basicgamelogic/graphics/Player\player_walk_1.png').convert_alpha()
player_walk2 = pygame.image.load('../pygameBeetle/basicgamelogic/graphics/Player\player_walk_2.png').convert_alpha()
player_walk = [player_walk1,player_walk2]
player_index = 0
player_jump = pygame.image.load('../pygameBeetle/basicgamelogic/graphics/Player\jump.png').convert_alpha()

player_surface = player_walk[player_index]
# make rectangle 
player_rect = player_surface.get_rect(midbottom = (80,300))
# set garvity
player_gravity = 0

# intro screen 
player_stand = pygame.image.load('../pygameBeetle/basicgamelogic/graphics/Player/player_stand.png').convert_alpha() # import 
player_stand = pygame.transform.rotozoom(player_stand,0,2)  # resize the surface 
player_stand_rect = player_stand.get_rect(center = (400,200))  # make the rect 
# game title 
game_title = test_font.render('Pix Runner',False,(111,196,169)).convert()
game_title_rect = game_title.get_rect(center = (400,50))
# game instructions
game_instruction = test_font.render('Spacebar to Start and Jump',False,(64,64,64)).convert()
game_instruction_rect = game_instruction.get_rect(center = (400,350))

# TIMER EVENT 
obstacle_timer = pygame.USEREVENT + 1 
pygame.time.set_timer(obstacle_timer,1500) # trigger per 1500 ms

snail_animation_timer = pygame.USEREVENT + 2 
pygame.time.set_timer(snail_animation_timer,500)

fly_animation_timer = pygame.USEREVENT + 3 
pygame.time.set_timer(fly_animation_timer,200)



#############################################################

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:   
            # is mouse pressed  and mouse is on player than jump    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                    player_gravity = -20
        
            # is botton pressed or release  
            # event type is look for event // event.key look for key being press      
            if event.type == pygame.KEYDOWN and player_rect.bottom == 300:
                if event.key == pygame.K_SPACE:
                    player_gravity = -20 # get player move up 
                    
            if event.type == pygame.KEYUP:
                print('keyup')


        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                 game_active = True
                 start_time = int(pygame.time.get_ticks() / 1000)              

        if game_active: # if game active check for timer event 
            # add timer tigger event (add enmies)
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly','snail','snail','snail'])) ) # more change to get snail (75%)

                #if randint(0,2): # random 0 or 1 (True or False)
                    #obstacle_rect_list.append(snail_surface.get_rect(midbottom = (randint(900,1100),300)))
                #else:
                    #obstacle_rect_list.append(fly_surface.get_rect(midbottom = (randint(900,1100),200)))

            # animate snail with time event
            if event.type == snail_animation_timer:
                if snail_frame_index == 0: snail_frame_index = 1
                else: snail_frame_index = 0
                # set it to snail surface 
                snail_surface = snail_frames[snail_frame_index]
            # animate fly with time event 
            if event.type == fly_animation_timer: 
                if fly_frame_index == 0: fly_frame_index = 1
                else: fly_frame_index = 0
                # set its to fly surface 
                fly_surface = fly_frames[fly_frame_index]

        # mouse collision 
    '''if event.type == pygame.MOUSEMOTION:
            print(event.pos)
            if player_rect.collidepoint(event.pos):
                print('mouse is at same postion as player')'''


 ####################### blit things on screen
    if game_active:
        # blit is put one surface to another surface(surface,position)
        # background blit
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))


        # text blit with rect
       #pygame.draw.rect(screen,'#c0e8ec',score_rect) # fill space  
       # pygame.draw.rect(screen,'#c0e8ec',score_rect,width=10) # add margin around it 
       # screen.blit(score_surface,score_rect)
       # show score with function 
        score = display_score()


        # snail blit 
        # snail animation
        #snail_rect.x -= 4
        #if snail_rect.right <= 0:
        #    snail_rect.left = 800
        #screen.blit(snail_surface,snail_rect)

        # player blit and player animation
        # move rectangle that contain the surface instance of move image itslef
        # make player garvity 
        # first loop y == 300 + 1 // second loop y == 300 + 2 player_gravity increment 1 by each loop
       
        #player_gravity += 1
        #player_rect.y += player_gravity
        # make floor // if player pos > 300(falldown) reset to 300 
        #if player_rect.bottom >= 300: player_rect.bottom = 300
        #player_animation()
        #screen.blit(player_surface,player_rect)
        
        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        # obstacle movement
        #obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # collision for game state 
        game_active = collision_sprite() # get boolean from funtions 
        #game_active = collisions(player_rect,obstacle_rect_list)

    else: 
        # end game and intro screen when game state is False
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        # reset enmies by empty obstacle rect list
        obstacle_rect_list.clear()
        # reset player 
        player_rect.midbottom = (80,300)
        player_gravity = 0
        # add game title 
        screen.blit(game_title,game_title_rect)

        # score after dead
        score_massage = test_font.render(f'Your score: {score}',False,(111,196,169))
        score_massage_rect = score_massage.get_rect(center = (400,350))

        # condition if have score will not show instruction and show score 
        if score == 0:
            # add game instructions
            screen.blit(game_instruction,game_instruction_rect)
        else: 
            screen.blit(score_massage,score_massage_rect)

    
        
        

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