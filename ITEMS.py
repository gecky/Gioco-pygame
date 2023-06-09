import pygame
import time


class diamante:
    def __init__(self,screen,pos):
        self.speed = 1  # Velocità di caduta iniziale
        self.acceleration = 0.1  # Accelerazione di caduta
        self.image=pygame.image.load('cananap.png')
        self.image=pygame.transform.scale(self.image,(70,70))
        self.screen=screen
        self.rect = pygame.Rect(pos[0],pos[1],70,70)
        punti=5

    def rettangolo(self):
        return self.rect

    def draw(self):
        self.screen.blit(self.image, self.rect)

class viola:
    def __init__(self,screen,pos):
        self.speed = 1  # Velocità di caduta iniziale
        self.acceleration = 0.1  # Accelerazione di caduta
        self.image=pygame.image.load('viola.png')
        self.image=pygame.transform.scale(self.image,(80,80))
        self.screen=screen
        self.rect = pygame.Rect(pos[0],pos[1],80,80)
        punti=4

    def rettangolo(self):
        return self.rect

    def draw(self):
        self.screen.blit(self.image, self.rect)

class smeraldo:
    def __init__(self,screen,pos):
        self.speed = 1  # Velocità di caduta iniziale
        self.acceleration = 0.1  # Accelerazione di caduta
        self.image=pygame.image.load('smeraldo.png')
        self.image=pygame.transform.scale(self.image,(80,80))
        self.screen=screen
        self.rect = pygame.Rect(pos[0],pos[1],80,80)
        punti=3

    def rettangolo(self):
        return self.rect

    def draw(self):
        self.screen.blit(self.image, self.rect)

class zaffiro:
    def __init__(self,screen,pos):
        self.speed = 1  # Velocità di caduta iniziale
        self.acceleration = 0.1  # Accelerazione di caduta
        self.image=pygame.image.load('zaffiro.png')
        self.image=pygame.transform.scale(self.image,(80,80))
        self.screen=screen
        self.rect = pygame.Rect(pos[0],pos[1],80,80)
        punti=2

    def rettangolo(self):
        return self.rect

    def draw(self):
        self.screen.blit(self.image, self.rect)


class topazio:
    def __init__(self,screen,pos):
        self.speed = 1  # Velocità di caduta iniziale
        self.acceleration = 0.1  # Accelerazione di caduta
        self.image=pygame.image.load('topazio.png')
        self.image=pygame.transform.scale(self.image,(100,100))
        self.screen=screen
        self.rect = pygame.Rect(pos[0],pos[1],100,100)
        punti=1

    def rettangolo(self):
        return self.rect

    def draw(self):
        self.screen.blit(self.image, self.rect)




class bombanucleare:
    def __init__(self,screen,pos):
        self.speed = 1  # Velocità di caduta iniziale
        self.acceleration = 0.1  # Accelerazione di caduta
        self.image=pygame.image.load('tormy.png')
        self.image=pygame.transform.scale(self.image,(40,80))
        self.screen=screen
        self.rect = pygame.Rect(pos[0],pos[1],25,50)
        vite=-2

    def rettangolo(self):
        return self.rect

    def draw(self):
        self.screen.blit(self.image, self.rect)
    def esplosione(self):
        self.image=pygame.image.load('esplosione.png')
        self.image=pygame.transform.scale(self.image,(40,80))
    
    def esplosioneinversa(self):
        self.image=pygame.image.load('bomba.png')
        self.image=pygame.transform.scale(self.image,(120,140))

class bomba:
    def __init__(self,screen,pos):
        self.speed = 1  # Velocità di caduta iniziale
        self.acceleration = 0.1  # Accelerazione di caduta
        self.image=pygame.image.load('bomba.png')
        self.image=pygame.transform.scale(self.image,(120,140))
        self.screen=screen
        self.rect = pygame.Rect(pos[0],pos[1],120,160)
        vite=-1

    def rettangolo(self):
        return self.rect

    def draw(self):
        self.screen.blit(self.image, self.rect)
    
    def esplosione(self):
        self.image=pygame.image.load('esplosione.png')
        self.image=pygame.transform.scale(self.image,(120,140))
    
    def esplosioneinversa(self):
        self.image=pygame.image.load('bomba.png')
        self.image=pygame.transform.scale(self.image,(120,140))

class info:
    def __init__(self,screen,pos):
        self.image=pygame.image.load('info.png')
        self.image=pygame.transform.scale(self.image,(50,50))
        self.screen=screen
        self.rect = pygame.Rect(pos[0],pos[1],50,50)

    def rettangolo(self):
        return self.rect

    def draw(self):
        self.screen.blit(self.image, self.rect)

class rosso:
    def __init__(self,screen,pos):
        self.image=pygame.image.load('bottonerosso.png')
        self.image=pygame.transform.scale(self.image,(250,250))
        self.screen=screen
        self.rect = pygame.Rect(pos[0],pos[1],250,250)

    def rettangolo(self):
        return self.rect

    def draw(self):
        self.screen.blit(self.image, self.rect)

