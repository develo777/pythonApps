import pygame
from pygame.locals import *
import sys
import random

###color
WHITE=(250,250,250)
BLACK=(0,0,0)
RED=(255,0,0)
XX=(255,255,0)


size= width , height = 600,400

class box(pygame.sprite.Sprite):

    def __init__(self,image_x,pos_x,pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_x)
        #self.image = pygame.Surface((20,20))
        #self.image.fill(color_box)
        self.rect =self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
       
    

def main():
    #### Inicializar screen
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Basic Pygame program')

    ####  Fill background
    background=pygame.Surface(screen.get_size())
    background=background.convert()
    background.fill(WHITE)

    #### Display some text
    font=pygame.font.Font(None,36)
    text=font.render("Hello there",1,(10,10,10))
    textpos=text.get_rect()
    textpos.centerx =background.get_rect().centerx
    background.blit(text,textpos)
    
    ####This will be a list that will contain all the sprites we intend to use in our game.
    block_list = pygame.sprite.Group()

    all_sprites_list = pygame.sprite.Group()

    
    for x in range(1,15,1):
        ##### display box
        for y in range(1,20,1):
            mybox = box('images/box.jpg',300+x*20,20*y)
        # Add the car to the list of objects
            block_list.add(mybox)

    myplayer = box('images/snake.jpg',100,100)
    #all_sprites_list.add(myplayer)
    xmyplayer =pygame.sprite.RenderPlain(myplayer)
    xmyplayer.x=100
    xmyplayer.y=100

    score=0

    flag=True

    while  flag:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
                flag=False
            elif event.type ==KEYDOWN:
                if event.key ==K_UP:
                    pass
                    #mybox.moveup()
                if event.key ==K_DOWN:
                    pass
                    #mybox.movedown()
                if event.key ==K_RIGHT:
                    pass
                    #for myplayerx in all_sprites_list:
                        #myplayerx.rect.x+=10
                    myplayer.rect.x+=10

            elif event.type ==KEYUP:
                if event.key == K_UP or event.key == K_DOWN:
                    pass
                    #mybox.movepos=[0,0]
                    #mybox.state="still"
        
        #pos =pygame.mouse.get_pos()
        #print(pos)
        #myplayer.rect.x=pos[0]
        #myplayer.rect.y=pos[1]

        isColision = pygame.sprite.spritecollide(myplayer,block_list,True)
        

        if len(isColision)>0:
            score +=len(isColision)
            print(score)

        #screen.fill(BLACK)
        screen.blit(background,(0,0))
        #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
        block_list.draw(screen)
        xmyplayer.draw(screen)
        #myplayer.draw(screen)
        #all_sprites_list.draw(screen)
        ## refresca screen
        pygame.display.flip()


if __name__=='__main__':
    main()
    
