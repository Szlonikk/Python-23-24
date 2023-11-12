dlugosc = int (input("Podaj dlugosc miarki: "))

miarkaGora = "|"
miarkaDol = "0"

for x in range (1, dlugosc + 1) :
	miarkaGora += "....|"
	miarkaDol += str (x).rjust (5)
	
miarka = miarkaGora + "\n" + miarkaDol

print (miarka)