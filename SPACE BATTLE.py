"""Thank you for playing my first game! Here is the code that makes it all work.
I understand that some of this code may be a bit bulky and hard to follow,
but it's my first game!
Anyways, enjoy! --Jim"""

#Imports the library and all necessary modules
import pygame
from pygame.locals import *
import random

#Defining some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LOBLUE = (0, 0, 25)
ORANGE = (255, 155, 0)
GRAY = (150,150,160)
LOGRAY = (80,80,90)
HIBLUE = (70, 140, 255)

# ---- Create the window

#Initialize the Game Engine
pygame.init()

#import sounds for later GAME MUSIC REMOVED FOR BETA VERSION
##shooty_sound = pygame.mixer.Sound("laser5.ogg")

##MUSIC = [
        ##"ThemeSong",
        ##"other songs"
         ##]

#Set the width and height of the screen
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width,screen_height])
#The next line shows up on the top bar of the window
pygame.display.set_caption("SPACE BATTLE")

def title():
    """Calls up the title screen"""

    #This changes the music to the Title Theme GAME MUSIC REMOVED FOR BETA VERSION
    ##if pygame.mixer.music.get_busy() == False:
        ##pygame.mixer.music.load(MUSIC[0])
        ##pygame.mixer.music.play(-1)

    #This variable controls the menu navigation
    choice = 2
    
    #Set the loop up
    done = False
    while done == False:
        #Create the title screen
        screen.fill(BLACK)
        
        #Creating text:
        #Select the font to use, size, bold, italics
        font = pygame.font.SysFont('Ariel',72,True,False)
        #Render the text. "True" means anti-aliased text.
        #Note: This line creates an image of the letters,
        #but does NOT put it on the screen yet.
        text = font.render("SPACE BATTLES",True,ORANGE)
        screen.blit(text, [45,150])

        #Create the credits AND BETA SIGN
        font = pygame.font.SysFont('Ariel',30,True,False)
        text = font.render("A Wiseguy Game by Jim",True,ORANGE)
        screen.blit(text, [48, 200])
        font = pygame.font.SysFont('Ariel',72,True,False)
        text = font.render("BETA",False,HIBLUE)
        screen.blit(text, [247, 250])

        #Create the main menu
        font = pygame.font.SysFont('Ariel',40,True,False)
        text = font.render("PLAY",True,ORANGE)
        screen.blit(text, [48,320])
        text = font.render("INSTRUCTIONS",True,ORANGE)
        screen.blit(text, [198,320])
        text = font.render("CREDITS",True,ORANGE)
        screen.blit(text, [508, 320])
        font = pygame.font.SysFont('Ariel',27,True,False)
        text = font.render("USE THE ARROW KEYS AND ENTER TO SELECT",True,ORANGE)
        screen.blit(text, [108, 385])
        
        for event in pygame.event.get(): #User did something
            if event.type == pygame.QUIT: #If the user clicks close
                done = True


            #Creating menu navigation system
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if choice == 1:
                        choice = 3
                    elif choice == 2:
                        choice = 1
                    elif choice == 3:
                        choice = 2
                elif event.key == pygame.K_RIGHT:
                    if choice == 1:
                        choice = 2
                    elif choice == 2:
                        choice = 3
                    elif choice == 3:
                        choice = 1
                if event.key == pygame.K_RETURN:
                    if choice == 1:
                        pygame.mixer.music.stop()
                        main_game()
                    if choice == 2:
                        instructions()
                    if choice == 3:
                        show_credits()
                    #assign an arbitrary new value to the choice variable
                    #AND set done equal to true for when pygame.QUIT is called
                    choice = 4
                    done = True
                    
        #Reflecting menu navigation
        if choice == 1:
            pygame.draw.rect(screen,ORANGE,[44,315,87,34],5)
        elif choice == 2:
            pygame.draw.rect(screen,ORANGE,[194,315,252,34],5)
        elif choice == 3:
            pygame.draw.rect(screen,ORANGE,[503,315,145,34],5)
                
        pygame.display.flip()
        
