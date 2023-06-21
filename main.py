import pygame
import random
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

mha =pygame.transform.scale(pygame.image.load("mha.png"),(100,150))
mha_walk = pygame.transform.scale(pygame.image.load("mha_walk.png"),(100,150))
mha_punch = pygame.transform.scale(pygame.image.load("mha_punch.png"),(100,150))
ring = pygame.transform.scale(pygame.image.load("ring.jpg"),(800,600))

mt = pygame.transform.scale(pygame.image.load("mt.png"),(100,150))
mt_walk = pygame.transform.scale(pygame.image.load("mt_walk.png"),(100,150))
mt_punch = pygame.transform.scale(pygame.image.load("mt_punching.png"),(100,150))

class MuhammadAli:
    def __init__(self,x,y,stand , walk , punch):
        self.stand = stand
        self.walk = walk
        self.punch = punch
        self.now = stand
        self.now_rect = self.now.get_rect(center = (300,200))
        self.punching = False
        self.punching_force = 0

muhammadAli = MuhammadAli(100,100 , mha , mha_walk , mha_punch)

class Miketyson:
    def __init__(self,x,y,stand,walk,punch):
        self.stand = stand
        self.walk = walk
        self.now = walk
        self.now_rect =self.now.get_rect(center = (400,100))
        self.punch = punch
miketyson = Miketyson(375,175,mt,mt_walk,mt_punch)

def control_miketyson():
    mtPosition = miketyson.now_rect.center
    mhaPosition= muhammadAli.now_rect.center

    if mtPosition[1] < mhaPosition[1] :
        miketyson.now = miketyson.walk
        miketyson.now_rect.bottom += random.randint(0,1)

    if mtPosition[1] > mhaPosition[1] :
        miketyson.now = miketyson.walk
        miketyson.now_rect.bottom -= random.randint(0,1)
    
    if mtPosition[0] - mhaPosition[0] > 100 :
        miketyson.now = miketyson.walk
        miketyson.now_rect.left -= random.randint(0,1)
       
    if mtPosition[0] - mhaPosition[0] < 100 :
        miketyson.now = miketyson.walk
        miketyson.now_rect.left += random.randint(0,1)

    if abs(mtPosition[0] - mhaPosition[0] ) < 100 :
         miketyson.now = miketyson.punch


    


while True:
    pass
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if muhammadAli.punching == False:
                    muhammadAli.now = muhammadAli.punch
                    muhammadAli.punching_force = 20
                    muhammadAli.punching = True

    screen.fill("grey")
    screen.blit(ring,(0,0))
    screen.blit(muhammadAli.now,muhammadAli.now_rect)
    muhammadAli.now = muhammadAli.stand
    

    screen.blit(miketyson.now,miketyson.now_rect)
    miketyson.now = miketyson.stand

    if muhammadAli.punching_force <= 0 :
        muhammadAli.punching = False
    
    keys = pygame.key.get_pressed()

    if muhammadAli.punching:
        muhammadAli.now = muhammadAli.punch
        muhammadAli.punching_force -= 1

    else:
        if keys[pygame.K_w]:
            muhammadAli.now = muhammadAli.walk
            muhammadAli.now_rect.top-=1
        if keys[pygame.K_s]:
            muhammadAli.now = muhammadAli.walk
            muhammadAli.now_rect.top+=1
        if keys[pygame.K_a]:
            muhammadAli.now = muhammadAli.walk
            muhammadAli.now_rect.left-=1
        if keys[pygame.K_d]:
            muhammadAli.now = muhammadAli.walk
            muhammadAli.now_rect.left+=1
    

    control_miketyson()    

    pygame.display.flip()
    clock.tick(60)