import pygame, sys, os
from pygame.locals import *
from ITEMS import diamante,smeraldo,viola,topazio,zaffiro,bomba,rosso,rossopremuto,gameover,bombanucleare,play,playdown,info,diamanteinfo,smeraldoinfo,bombainfo,zaffiroinfo,violainfo,topazioinfo,nukeinfo,Exit,Vita
from random import randint
from os.path import join
import time


pygame.init()
pygame.font.init()

window_size = (600, 800)
screenrect=pygame.Rect((0,0),(600,800))
screen = pygame.display.set_mode(window_size)
s=pygame.image.load('sfondo.jpg')
pygame.transform.scale(s,(600,800))
pygame.display.set_caption('ERGIOCOCHECADE')

def reset():
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


    


bordeaux=(252, 28, 28)

record=0

sec=0

esplosione=pygame.image.load('esplosione.png')
nesplosione=pygame.image.load('nesplosione.png')
nesplosione=pygame.transform.scale(nesplosione,(150,150))


t1=None
t2=None
t3=None
t4=None
t5=None
tb1=None
tb2=None
tn1=None

vita1=Vita(screen,(35,20))
vita2=Vita(screen,(70,20))
vita3=Vita(screen,(105,20))
vita4=Vita(screen,(140,20))
vita5=Vita(screen,(175,20))
vite=[vita1,vita2,vita3,vita4,vita5]




sound1 = pygame.mixer.Sound('message-incoming-132126.mp3')
sound2 = pygame.mixer.Sound('negative_beeps-6008.mp3')
sound3 = pygame.mixer.Sound('mixkit-falling-game-over-1942.wav')

gioco=0
points=0
damage=5
speed=2
acc=0.001

r=rosso(screen,(150,300))
rr=r.rettangolo()
rp=rossopremuto(screen,(163,300))
rpr=rp.rettangolo()
i=info(screen,(500,700))
ri=i.rettangolo()
x=Exit(screen,(530,50))
rx=x.rettangolo()

diamante1=diamante(screen,(randint(50,550),randint(-600,-150)))
topazio1=topazio(screen,(randint(50,550),randint(-600,-150)))
viola1=viola(screen,(randint(50,550),randint(-600,-150)))
zaffiro1=zaffiro(screen,(randint(50,550),randint(-600,-150)))
smeraldo1=smeraldo(screen,(randint(50,550),randint(-600,-150)))


            # titolo=font3.render(f' ISTRUZIONI:',True,'BLACK')

bomba1=bomba(screen,(randint(50,550),randint(-600,-150)))
bomba2=bomba(screen,(randint(50,550),randint(-600,-150)))
nuke=bombanucleare(screen,(randint(50,550),randint(-600,-150)))


font1 = pygame.font.SysFont('freesansbold.ttf', 50)
font2 = pygame.font.SysFont('freesansbold.ttf', 200)
font3 = pygame.font.SysFont('freesansbold.ttf', 80)
font4 = pygame.font.SysFont('freesansbold.ttf', 30)

