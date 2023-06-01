# Gioco-pygame
import pygame, sys, os
from pygame.locals import *
from ITEMS import diamante,smeraldo,viola,topazio,zaffiro,bomba,rosso,rossopremuto,gameover,bombanucleare,play,playdown
from random import randint
from os.path import join
import time


pygame.init()
pygame.font.init()

bordeaux=(168,10,10)

record=0

sec=0

t0=None

window_size = (600, 800)
screenrect=pygame.Rect((0,0),(600,800))
screen = pygame.display.set_mode(window_size)
s=pygame.image.load('sfondo.jpg')
pygame.transform.scale(s,(600,800))
pygame.display.set_caption('ERGIOCOCHECADE')

sound1 = pygame.mixer.Sound('message-incoming-132126.mp3')
sound2 = pygame.mixer.Sound('negative_beeps-6008.mp3')
sound3 = pygame.mixer.Sound('mixkit-falling-game-over-1942.wav')

gioco=0
points=0
damage=5
speed=2
acc=0.0050),randint(-600,-150)))
nuke=bombanucleare(screen,(randint(50,550),randint(-600,-150)))


font1 = pygame.font.SysFont('Times New Roman', 24)
font2 = pygame.font.SysFont('arial', 200)
font3 = pygame.font.SysFont('Times New Roman', 50)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        sec+=0.1666666666666667
    
        posmouse=pygame.mouse.get_pos()


        if gioco==0:
            screen.fill('BLACK')
            r.draw()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
                    if rr.collidepoint(posmouse):
                        rp.draw()
                        gioco=1
        if gioco==1:
            if  event.type == MOUSEBUTTONUP and event.button==1:
                gioco=2
                t=False
        pygame.display.flip()
        clock.tick(60)

r=rosso(screen,(150,300))
rr=r.rettangolo()
rp=rossopremuto(screen,(163,300))
rpr=rp.rettangolo()

diamante1=diamante(screen,(randint(50,550),randint(-600,-150)))
topazio1=topazio(screen,(randint(50,550),randint(-600,-150)))
viola1=viola(screen,(randint(50,550),randint(-600,-150)))
zaffiro1=zaffiro(screen,(randint(50,550),randint(-600,-150)))
smeraldo1=smeraldo(screen,(randint(50,550),randint(-600,-150)))


