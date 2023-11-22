najglebszyPoziom = 0
najglebszeListy = []

def zagniezdz (lista) :
	
	global najglebszyPoziom
	global najglebszeListy
	
	najglebszyPoziom = 0
	najglebszeListy = []
	
	szukaj (lista, 0)
	
	for i in najglebszeListy :
		i.append (i[len(i) - 1] + 1)
	
	return lista

def szukaj (lista, poziom) :
	
	global najglebszyPoziom
	global najglebszeListy
	
	for i in lista :
		if isinstance (i, list)	:
			szukaj (i, poziom + 1)
	
	if poziom > najglebszyPoziom :
		najglebszyPoziom = poziom
		najglebszeListy = []
		najglebszeListy.append (lista)
	elif poziom == najglebszyPoziom :
		najglebszeListy.append (lista)

lista = [1, 2, [3, 4, [5, 6], 5], 3, [4, 5]]
print (str (lista) + " => " +  str (zagniezdz (lista)), end='\n\n')
lista = [1, [2, 3], 4]
print (str (lista) + " => " +  str (zagniezdz (lista)), end='\n\n')
lista = [3, 4, [2, [1, 2, [7, 8], 3, 4], 3, 4], 5, 6, 7]
print (str (lista) + " => " +  str (zagniezdz (lista)), end='\n\n')
lista = [1, [3], [2]]
print (str (lista) + " => " +  str (zagniezdz (lista)), end='\n\n')