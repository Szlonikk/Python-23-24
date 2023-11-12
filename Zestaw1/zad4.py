import sys
import time

def pasek_postepu(dl, postep):
    pelna_dl = 50  
    pelna_dl_procent = 100

    ilosc_pelnych = int(pelna_dl * (postep / pelna_dl_procent))
    ilosc_pustych = pelna_dl - ilosc_pelnych

    pasek = "|" + "=" * ilosc_pelnych + "-" * ilosc_pustych + "|"

    sys.stdout.write(f"\r{pasek} {postep}%")
    sys.stdout.flush()

dlugosc = 100
for i in range(dlugosc + 1):
    postep = int((i / dlugosc) * 100)
    pasek_postepu(dlugosc, postep)
    time.sleep(0.1) 

print("\nZakończono!")
