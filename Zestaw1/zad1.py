import sys

def czynniki(n):
    czynniki = []
    dzielnik = 2

    while dzielnik * dzielnik <= n:
        if n % dzielnik == 0:
            czynniki.append(dzielnik)
            n //= dzielnik
        else:
            dzielnik += 1

    if n > 1:
        czynniki.append(n)

    return czynniki

def formatuj_wykladniki(czynniki):
    wynik = ""
    i = 0
    while i < len(czynniki):
        podstawa = czynniki[i]
        wykladnik = 0
        while i < len(czynniki) and czynniki[i] == podstawa:
            wykladnik += 1
            i += 1

        if wykladnik == 1:
            wynik += str(podstawa)
        else:
            wynik += f"{podstawa}^{wykladnik}"
        if i < len(czynniki):
            wynik += " * "
    return wynik

if len(sys.argv) < 2:
    print("Podaj jakas wartosc!")
else:
    for i in range(1, len(sys.argv)):
        liczba = int(sys.argv[i])
        czynniki_pierwsze = czynniki(liczba)
        sformatowany_wynik = formatuj_wykladniki(czynniki_pierwsze)
        print(f"{liczba} = {sformatowany_wynik}")
        