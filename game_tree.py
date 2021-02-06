import time
import sys
import pygame
from pygame.locals import *
import time
import random

#### COLOR 
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARK = (0, 0, 0)
DARK_GRAY = (32, 32, 32)
WHITE = (255, 255, 255)

#### speep 10 FPS
SPEED = 18
DELAY=30
TIME_FINISH = 10


SIZE=20

####  CONFIGURATIONS OF THE GAME

title_window="My first Game!"

### message
title_game="Wherever you, go GOD is with you!"
title_size=40
title_x=45 
title_y=180
title_color=WHITE

#### COLOR GRID
color_grid=GREEN

###  COLOR WINDOW MAIN 
backgroundcolor = (DARK_GRAY)
screen_width = 600
screen_height = 400

###  COLOR GAME OVER 
screen_width = 600
screen_height = 400


####score
class Texto(pygame.sprite.Sprite):
    def __init__(self,size):
        super().__init__()
        self.myfont=pygame.font.Font("font/Game_over.ttf",size)

    def set(self,text):
        self.image=self.myfont.render(text,1,WHITE)
        self.rect = self.image.get_rect()      
####apple
class apple(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image=pygame.image.load("images/Apple.png").convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=pos_x
        self.rect.y=pos_y
####snake
class Snake(pygame.sprite.Sprite):
    #### constructor
    def __init__(self,length):
        super().__init__()
        #### load character
        self.length=length 
        self.image=pygame.image.load("images/snake.jpg").convert() 
        self.rect = self.image.get_rect()
        self.direction ='down'
        self.rect.x=0
        self.rect.y=0

    #### walk
    def walk(self):

        #for i in range(self.length-1,3):
            #self.rect.x[i]=self.rect.x[i-1]
            #self.rect.y[i]=self.rect.y[i-1]

        if self.direction=='left' and self.rect.x>1 :
            self.rect.x-=SIZE
        if self.direction=='right' and self.rect.x< screen_width - SIZE:
            self.rect.x+=SIZE
        if self.direction=='up'   and self.rect.y>1 :
            self.rect.y-=SIZE
        if self.direction=='down'  and self.rect.y< screen_height-SIZE:
            self.rect.y+=SIZE

        
    #### move left 
    def move_left(self):
        self.direction='left'
    #### move right 
    def move_right(self):
        self.direction='right'
    #### move up 
    def move_up(self):
        self.direction='up'
    #### move down 
    def move_down(self):
        self.direction='down'     
####game
class Game:

    #### constructor
    def __init__(self):
        #### initialize all imported pygame modules 
        pygame.init()

        #### score initializar
        self.score=0
        self.time_down=TIME_FINISH
        self.aux=1

        #### create a window 
        self.surface=pygame.display.set_mode((screen_width,screen_height))

        #### title
        pygame.display.set_caption(title_window)

        #### creating a clock object
        self.clock = pygame.time.Clock()
        
        ###current time
        current_time=0

        #### grupo apples
        self.list_apple =pygame.sprite.Group()
        
        #### create my labels Score /Timeove
        self.myScore=Texto(50)
        self.myTime=Texto(50)
        
        #### create a instance o objet snake
        self.mySnake=Snake(2)
        self.xplayer=pygame.sprite.RenderPlain(self.mySnake)

        #### create appless
        for x in range(1,14,1):
            for y in range(1,19,1):
                myapples=apple(302+x*20,20*y)
                self.list_apple.add(myapples)

    #### finish window                                                                                                                          
    def finish(self):
        pygame.quit()
        sys.exit()

    #### display grid
    def display_grid(self):
        rows =20
        w=screen_width
        h=screen_height
        x=300
        y=0

        for l in range(rows):
            x=x+SIZE
            y=y+SIZE
            pygame.draw.line(self.surface,color_grid,(x,0),(x,h))
            # x,y
            pygame.draw.line(self.surface,color_grid,(300,y),(w,y))

    #### display title
    def display_score(self):
        self.myScore.set("SCORE :"+" "+str(self.score))
        self.surface.blit(self.myScore.image,(14,14))

    #### display time   
    def display_time(self):
        self.myTime.set("TIME:" +" "+ str(self.time_down))
        self.surface.blit(self.myTime.image,(215,14))

    ###$ time left
    def time_left(self,segundos):
            if self.aux==segundos:
                self.aux+=1
                self.time_down-=1
                
    #### display characters
    def display_characters(self):
        self.xplayer.draw(self.surface)
        self.list_apple.draw(self.surface)

    #### play
    def play(self):

        #clear and painting
        self.surface.fill(backgroundcolor)
        self.display_grid()
        self.mySnake.walk()
        self.display_characters()
        self.display_score()
        self.display_time()

        ### collision
        iscolision =pygame.sprite.spritecollide(self.mySnake,self.list_apple,True)

        if(iscolision):
            self.score +=1
        
        if (self.time_down==0):
            raise "Game over"

    #### game over
    def show_game_over(self):
        self.pause=False
        self.surface.fill(DARK)

        self.myTextgo=Texto(60)
        self.myTextmsg=Texto(30)

        self.myTextgo.set("GAME OVER!")

        gowhith =self.myTextgo.image.get_width()/2
        goheight=self.myTextgo.image.get_height()/2
        
        self.myTextmsg.set("PRESS SCAPE TO <<EXIT>>")

        msgwith =self.myTextmsg.image.get_width()/2
        msgheight  =self.myTextmsg.image.get_height()/2

        
        self.surface.blit(self.myTextgo.image,( (screen_width/2)- gowhith,(screen_height/2)-goheight))
        self.surface.blit(self.myTextmsg.image,( (screen_width/2)- msgwith,(screen_height/2)+goheight))

    #### run game
    def run(self):

        running =True
        self.pause =True

        # STARTING MAIN LOOP
        while running:

            current_time=pygame.time.get_ticks()
            seconds=int(current_time/1000)

            #### get list events
            for event in pygame.event.get():

                if event.type==KEYDOWN:

                    if event.key==K_ESCAPE:
                        running=False
                        self.finish()

                    #### moventes by key left top up down
                    if  self.pause:
                        if event.key==K_UP:
                            self.mySnake.move_up()
                        if event.key==K_DOWN:
                            self.mySnake.move_down()
                        if event.key==K_LEFT:
                            self.mySnake.move_left()
                        if event.key==K_RIGHT:
                            self.mySnake.move_right()
                    
                elif event.type==QUIT:
                    running=False
                    self.finish()
            
            try :

                if self.pause:
                    ### iniciar play
                    self.play()

                self.time_left(seconds) 

            except Exception as e:
                self.show_game_over()
                #pygame.display.flip()

            #### This will refresh our screen 
            pygame.display.flip()
            #### This will delay the game so it doesn't run too quickly
            self.clock.tick(SPEED)            
            
       
#### Main process
if __name__=="__main__":
    mygame = Game()
    mygame.run()
  