def show_credits():
    """Let's everyone know without a doubt that I made this game"""
    done = False
    while done == False:
        #Create the credits screen
        screen.fill(BLACK)
        
        #Screen title
        font = pygame.font.SysFont('Ariel',72,True,False)
        text = font.render("CREDITS",True,ORANGE)
        screen.blit(text, [221,20])

        #Bulk of credits
        font = pygame.font.SysFont('Ariel',30,True,False)
        text = font.render("Lead Writer",True,ORANGE)
        screen.blit(text, [190,80])
        text = font.render("Storyboard",True,ORANGE)
        screen.blit(text, [195,100])
        text = font.render("Concept Art",True,ORANGE)
        screen.blit(text, [184,120])
        text = font.render("Actual Art",True,ORANGE)
        screen.blit(text, [205,140])
        text = font.render("Character Design",True,ORANGE)
        screen.blit(text, [122,160])
        text = font.render("Set Design",True,ORANGE)
        screen.blit(text, [201,180])
        text = font.render("Game Design",True,ORANGE)
        screen.blit(text, [176,200])
        text = font.render("Special Effects",True,ORANGE)
        screen.blit(text, [143,220])
        text = font.render("Revisions",True,ORANGE)
        screen.blit(text, [212,240])
        text = font.render("Publishing",True,ORANGE)
        screen.blit(text, [205,260])
        text = font.render("Public Relations",True,ORANGE)
        screen.blit(text, [134,280])
        text = font.render("Credits",True,ORANGE)
        screen.blit(text, [240,300])

        text = font.render("Jim",True,ORANGE)
        screen.blit(text, [380,80])
        screen.blit(text, [380,100])
        screen.blit(text, [380,120])
        screen.blit(text, [380,140])
        screen.blit(text, [380,160])
        screen.blit(text, [380,180])
        screen.blit(text, [380,200])
        screen.blit(text, [380,220])
        screen.blit(text, [380,240])
        screen.blit(text, [380,260])
        screen.blit(text, [380,280])
        screen.blit(text, [380,300])

        text = font.render("And special thanks to everyone",True,ORANGE)
        screen.blit(text, [140,380])
        text = font.render("who helped make this game by testing",True,ORANGE)
        screen.blit(text, [110,400])
        text = font.render("it and telling Jim what sucked.",True,ORANGE)
        screen.blit(text, [110,420])

        font = pygame.font.SysFont('Ariel',40,True,False)
        text = font.render("BACK",True,ORANGE)
        screen.blit(text, [295,460])
        pygame.draw.rect(screen,ORANGE,[291,455,94,34],5)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    title()
                    done = True
                
        pygame.display.flip()