class rossopremuto:
    def __init__(self,screen,pos):
        self.image=pygame.image.load('bottonerossopremuto.png')
        self.image=pygame.transform.scale(self.image,(240,250))
        self.screen=screen
        self.rect = pygame.Rect(pos[0],pos[1],240,250)

    def rettangolo(self):
        return self.rect

    def draw(self):
        self.screen.blit(self.image, self.rect)

class gameover:
    def __init__(self,screen,pos):
            self.image=pygame.image.load('gameover.png')
            self.image=pygame.transform.scale(self.image,(240,280))
            self.screen=screen
            self.rect = pygame.Rect(pos[0],pos[1],240,280)

    def rettangolo(self):
        return self.rect

    def draw(self):
        self.screen.blit(self.image, self.rect)

class play:
    def __init__(self,screen,pos):
            self.image=pygame.image.load('play.png')
            self.image=pygame.transform.scale(self.image,(110,110))
            self.screen=screen
            self.rect = pygame.Rect(pos[0],pos[1],100,100)

    def rettangolo(self):
        return self.rect

    def draw(self):
        self.screen.blit(self.image, self.rect)
class playdown:
    def __init__(self,screen,pos):
            self.image=pygame.image.load('playdown.png')
            self.image=pygame.transform.scale(self.image,(110,115))
            self.screen=screen
            self.rect = pygame.Rect(pos[0],pos[1],100,100)

    def rettangolo(self):
        return self.rect

    def draw(self):
        self.screen.blit(self.image, self.rect)


class orologio:
    def __init__(self,screen,pos):
        self.screen=screen
        self.rect = pygame.Rect(pos[0],pos[1],100,100)
    def rettangolo(self):
        self.screen.blit



class topazioinfo:
    def __init__(self,screen,pos):
        self.image=pygame.image.load('topazio.png')
        self.image=pygame.transform.scale(self.image,(60,60))
        self.screen=screen
        self.rect = pygame.Rect(pos[0],pos[1],60,60)
        punti=1

    def rettangolo(self):
        return self.rect

    def draw(self):
        self.screen.blit(self.image, self.rect)

class diamanteinfo:
    def __init__(self,screen,pos):
        self.image=pygame.image.load('cananap.png')
        self.image=pygame.transform.scale(self.image,(60,60))
        self.screen=screen
        self.rect = pygame.Rect(pos[0],pos[1],60,60)
        punti=1

    def rettangolo(self):
        return self.rect

    def draw(self):
        self.screen.blit(self.image, self.rect)

class smeraldoinfo:
    def __init__(self,screen,pos):
        self.image=pygame.image.load('smeraldo.png')
        self.image=pygame.transform.scale(self.image,(60,60))
        self.screen=screen
        self.rect = pygame.Rect(pos[0],pos[1],60,60)
        punti=1

    def rettangolo(self):
        return self.rect

    def draw(self):
        self.screen.blit(self.image, self.rect)

class violainfo:
    def __init__(self,screen,pos):
        self.image=pygame.image.load('viola.png')
        self.image=pygame.transform.scale(self.image,(60,60))
        self.screen=screen
        self.rect = pygame.Rect(pos[0],pos[1],60,60)
        punti=1

    def rettangolo(self):
        return self.rect

    def draw(self):
        self.screen.blit(self.image, self.rect)

class zaffiroinfo:
    def __init__(self,screen,pos):
        self.image=pygame.image.load('zaffiro.png')
        self.image=pygame.transform.scale(self.image,(60,60))
        self.screen=screen
        self.rect = pygame.Rect(pos[0],pos[1],60,60)
        punti=1

    def rettangolo(self):
        return self.rect

    def draw(self):
        self.screen.blit(self.image, self.rect)

class bombainfo:
    def __init__(self,screen,pos):
        self.image=pygame.image.load('bomba.png')
        self.image=pygame.transform.scale(self.image,(60,60))
        self.screen=screen
        self.rect = pygame.Rect(pos[0],pos[1],60,60)
        punti=1

    def rettangolo(self):
        return self.rect

    def draw(self):
        self.screen.blit(self.image, self.rect)

class nukeinfo:
    def __init__(self,screen,pos):
        self.image=pygame.image.load('tormy.png')
        self.image=pygame.transform.scale(self.image,(60,60))
        self.screen=screen
        self.rect = pygame.Rect(pos[0],pos[1],60,60)
        punti=1

    def rettangolo(self):
        return self.rect

    def draw(self):
        self.screen.blit(self.image, self.rect)

class Exit:
    def __init__(self,screen,pos):
        self.image=pygame.image.load('x.png')
        self.image=pygame.transform.scale(self.image,(40,40))
        self.screen=screen
        self.rect = pygame.Rect(pos[0],pos[1],60,60)
        punti=1

    def rettangolo(self):
        return self.rect

    def draw(self):
        self.screen.blit(self.image, self.rect)

class Vita:
    def __init__(self, screen, pos) -> None:
        self.screen = screen
        self.image = pygame.image.load('vita.png')
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = pygame.Rect((pos[0], pos[1]), (30,30))
        
    def rettangolo(self):
        return self.rect()

    def draw(self):
        self.screen.blit(self.image, self.rect)
        
