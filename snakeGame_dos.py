import time
import sys
import pygame
from pygame.locals import *
import time


### color
GREEN = (0, 255, 0)
DARK_GRAY = (32, 32, 32)

### speep
SPEED = 10


SIZE=30

###parameters
backgroundcolor = (DARK_GRAY)
screen_width = 600
screen_height = 400


class Heart:
    def __init__(self,parent_screen):
        pass
      
    def draw(self):
        pass
      
class Snake:

    #### constructor
    def __init__(self,parent_screen,length):
        pass

    def draw(self):
        pass
       
    def walk(self):
        pass

    #### move left 
    def move_left(self):
        pass
    
    #### move right 
    def move_right(self):
        pass
      
    #### move up 
    def move_up(self):
        pass
     
    #### move down 
    def move_down(self):
        pass
       
       
class Game:

    #### constructor
    def __init__(self):
        win = pygame.display.set_mode(screen_width,screen_height)
        pass
       
    #### finish window                                                                                                                          
    def finish(self):
        pass
      
    ### display title
    def display_title(self):
        pass
       
    #### play
    def play(self):
        pass

    #### run game
    def run(self):

        running =True

        while running:
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

            
#### Main process
if __name__=="__main__":
    mygame = Game()
    mygame.run()
  