def instructions():
    """Calls up the instruction screen"""
    
    #For the minimenu
    choice = 1
    
    def squarrow(x,y,letter):
        #Draws an arrow key on the screen
        pygame.draw.rect(screen,ORANGE,[x-30,y-30,60,60],10)
        font = pygame.font.SysFont('Ariel',45,True,False)
        text = font.render(letter,True,ORANGE)
        screen.blit(text, [x-12,y-12])

    done = False
    while done == False:
        screen.fill(BLACK)
        
        """The next block of code only makes up the words in the instructions"""
        #The bulk of the instructions
        font = pygame.font.SysFont('Ariel',72,True,False)
        text = font.render("INSTRUCTIONS",True,ORANGE)
        screen.blit(text, [140,10])
        font = pygame.font.SysFont('Ariel',24,True,False)
        text = font.render("The object of the game is to shoot the",True,ORANGE)
        screen.blit(text, [180,75])
        text = font.render("other player until their ship's health",True,ORANGE)
        screen.blit(text, [190,95])
        text = font.render("reaches zero. You should then assume",True,ORANGE)
        screen.blit(text, [180,115])
        text = font.render("that they blew up, because I didn't",True,ORANGE)
        screen.blit(text, [200,135])
        text = font.render("animate the ships exploding.",True,ORANGE)
        screen.blit(text, [220,155])
        
        text = font.render("Anyways, you fire PROJECTILES when",True,ORANGE)
        screen.blit(text, [182,245])
        text = font.render("you're MOVING. If you shoot and you",True,ORANGE)
        screen.blit(text, [190,265])
        text = font.render("are completely STATIONARY, then you",True,ORANGE)
        screen.blit(text, [188,285])
        text = font.render("will drop a MINE. Pretty cool, huh?",True,ORANGE)
        screen.blit(text, [197,305])
        
        font = pygame.font.SysFont('Ariel',34,True,False)
        text = font.render("PLAY WITH BOTH HANDS",True,ORANGE)
        screen.blit(text, [180,360])

        #Player classificaion
        font = pygame.font.SysFont('Ariel',30,True,False)
        text = font.render("PLAYER 1",True,ORANGE)
        screen.blit(text, [45,140])
        
        text = font.render("PLAYER 2",True,ORANGE)
        screen.blit(text, [545,140])
        
        #Key designation text
        font = pygame.font.SysFont('Ariel',26,True,False)
        text = font.render("MOVE",True,ORANGE)
        screen.blit(text, [73,340])
        screen.blit(text, [573,340])
        
        text = font.render("SHOOT",True,ORANGE)
        screen.blit(text, [80,185])
        screen.blit(text, [90,265])
        screen.blit(text, [550,185])
        screen.blit(text, [540,265])

        text = font.render("FORWARD",True,ORANGE)
        screen.blit(text, [80,205])
        screen.blit(text, [525,205])

        text = font.render("BACK",True,ORANGE)
        screen.blit(text, [98,285])
        screen.blit(text, [550,285])

        #Player 1 control/key diagram
        squarrow(100,400,"W")
        squarrow(40,460,"A")
        squarrow(100,460,"S")
        squarrow(160,460,"D")
        squarrow(40,205,"T")
        squarrow(50,285,"R")

        #Player 2 control/key diagram
        squarrow(600,400,"^")
        squarrow(540,460,"<")
        squarrow(600,460,"v")
        squarrow(660,460,">")
        squarrow(660,205,"3")
        squarrow(650,285,"2")

        #Minimenu
        font = pygame.font.SysFont('Ariel',40,True,False)
        text = font.render("PLAY",True,ORANGE)
        screen.blit(text, [243,395])
        text = font.render("BACK",True,ORANGE)
        screen.blit(text, [373,395])
        
        for event in pygame.event.get(): #User did something
            if event.type == pygame.QUIT: #If the user clicks close
                done = True
                
            #Minimenu navigation
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    choice = 1
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    choice = 2
                    
                if event.key == pygame.K_RETURN:
                    if choice == 1:
                        pygame.mixer.music.stop()
                        main_game()
                    elif choice == 2:
                        title()
                    choice = 4
                    done = True

        #Reflecting minimenu navigation
        if choice == 1:
            pygame.draw.rect(screen,ORANGE,[239,390,87,34],5)
        elif choice == 2:
            pygame.draw.rect(screen,ORANGE,[369,390,94,34],5)
                
        pygame.display.flip()
        

