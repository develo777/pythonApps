import time
import pygame
from pygame.locals import *

class Snake:

    def __init__(self,parent_screen):
        self.parent_screen=parent_screen
        self.ball=pygame.image.load("intro_ball.gif").convert() #cargar imagen
        self._x=2
        self._y=2
    
    def draw(self):
        self.mwindow.fill((200,200,200)) #borramos y pintamos 
        self.parent_screen.blit(self.ball,(self._x,self._y))
        pygame.display.flip() 
        
        
class Game:
    def __init__(self):
        pygame.init()
        #### Create a canvas on which to display everything ####
        self.mwindow=pygame.display.set_mode((500,500))
        #### color ####
        self.mwindow.fill((200,200,200))

        self.Snake=Snake(self.mwindow)
        self.Snake.draw()

    def run(self):
        running =True
        while running:
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        running=False
                    if event.key==K_UP:
                        ball_y-=10
                        draw_ball()
                    if event.key==K_DOWN:
                        ball_y+=10
                        draw_ball()
                    if event.key==K_LEFT:
                        ball_x-=10
                        draw_ball()
                    if event.key==K_RIGHT:
                        ball_x+=10
                        draw_ball()
                    
                elif event.type==QUIT:
                    running=False


if __name__=="__main__":
    mygame = Game()
    mygame.run()
  

