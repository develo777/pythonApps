import time
import sys
import pygame
from pygame.locals import *
import time
import random

#### color
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
title_game="Wherever you go GOD is with you!"
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

class corazon(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image=pygame.image.load("images/Apple.png").convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=pos_x
        self.rect.y=pos_y
        

class Heart:
    def __init__(self,parent_screen):
        self.parent_screen=parent_screen
        self.heart=pygame.image.load("images/Apple.png").convert_alpha()
        self._x=300
        self._y=376
    
    def draw(self):
        self.parent_screen.blit(self.heart,(self._x,self._y))



class Snake:
    #### constructor
    def __init__(self,parent_screen,length):
        self.length=length
        self.parent_screen=parent_screen
        #### load character 
        self.snake=pygame.image.load("images/snake.jpg").convert() 
        self.direction ='down'
        self._x=[SIZE] * length
        self._y=[SIZE] * length
    #### draw
    def draw(self):

        for i in range(self.length):
            ### draw  snake on the window
            self.parent_screen.blit(self.snake,(self._x[i],self._y[i]))
        ### update screen
        pygame.display.flip() 
    #### walk
    def walk(self):

        for i in range(self.length-1,0,-1):
            self._x[i]=self._x[i-1]
            self._y[i]=self._y[i-1]

        if self.direction=='left' and self._x[0]>1 :
            self._x[0]-=SIZE
        if self.direction=='right' and self._x[0]< screen_width - SIZE:
            self._x[0]+=SIZE
        if self.direction=='up'   and self._y[0]>1 :
            self._y[0]-=SIZE
        if self.direction=='down'  and self._y[0]< screen_height-SIZE:
            self._y[0]+=SIZE

        self.draw()
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
        
        ### grupo
        self.list_corazones =pygame.sprite.Group()



        #### create a instance o objet snake
        self.Snake=Snake(self.surface,2)
        
        #### create a hearth
        self.myheart=Heart(self.surface)
        self.myheart.draw()

        ### create targets
        for i in range(7):
           mycorazon=corazon(random.randrange(0,screen_width),random.randrange(0,screen_height))
           self.list_corazones.add(mycorazon)

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
        self.myFont = pygame.font.Font("font/Myrlissa.otf",title_size)
        self.myText = self.myFont.render(title_game,1,title_color)
        self.surface.blit(self.myText,(title_x,title_y))

    #### display objetos
    def display_objetos(self):
        self.list_corazones.draw(self.surface)

    #### play
    def play(self):
      
        #clear and painting
        self.surface.fill(backgroundcolor)
        self.display_workarea()
        self.Snake.draw()
        self.Snake.walk()
       # self.myheart.draw()
        self.display_title()
        self.display_objetos()

        if self.is_collision(self.Snake._x[0],self.Snake._y[0],self.myheart._x,self.myheart._y):
            print("collision ocurred")
    
    ### collision
    def is_collision(self,snake_x1,snake_y1,x2,y2):
        if snake_x1>=x2 and snake_x1 <=x2+SIZE:
            if snake_y1>=y2 and snake_y1 <=y2+SIZE:
                return True
        else:
            return False

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
                        self.Snake.move_up()
                    if event.key==K_DOWN:
                        self.Snake.move_down()
                    if event.key==K_LEFT:
                        self.Snake.move_left()
                    if event.key==K_RIGHT:
                        self.Snake.move_right()
                    
                elif event.type==QUIT:
                    running=False
                    self.finish()
            
            #### Will ensure our game runs at 10 FPS
            self.clock.tick(SPEED)
            self.play()
            #time.sleep(.2)
            #### This will refresh our screen 
            pygame.display.flip()
            
       
#### Main process
if __name__=="__main__":
    mygame = Game()
    mygame.run()
  