# ---- The playable part of the game
def main_game():
       
    #Set up the starfield (different every time)
    star_list = []
    for i in range(50):
        x = random.randrange(0,700)
        y = random.randrange(0,500)
        star_list.append([x,y])

    #Draw the background
    def space():
        screen.fill(LOBLUE)
        for i in range(len(star_list)):
            pygame.draw.circle(screen,WHITE,star_list[i],2)

    # ---- Player control configurations
    config_1 = {
        'number': 1,
        'color': RED,
        'left': pygame.K_a,
        'right': pygame.K_d,
        'up': pygame.K_w,
        'down': pygame.K_s,
        'fire_forward': pygame.K_t,
        'fire_back': pygame.K_r
        }
    config_2 = {
        'number': 2,
        'color': GREEN,
        'left': pygame.K_LEFT,
        'right': pygame.K_RIGHT,
        'up': pygame.K_UP,
        'down': pygame.K_DOWN,
        'fire_forward': pygame.K_KP3,
        'fire_back': pygame.K_KP2
        }

    # ---- Classes

    class Player(pygame.sprite.Sprite):
        """This class represents the player."""
        def __init__(self,x,controls):

            """set up the player on creation."""
            #call the parent class (Sprite) constructor
            super(Player,self).__init__()

            self.image = pygame.Surface([80,45])
            self.image.fill(WHITE)
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()

            self.rect.x = x
            self.rect.y = 250
            self.controls = controls
            
            self.acc = 5
            self.x_vel = 0
            self.y_vel = 0

            #draw the UFO
            pygame.draw.ellipse(self.image,BLACK,[0,5,80,40],0)
            pygame.draw.ellipse(self.image,GRAY,[2.5,7.5,77,37],0)
            pygame.draw.ellipse(self.image,BLACK,[21,0,40,18.5],0)
            pygame.draw.ellipse(self.image,BLACK,[36,25,10,10],0)
            pygame.draw.ellipse(self.image,BLACK,[6,10,10,10],0)
            pygame.draw.ellipse(self.image,BLACK,[66,10,10,10],0)
            pygame.draw.ellipse(self.image,self.controls['color'],[23.5,0,37,17],0)
            pygame.draw.ellipse(self.image,self.controls['color'],[38.5,27.5,7,7],0)
            pygame.draw.ellipse(self.image,self.controls['color'],[8.5,11.5,7,7],0)
            pygame.draw.ellipse(self.image,self.controls['color'],[68.5,11.5,7,7],0)

        def movement(self):
            #reset the player velocities to zero
            self.x_vel = 0
            self.y_vel = 0
            #If a key is pressed, accelerate the repsective velocity by five
            combo = pygame.key.get_pressed()
            if combo[self.controls['left']]:
                self.x_vel -= self.acc
            if combo[self.controls['right']]:
                self.x_vel += self.acc
            if combo[self.controls['up']]:
                self.y_vel -= self.acc
            if combo[self.controls['down']]:
                self.y_vel += self.acc          
                
        def update(self):
            #Add the velocities to the current position
            self.rect.x += self.x_vel
            self.rect.y += self.y_vel

            #If the UFO reaches a border, prevent it from leaving the screen
            if self.rect.x > 660:
                self.rect.x = 660
            elif self.rect.x < -40:
                self.rect.x = -40
            if self.rect.y > 480:
                self.rect.y = 480
            elif self.rect.y < 70:
                self.rect.y = 70

    class Health_bar(pygame.sprite.Sprite):
        """This class represents the player's health level"""
        def __init__(self,x,controls):
            
            """set up the health bar on creation."""
            #call up the parent class (Sprite) constructor
            super(Health_bar,self).__init__()

            self.image = pygame.Surface([210,70])
            self.image.fill(WHITE)
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()

            self.rect.x = x
            self.rect.y = 0
            self.controls = controls
            self.health = 100
            
            #Draw the health bar
            pygame.draw.rect(self.image,GRAY,[0,30,210,40],0)
            pygame.draw.rect(self.image,LOGRAY,[5,35,200,30],0)
            pygame.draw.rect(self.image,RED,[5,35,self.health*2,30],0)
            pygame.draw.rect(self.image,BLACK,[3,35,202,30],2)
            
            #Creat the text
            self.font = pygame.font.SysFont('Ariel', 29, True, False)
            text = self.font.render('PLAYER '+str(self.controls['number'])+" HEALTH:",False,ORANGE)
            self.image.blit(text, [0,10])
            
        def update(self):
            #Draw the current health level
            pygame.draw.rect(self.image,LOGRAY,[5,35,200,30],0)
            pygame.draw.rect(self.image,RED,[5,35,self.health*2,30],0)
            pygame.draw.rect(self.image,BLACK,[3,35,202,30],2)

    class Plasma_ball_forward(pygame.sprite.Sprite):
        """this object represents the player's shots"""
        def __init__(self,controls):

            """Set up the Plasma ball on creation"""
            #Call the parent class (Sprite) constructor
            super(Plasma_ball_forward,self).__init__()
            
            self.image = pygame.Surface([16,16])
            #since this object uses white in its color scheme,
            #use a different-colored colorkey
            self.image.fill(ORANGE)
            self.image.set_colorkey(ORANGE)
            self.rect = self.image.get_rect()

            self.controls = controls
            
            self.acc = 20
            self.x_vel = 0
            self.y_vel = 0

            #Draw the plasma ball
            pygame.draw.ellipse(self.image,controls['color'],[0,0,16,16],0)
            pygame.draw.ellipse(self.image,WHITE,[3,3,10,10],0)

            #Find out what direction the shot was in and accelerate accordingly
            combo = pygame.key.get_pressed()
            if combo[self.controls['left']]:
                self.x_vel = -self.acc
            if combo[self.controls['right']]:
                self.x_vel = self.acc
            if combo[self.controls['up']]:
                self.y_vel = -self.acc
            if combo[self.controls['down']]:
                self.y_vel = self.acc
                
        def update(self):
            #Add the velocities to the current position
            self.rect.x += self.x_vel
            self.rect.y += self.y_vel

    class Plasma_ball_back(pygame.sprite.Sprite):
        """this object represents the player's shots"""
        def __init__(self,controls):

            """Set up the Plasma ball on creation"""
            #Call the parent class (Sprite) constructor
            super(Plasma_ball_back,self).__init__()
            
            self.image = pygame.Surface([16,16])
            #since this object uses white in its color scheme,
            #use a different-colored colorkey
            self.image.fill(ORANGE)
            self.image.set_colorkey(ORANGE)
            self.rect = self.image.get_rect()

            self.controls = controls
            
            self.acc = 20
            self.x_vel = 0
            self.y_vel = 0

            #Draw the plasma ball
            pygame.draw.ellipse(self.image,controls['color'],[0,0,16,16],0)
            pygame.draw.ellipse(self.image,WHITE,[3,3,10,10],0)

            #Find out what direction the shot was in and accelerate accordingly
            combo = pygame.key.get_pressed()
            if combo[self.controls['left']]:
                self.x_vel = self.acc
            if combo[self.controls['right']]:
                self.x_vel = -self.acc
            if combo[self.controls['up']]:
                self.y_vel = self.acc
            if combo[self.controls['down']]:
                self.y_vel = -self.acc
                
        def update(self):
            #Add the velocities to the current position
            self.rect.x += self.x_vel
            self.rect.y += self.y_vel

    # ---- Sprite lists

    #This is a list of every sprite; all shots and players combined.
    all_sprites_list = pygame.sprite.Group()

    #This is a list of each plasma ball shot by player 1
    plasma_list_1 = pygame.sprite.Group()
    #This is a list of each plasma ball shot by player 2
    plasma_list_2 = pygame.sprite.Group()


    # ---- Create the players and add them to the sprites list

    player_1 = Player(20,config_1)
    all_sprites_list.add(player_1)

    player_2 = Player(600,config_2)
    all_sprites_list.add(player_2)

    # ---- Create the health bars and add them to the sprites list

    p1_health_bar = Health_bar(10,config_1)
    all_sprites_list.add(p1_health_bar)

    p2_health_bar = Health_bar(480,config_2)
    all_sprites_list.add(p2_health_bar)

    #Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # ------ Countdown to start game ------
    for i in range(72):
        space()
        all_sprites_list.draw(screen)
        #This calls up a random non-title song to play GAME MUSIC REMOVED FOR BETA VERSION
        ##if pygame.mixer.music.get_busy() == False:
            ##pygame.mixer.music.load(MUSIC[1])
            ##pygame.mixer.music.play()
            
        font = pygame.font.SysFont('Ariel',72,True,False)
        if i <= 24:
            text = font.render("3",True,ORANGE)
            screen.blit(text, [330,230])
        if i > 24 and i <= 48:
            text = font.render("2",True,ORANGE)
            screen.blit(text, [330,230])
        if i > 48:
            text = font.render("1",True,ORANGE)
            screen.blit(text, [330,230])
            
        pygame.display.flip()
        
        #Establish the frames per second(standard: 24)
        clock.tick(24)

    #Set up the Main Program Loop
    done = False
    
    #The final countdown
    go = 0
    
    #Controls mini-menu navigation
    choice = 1
    
    # ------------ Main Program Loop ------------
    while done == False:

        # ---- Music Matrix REMOVED FOR BETA VERSION

        #This calls up a random song to play (except the title theme)
        ## if pygame.mixer.music.get_busy() == False:
            ## pygame.mixer.music.load(MUSIC[1])
            ## pygame.mixer.music.play()
            
        # ------ Event Processing ------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if p1_health_bar.health > 5 and p2_health_bar.health > 5:
                player_1.movement()
                player_2.movement()
                
            # ---- Firing plasma
            if event.type == pygame.KEYDOWN:
                if p1_health_bar.health > 5 and p2_health_bar.health > 5:
                    #Player 1's shot
                    if event.key == config_1['fire_forward']:
                        #shooty_sound.play()
                        shot = Plasma_ball_forward(config_1)
                        #Set the plasma shot so it is where player 1 is
                        shot.rect.x = player_1.rect.x + 32
                        shot.rect.y = player_1.rect.y + 22
                        #add the plasma shot to the lists
                        all_sprites_list.add(shot)
                        plasma_list_1.add(shot)
                    elif event.key == config_1['fire_back']:
                        #shooty_sound.play()
                        shot = Plasma_ball_back(config_1)
                        #Set the plasma shot so it is where player 1 is
                        shot.rect.x = player_1.rect.x + 32
                        shot.rect.y = player_1.rect.y + 22
                        #add the plasma shot to the lists
                        all_sprites_list.add(shot)
                        plasma_list_1.add(shot)
                    #Player 2's shot
                    if event.key == config_2['fire_forward']:
                        #shooty_sound.play()
                        shot = Plasma_ball_forward(config_2)
                        #Set the plasma shot so it is where player 1 is
                        shot.rect.x = player_2.rect.x + 32
                        shot.rect.y = player_2.rect.y + 22
                        #add the plasma shot to the lists
                        all_sprites_list.add(shot)
                        plasma_list_2.add(shot)
                    elif event.key == config_2['fire_back']:
                        #shooty_sound.play()
                        shot = Plasma_ball_back(config_2)
                        #Set the plasma shot so it is where player 1 is
                        shot.rect.x = player_2.rect.x + 32
                        shot.rect.y = player_2.rect.y + 22
                        #add the plasma shot to the lists
                        all_sprites_list.add(shot)
                        plasma_list_2.add(shot)
     
        # ------ Game Logic ------

        #calculate mechanics for each shot by player ONE
        for shot in plasma_list_1:
            
            #see if it hits player 2
            p1_hit_list = pygame.sprite.spritecollide(player_2,plasma_list_1,True)

            #for each successful hit, remove the bullet and reduce player 2's health
            for shot in p1_hit_list:
                plasma_list_1.remove(shot)
                p2_health_bar.health -= 10

            #remove the shot if it flies off the screen
            if shot.rect.x > 710 or shot.rect.x < -10:
                plasma_list_1.remove(shot)
            if shot.rect.y > 510 or shot.rect.y < -10:
                plasma_list_1.remove(shot)

        #calculate mechanics for each shot by player TWO
        for shot in plasma_list_2:
            
            #see if it hits player 1
            p2_hit_list = pygame.sprite.spritecollide(player_1,plasma_list_2,True)

            #for each successful hit, remove the bullet and reduce player 2's health
            for shot in p2_hit_list:
                plasma_list_2.remove(shot)
                p1_health_bar.health -= 10

            #remove the shot if it flies off the screen
            if shot.rect.x > 710 or shot.rect.x < -10:
                plasma_list_2.remove(shot)
            if shot.rect.y > 510 or shot.rect.y < -10:
                plasma_list_2.remove(shot)

        #check if player 1 has lost
        if p1_health_bar.health < 1:
            p1_health_bar.health = 1
            all_sprites_list.remove(player_1)
        #check if player 2 has lost
        if p2_health_bar.health < 1:
            p2_health_bar.health = 1
            all_sprites_list.remove(player_2)
            player_1.x_vel = 0
            player_1.y_vel = 0

        #If the game is over, do... something.
        if p1_health_bar.health < 5 or p2_health_bar.health < 5:
                player_1.rect.x = 310
                player_2.rect.x = 310
                player_1.rect.y = 200
                player_2.rect.y = 200
                
        all_sprites_list.update()

        # ------ Screen Drawing ------
        space()
        all_sprites_list.draw(screen)
        #The "final number" in the game-start countdown
        if go <= 24:
            font = pygame.font.SysFont('Ariel',72,True,False)
            text = font.render("GO!",True,ORANGE)
            screen.blit(text, [310,230])
            go += 1

        # ---- If a player dies (Game Over)
         
        if p1_health_bar.health < 5 or p2_health_bar.health < 5:
            #Tie Game
            if p1_health_bar.health < 5 and p2_health_bar.health < 5:
                font = pygame.font.SysFont('Ariel',72,True,False)
                text = font.render('TIE GAME!!!',True,ORANGE)
                screen.blit(text, [175,250])
            #Player 1 wins
            elif p2_health_bar.health < 5:
                font = pygame.font.SysFont('Ariel',72,True,False)
                text = font.render('PLAYER 1 WINS!!!',True,ORANGE)
                screen.blit(text, [110,250])
            #Player 2 wins
            else:
                font = pygame.font.SysFont('Ariel',72,True,False)
                text = font.render('PLAYER 2 WINS!!!',True,ORANGE)
                screen.blit(text, [110,250])

            #Create the Game Over mini-menu
            font = pygame.font.SysFont('Ariel',31,True,False)
            text = font.render("PLAY AGAIN",True,ORANGE)
            screen.blit(text, [170,310])
            text = font.render("MAIN MENU",True,ORANGE)
            screen.blit(text, [380,310])

            #mini-menu navigation
            restart = pygame.key.get_pressed()
            if restart[pygame.K_LEFT] or restart[pygame.K_a]:
                    choice = 1
            elif restart[pygame.K_RIGHT] or restart[pygame.K_d]:
                    choice = 2
            elif restart[pygame.K_RETURN]:
                if choice == 1:
                    main_game()
                elif choice == 2:
                    title()
                #assign an arbitrary new value to the choice variable
                #AND set done equal to true for when pygame.QUIT is called
                choice = 3
                done = True

            #Reflecting mini-menu navigation
            if choice == 1:
                pygame.draw.rect(screen,ORANGE,[166,305,156,28],5)
            elif choice == 2:
                pygame.draw.rect(screen,ORANGE,[375,305,147,28],5)  
        
        pygame.display.flip()

        #Establish the frames per second(standard: 24)
        clock.tick(24)

    # ------------ End of Main Program Loop ------------

# ---- Running the game
title()
#If any loop is exited, close the program
pygame.quit()