scrittadiamante=font4.render(f'Da +5 punti se colpito, se cade perdi una vita',True,'black')
scrittaviola=font4.render(f'Da +4 punti se colpito, se cade perdi una vita',True,'black')
scrittasmeraldo=font4.render(f'Da +5 punti se colpito, se cade perdi una vita',True,'black')
scrittazaffiro=font4.render(f'Da +5 punti se colpito, se cade perdi una vita',True,'black')
scrittatopazio=font4.render(f'Da +5 punti se colpito, se cade perdi una vita',True,'black')
scrittabomba=font4.render(f'Toglie -1 vita se colpita',True,'black')
scrittanuke=font4.render(f'Toglie -3 vite se colpita',True,'black')


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        sec+=(1)
    
        posmouse=pygame.mouse.get_pos()


        if gioco==0:
            screen.fill('BLACK')
            scritta=font1.render(f'SO CHE VUOI CLICCARLO',True,'white')
            screen.blit(scritta,(85,150))
            r.draw()
            i.draw()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
                if rr.collidepoint(posmouse):
                    rp.draw()
                    gioco=1
            if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
                if ri.collidepoint(posmouse):
                    gioco=5
        
        if gioco==5:
            screen.fill('white')
            titolo=font3.render(f' ISTRUZIONI:',True,'BLACK')
            screen.blit(titolo,(110,50))
            diamantei=diamanteinfo(screen,(50,150))
            violai=violainfo(screen,(50,220))
            smeraldoi=smeraldoinfo(screen,(50,290))
            zaffiroi=zaffiroinfo(screen,(50,360))
            topazioi=topazioinfo(screen,(50,430))
            bombai=bombainfo(screen,(50,500))
            nukei=nukeinfo(screen,(50,570))
            diamantei.draw()
            topazioi.draw()
            violai.draw()
            zaffiroi.draw()
            smeraldoi.draw()
            bombai.draw()
            nukei.draw()
            x.draw()
            screen.blit(scrittadiamante,(120,170))
            screen.blit(scrittaviola,(120,240))
            screen.blit(scrittasmeraldo,(120,310))
            screen.blit(scrittazaffiro,(120,380))
            screen.blit(scrittatopazio,(120,450))
            screen.blit(scrittabomba,(120,520))
            screen.blit(scrittanuke,(120,590))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
                if rx.collidepoint(posmouse):
                    gioco=0



            

        if gioco==1:
            if  event.type == MOUSEBUTTONUP and event.button==1:
                gioco=2
                t=False
        pygame.display.flip()
        clock.tick(60)


        
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
            if speed>=5:
                speed=5
                scrittaspeed=font1.render(f'SPEED: MAX',True,'WHITE')
                screen.blit(scrittaspeed,(35,110))


            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if q1.collidepoint(posmouse):
                    sound1.play()
                    points+=5
                    q1.centery=randint(-200,0)
                    q1.centerx=randint(50,550)
                    xy=posmouse
                    s1=font3.render(f'+5',True,('WHITE'))
                    t1=sec
                    screen.blit(s1,(xy))
                    c1=1
                if q2.collidepoint(posmouse):
                    sound1.play()
                    points+=4
                    q2.centery=randint(-200,0)
                    q2.centerx=randint(50,550)
                    xy=posmouse
                    s2=font3.render(f'+4',True,(223, 0, 255))
                    t2=sec
                    screen.blit(s2,(xy))
                    c2=1
                if q3.collidepoint(posmouse):
                    sound1.play()
                    points+=3
                    q3.centery=randint(-200,0)
                    q3.centerx=randint(50,550)
                    xy=posmouse
                    s3=font3.render(f'+3',True,(11, 212, 9))
                    t3=sec
                    screen.blit(s3,(xy))
                    c3=1
                if q4.collidepoint(posmouse):
                    sound1.play()
                    points+=2
                    q4.centery=randint(-200,0)
                    q4.centerx=randint(50,550)
                    xy=posmouse
                    s4=font3.render(f'+2',True,(15, 9, 219))
                    t4=sec
                    screen.blit(s4,(xy))
                    c4=1
                if q5.collidepoint(posmouse):
                    sound1.play()
                    points+=1
                    q5.centery=randint(-200,0)
                    q5.centerx=randint(50,550)
                    xy=posmouse
                    s5=font3.render(f'+1',True,(255, 227, 31))
                    t5=sec
                    screen.blit(s5,(xy))
                    c5=1
                if b1.collidepoint(posmouse):
                    y=b1.centery
                    x=b1.centerx
                    sound2.play()
                    b1.centery=randint(-200,0)
                    b1.centerx=randint(50,550)
                    damage-=1
                    xy=posmouse
                    sb1=font3.render(f'-1',True,bordeaux)
                    tb1=sec
                    screen.blit(esplosione,(x-45,y-45))
                    cb1=1

                    bomba1.draw()
                if b2.collidepoint(posmouse):
                    y=b2.centery
                    x=b2.centerx
                    sound2.play()
                    b2.centery=randint(-200,0)
                    b2.centerx=randint(50,550)
                    damage-=1
                    screen.blit(esplosione,(x-45,y-45))
                    bomba2.draw()
                    xy=posmouse
                    sb1=font3.render(f'-1',True,bordeaux)
                    tb2=sec
                    screen.blit(sb1,(xy))
                    cb2=1

                if n1.collidepoint(posmouse):
                    y=n1.centery
                    x=n1.centerx
                    sound2.play()
                    n1.centery=randint(-200,0)
                    n1.centerx=randint(50,550)
                    damage-=3
                    screen.blit(nesplosione,(x-45,y-45))
                    nuke.draw()
                    xy=posmouse
                    sn1=font3.render(f'-3',True,bordeaux)
                    tn1=sec
                    screen.blit(sn1,(xy))
                    cn1=1

            if t1!=None:
                if sec-t1==60 and c1==1:
                    screen.blit(s,screenrect)
                    c1=0
            if t2!=None:
                if sec-t2==60 and c2==1:
                    screen.blit(s,screenrect)
                    c2=0
            if t3!=None:
                if sec-t3==60 and c3==1:
                    screen.blit(s,screenrect)
                    c3=0
            if t4!=None:
                if sec-t4==60 and c4==1:
                    screen.blit(s,screenrect)
                    c4=0
            if t5!=None:
                if sec-t5==60 and c5==1:
                    screen.blit(s,screenrect)
                    c5=0
            if tb1!=None:
                if sec-tb1==60 and cb1==1:
                    screen.blit(s,screenrect)
                    cb1=0
            if tb2!=None:
                if sec-tb2==60 and cb2==1:
                    screen.blit(s,screenrect)
                    cb2=0
            if tn1!=None:
                if sec-tn1==60 and cn1==1:
                    screen.blit(s,screenrect)
                    cn1=0

        
            punteggio=font1.render(f'    {points}',True,'WHITE')
            danni=font1.render(f'VITE:  {damage}',True,'WHITE')
            for i in range(damage):
                vite[i].draw()
            screen.blit(punteggio,(0,65))
        if damage<=0 or gioco==6:
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
            scrittarecord=font1.render(f'RECORD : {record}',True, 'WHITE')
            screen.blit(scrittarecord,(180,100))

            punti=font1.render(f'{points}',True,'WHITE')
            screen.blit(punti,(270,500))
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
                    gioco=2
                    

                    
            pygame.display.flip()
            clock.tick(60)
