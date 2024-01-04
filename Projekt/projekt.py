from time import sleep
import pygame

from Platforma import Platforma
from Kulka import Kulka
from Klocek import Klocek

SZEROKOSC_EKRANU = 1024 
WYSOKOSC_EKRANU = 800
Poziom = 0
Zycia = 1


pygame.init()
pygame.font.init()

czcionka = pygame.font.SysFont('Comic Sans MS', 24)
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
obraz_tlo = pygame.image.load('images/background.png')
obraz_game_over = pygame.image.load('images/gameover.jpg')

#poziomy gry
poziom1 = [
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
poziom2 = [
    [0, 0, 1, 2, 3, 3, 2, 1, 0, 0],
    [0, 1, 1, 1, 2, 2, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 2, 0, 0, 2, 0, 2, 0]
]
poziom3 = [
    [2, 3, 2, 2, 2, 2, 2, 2, 3, 2],
    [2, 1, 3, 1, 1, 1, 1, 3, 1, 2],
    [2, 3, 1, 3, 1, 1, 3, 1, 3, 2],
    [3, 2, 2, 2, 3, 3, 2, 2, 2, 3],
    [0, 0, 2, 2, 3, 3, 2, 2, 0, 0],
    [0, 0, 2, 0, 3, 3, 0, 2, 0, 0],
    [0, 0, 3, 0, 3, 3, 0, 3, 0, 0]
]

klocki = pygame.sprite.Group()
def dodaj_klocki():
    wczytany_poziom = None
    if Poziom == 0:
        wczytany_poziom = poziom1
    if Poziom == 1:
        wczytany_poziom = poziom2
    if Poziom == 2:
        wczytany_poziom = poziom3

    for i in range(10):
        for j in range(7):
            if wczytany_poziom[j][i] != 0:
                klocek = Klocek(32+i*96, 32+j*48, wczytany_poziom[j][i])
                klocki.add(klocek)
dodaj_klocki()

platforma = Platforma()
kulka = Kulka()


gra_dziala = True
while gra_dziala:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False
    
    #sterowanie platforma
    wcisniete_klawisze=pygame.key.get_pressed()
    if wcisniete_klawisze[pygame.K_a]:
        platforma.ruszaj_platforma(-1)
    if wcisniete_klawisze[pygame.K_d]:
        platforma.ruszaj_platforma(1)      
    
    #sprawdzenie czy wszystkie klocki zostaly zniszczone
    if len(klocki.sprites()) == 0:
        Poziom += 1
        if Poziom >= 3:
            break
        kulka.zresetuj_pozycje()
        platforma.zresetuj_pozycje()
        dodaj_klocki()
    

 
    kulka.aktualizuj(platforma, klocki)

    #sprawdzenie czy kulka spadla
    if kulka.przegrana:
        Zycia -= 1
        if Zycia <= 0:
            ekran.fill((0, 0, 0))
            ekran.blit(obraz_game_over, ((SZEROKOSC_EKRANU - obraz_game_over.get_width()) // 2, (WYSOKOSC_EKRANU - obraz_game_over.get_height()) // 2))            
            pygame.display.flip()
            pygame.time.delay(500)
            break
        kulka.zresetuj_pozycje()
        platforma.zresetuj_pozycje()

    klocki.update()
    platforma.aktualizuj()
    
    ekran.blit(obraz_tlo, (0,0))

    for brick in klocki:
        ekran.blit(brick.obraz, brick.pozycja)
    
    ekran.blit(platforma.obraz, platforma.pozycja)
    ekran.blit(kulka.obraz, kulka.pozycja)

    tekst = czcionka.render(f'Poziom: {Poziom+1}, Życia: {Zycia}', False, (255, 0, 255))
    ekran.blit(tekst, (16, 16))

    pygame.display.flip()
    zegar.tick(60)

pygame.quit()