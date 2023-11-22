class Bug :
	
	licznik = 0
	
	def __init__ (self) :
		Bug.licznik += 1
		self.id = Bug.licznik
		
	def __del__ (self) :
		Bug.licznik -= 1
		print ("Koniec ID = " + str(self.id) + ", L = " + str(Bug.licznik))
	
	def __str__ (self) :
		return "Robak ID = " + str(self.id) + ", L = " + str(Bug.licznik)

bugs = []
for i in range(100) :
    bugs.append (Bug ())
    print (bugs[-1])