import time
import sys
import pygame
from pygame.locals import *
import time

class Snake:
    #### constructor
    def __init__(self,parent_screen):
        self.parent_screen=parent_screen
        ####load character ball
        self.ball=pygame.image.load("Apple.png").convert() 
        self._x=2
        self._y=2
    
    def draw(self):
        #borramos y pintamos 
        self.parent_screen.fill((0,0,0)) 
        ### dibujar el snake en la window
        self.parent_screen.blit(self.ball,(self._x,self._y))
        ### update screen
        pygame.display.flip() 
    

    #### move left 
    def move_left(self):
        self._x-=10
        self.draw()
    #### move right 
    def move_right(self):
        self._x+=10
        self.draw()
    #### move up 
    def move_up(self):
        self._y-=10
        self.draw()    
    #### move down 
    def move_down(self):
        self._y+=10
        self.draw()  
        
class Game:

    #### constructor
    def __init__(self):
        #### initialize all imported pygame modules ####
        pygame.init()
        #### Create a window ####
        self.mwindow=pygame.display.set_mode((500,500))
        #### title
        pygame.display.set_caption("my first Game!")
        #### background-color ####
        self.mwindow.fill((0,0,0))

        #### create a instance o objet (snake)
        self.Snake=Snake(self.mwindow)
        self.Snake.draw()

    #### finish window                                                                                                                          
    def finish(self):
        pygame.quit()
        sys.exit()


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



# Main process
#------------------------
if __name__=="__main__":
    mygame = Game()
    mygame.run()
  