bomba1=bomba(screen,(randint(50,550),randint(-600,-150)))
bomba2=bomba(screen,(randint(50,55

        
        if gioco==2:
            
            

            screen.blit(s,screenrect)

            bomba1.esplosioneinversa()
            bomba2.esplosioneinversa()

            
            diamante1.draw()
            topazio1.draw()
            viola1.draw()
            zaffiro1.draw()
            smeraldo1.draw()
            bomba1.draw()
            bomba2.draw()
            nuke.draw()

            q1=diamante1.rettangolo()  
            q2=viola1.rettangolo()  
            q3=smeraldo1.rettangolo()  
            q4=zaffiro1.rettangolo()
            q5=topazio1.rettangolo()
            b1=bomba1.rettangolo()
            b2=bomba2.rettangolo()
            n1=nuke.rettangolo()
            q1.centery+=speed
            if q1.centery>screen.get_height():
                damage-=1
                q1.centery=-10
                q1.centerx=randint(50,550)
                punti=font1.render(f'{points}',True,'WHITE')

            q2.centery+=speed
            if q2.centery>screen.get_height():
                damage-=1
                q2.centery=-10
                q2.centerx=randint(50,550)
            q3.centery+=speed
            if q3.centery>screen.get_height():
                damage-=1
                q3.centery=-10
                q3.centerx=randint(50,550)
            q4.centery+=speed
            if q4.centery>screen.get_height():
                damage-=1
                q4.centery=-10
                q4.centerx=randint(50,550)
            q5.centery+=speed
            if q5.centery>screen.get_height():
                damage-=1
                q5.centery=-10
                q5.centerx=randint(50,550)
            b1.centery+=speed
            if b1.centery>screen.get_height():
                b1.centery=-10
                b1.centerx=randint(50,550)
            b2.centery+=speed
            if b2.centery>screen.get_height():
                b2.centery=-10
                b2.centerx=randint(50,550)
            n1.centery+=speed
            if n1.centery>screen.get_height():
                n1.centery=-10
                n1.centerx=randint(50,550)

            speed+=acc
            if speed>=6:
                speed=6
                scrittaspeed=font1.render(f'SPEED: MAX',True,'WHITE')
                screen.blit(scrittaspeed,(0,100))
            else:
                scrittaspeed=font1.render(f'SPEED: {round(speed,2)}',True,'WHITE')
                screen.blit(scrittaspeed,(0,100))


            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if q1.collidepoint(posmouse):
                    sound1.play()
                    points+=5
                    q1.centery=randint(-200,0)
                    q1.centerx=randint(50,550)
                    xy=posmouse
                    s1=font3.render(f'+5',True,('WHITE'))
                    t0=sec
                    screen.blit(s1,(xy))
                    c1=1
                if q2.collidepoint(posmouse):
                    sound1.play()
                    points+=4
                    q2.centery=randint(-200,0)
                    q2.centerx=randint(50,550)
                    xy=posmouse
                    s2=font3.render(f'+4',True,(224,0,255,255))
                    t0=sec
                    screen.blit(s1,(xy))
                    c1=1
                if q3.collidepoint(posmouse):
                    sound1.play()
                    points+=3
                    q3.centery=randint(-200,0)
                    q3.centerx=randint(50,550)
                    xy=posmouse
                    s2=font3.render(f'+5',True,(224,0,255,25))
                    t0=sec
                    screen.blit(s1,(xy))
                    c1=1
                if q4.collidepoint(posmouse):
                    sound1.play()
                    points+=2
                    q4.centery=randint(-200,0)
                    q4.centerx=randint(50,550)
                if q5.collidepoint(posmouse):
                    sound1.play()
                    points+=1
                    q5.centery=randint(-200,0)
                    q5.centerx=randint(50,550)
                if b1.collidepoint(posmouse):
                    bomba1.esplosione()
                    sound2.play()
                    b1.centery=randint(-200,0)
                    b1.centerx=randint(50,550)
                    damage-=1
                if b2.collidepoint(posmouse):
                    bomba1.esplosione()
                    sound2.play()
                    b2.centery=randint(-200,0)
                    b2.centerx=randint(50,550)
                    damage-=1
                if n1.collidepoint(posmouse):
                    sound2.play()
                    n1.centery=randint(-200,0)
                    n1.centerx=randint(50,550)
                    damage-=3
            if t0!=None:
                if sec-t0==1 and c1==1:
                    screen.blit(s,screenrect)
                    c=0


            punteggio=font1.render(f'PUNTEGGIO:  {points}',True,'WHITE')
            danni=font1.render(f'VITE:  {damage}',True,'WHITE')
            screen.blit(punteggio,(0,0))
            screen.blit(danni,(0,50))
        if damage<=0:
            screen.fill('BLACK')
            gameover1=gameover(screen,(170,170))
            gameover1.draw()
            sound3.play()
            play1=play(screen,(240,600))
            playdown1=playdown(screen,(240,590))
            playrect=play1.rettangolo()
            play1.draw()
            if points>record:
                record=points
            scrittarecord=font1.render(f' record : {record}',True, 'WHITE')

            punti=font1.render(f'{points}',True,'WHITE')
            screen.blit(punti,(285,500))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
                if playrect.collidepoint(posmouse):
                    playdown1.draw()
                    gioco=4
            if gioco==4:
                if  event.type == MOUSEBUTTONUP and event.button==1:
                    gioco=0
                    damage=5
                    points=0
                    diamante1=diamante(screen,(randint(50,550),randint(-600,-150)))
                    topazio1=topazio(screen,(randint(50,550),randint(-600,-150)))
                    viola1=viola(screen,(randint(50,550),randint(-600,-150)))
                    zaffiro1=zaffiro(screen,(randint(50,550),randint(-600,-150)))
                    smeraldo1=smeraldo(screen,(randint(50,550),randint(-600,-150)))


                    bomba1=bomba(screen,(randint(50,550),randint(-600,-150)))
                    bomba2=bomba(screen,(randint(50,550),randint(-600,-150)))
                    nuke=bombanucleare(screen,(randint(50,550),randint(-600,-150)))
                    speed=4

                    
            pygame.display.flip()
            clock.tick(60)
