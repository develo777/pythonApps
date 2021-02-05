import time
import sys
import pygame
from pygame.locals import *
import time
import random

#### Color
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARK = (0, 0, 0)
DARK_GRAY = (32, 32, 32)
WHITE = (255, 255, 255)
#### speep 10 FPS
SPEED = 20
DELAY=60
SIZE=20

####  CONFIGURATIONS
title_window="My first Game!"

### TITLE
title_game="Wherever you, go GOD is with you!"
title_size=40
title_x=45 
title_y=180
title_color=WHITE

#### COLOR GRID
color_grid=GREEN

### CANVAS WINDOWS
backgroundcolor = (DARK_GRAY)
screen_width = 600
screen_height = 400


class apple(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image=pygame.image.load("Apple.png").convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=pos_x
        self.rect.y=pos_y

class Snake(pygame.sprite.Sprite):
    #### constructor
    def __init__(self,length):
        super().__init__()
        #### load character
        self.length=length 
        self.image=pygame.image.load("snake.jpg").convert() 
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

class Game:

    #### constructor
    def __init__(self):
        #### initialize all imported pygame modules ####
        pygame.init()

        #### create a window ####
        self.surface=pygame.display.set_mode((screen_width,screen_height))

        #### title
        pygame.display.set_caption(title_window)

        #### creating a clock object
        self.clock = pygame.time.Clock()
        
        #### grupo apples
        self.list_apple =pygame.sprite.Group()

        #### create a instance o objet snake
        self.mySnake=Snake(2)
        self.xplayer = pygame.sprite.RenderPlain(self.mySnake)

        #### create appless
        for x in range(1,15,1):
            for y in range(1,20,1):
                myapples=apple(300+x*20,20*y)
                self.list_apple.add(myapples)

    #### finish window                                                                                                                          
    def finish(self):
        pygame.quit()
        sys.exit()

    #### display grid
    def display_workarea(self):
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
    def display_title(self):
        self.myFont = pygame.font.Font("Myrlissa.otf",title_size)
        self.myText = self.myFont.render(title_game,1,title_color)
        self.surface.blit(self.myText,(title_x,title_y))

    #### display characters
    def display_characters(self):
        self.xplayer.draw(self.surface)
        self.list_apple.draw(self.surface)

    #### play
    def play(self):
      
        #clear and painting
        self.surface.fill(backgroundcolor)
        self.display_workarea()
        self.display_title()
        self.mySnake.walk()
        self.display_characters()

        ### collision
        iscolision =pygame.sprite.spritecollide(self.mySnake,self.list_apple,True)
    

    #### run game
    def run(self):

        running =True

        # STARTING MAIN LOOP
        while running:

            #### This will delay the game so it doesn't run too quickly
            pygame.time.delay(DELAY)

            #### get list events
            for event in pygame.event.get():

                if event.type==KEYDOWN:

                    if event.key==K_ESCAPE:
                        running=False
                        self.finish()

                    #### moventes by key left top up down
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
            
            #### Will ensure our game runs at 10 FPS
            self.clock.tick(SPEED)

            self.play()
            
            #### This will refresh our screen 
            pygame.display.flip()
            
       
#### Main process
if __name__=="__main__":
    mygame = Game()
    mygame.run()
  

