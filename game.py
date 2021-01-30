import time
import pygame
from pygame.locals import *


def draw_ball():
    mwindow.fill((200,200,200)) #borramos y pintamos 
    mwindow.blit(ball,(ball_x,ball_y))
    pygame.display.flip() 

class Game:
    def __init__(self):
        pass
    

if __name__=="__main__":
    pygame.init()
    
    #### Create a canvas on which to display everything ####
    mwindow=pygame.display.set_mode((500,500))
    #### color ####
    mwindow.fill((200,200,200))

    ball=pygame.image.load("intro_ball.gif").convert() #cargar imagen

    ball_x=2
    ball_y=2

    mwindow.blit(ball,(ball_x,ball_y))

    pygame.display.flip()
    
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
