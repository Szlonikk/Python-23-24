import time
import os
czas = 10
wysokosc = 20
pozycja = 0
kierunek = 1
koniec = time.time() + czas
tekst = "Hello world!"
while time.time() < koniec:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n' * pozycja + tekst)
    pozycja += kierunek
    if pozycja == wysokosc or pozycja == 0:
        kierunek *= -1
    time.sleep(0.05)