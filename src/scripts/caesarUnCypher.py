


def uncypherLetter(lista_men, i, salto):
	lista_men[i] = chr(ord(lista_men[i])+salto)
	#comprobamos si ha dado la vuelta
	#ord('z') = 122
	#ord('a') = 97
	if ord(lista_men[i]) > 122:
		lista_men[i] = 'a'

def uncypher(msg, saltoMax):
	lista_mensaje = list(msg.lower())
	
	for salto in xrange(0, saltoMax):
		for letter in xrange(0, len(lista_mensaje)):
			uncypherLetter(lista_mensaje, letter, 1)
		str1 = "".join(lista_mensaje)
		print "salto: " + str(salto) + " -> " +str1
	
if __name__ == "__main__":
	mns = raw_input("Introduce Mensaje:")
	uncypher(mns, 26)
