"""
Implementation of a terminal in Pyhon
"""

import os

from commands import exit as f_exit
from commands import placeholder as f_placeholder
from commands import script as f_script

class PTerm:
	

	def __init__(self):
		#the main loop will continue executing while this value is True
		self.__seguir=True
		self.__prompt="> "
		self.__debug=True
		#path where the execution began
		self.__root_path=os.getcwd()
	
	"""Return the path where the execution began"""
	def getRootPath(self):
		return self.__root_path

	"""Useless"""	
	def printPrompt(self):
		print self.__prompt
		
	"""GETS & SETS of some attributes"""
	def getSeguir(self):
		return self.__seguir
    
	def setSeguir(self, value):
		if type(value) is bool:
			self.__seguir=value
		else:
			print "The specified value is not bool."
	
	def getDebug(self):
		return self.__debug
	
	"""Dado un comando devuelve dos listas.
	com es una lista con un solo elemento que contiene el comando.
	args es una lista que contiene 0 o mas argumentos para el comando.
	REQUIERE QUE com Y args ESTEN VACIAS CUANDO SE PASAN POR PARMETRO"""
	def parseComando(self,rawCom, com, args):
		"""
		Get commands and args
		"""
		allList = rawCom.split()
		com.append(allList.pop(0))
		#https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference
		#NO SE PUEDE HACER ESTO.
		#CAMBIA LA REFERENCIA DEL OBJETO POR
		#LO QUE NO CAMBIARA SU VALOR FUERA DE LA FUNCION
		#args = allList
		args.extend(allList)

	"""Execute a given command if it is implemented"""
	def evaluarComando(self, rawCom):
		"""Solo evaluamos el comando si es una cadena no vacia"""
		if len(rawCom)>0: 
			"""Parsear comando: separar orden de los argumentos"""
			command = list()
			args = list()
			self.parseComando(rawCom,command,args)
			if self.__debug:
				print "command: " + str(command)
				print "args: " + str(args)

			"""Use of dictionary (or associative array) as a 
			substitute for the swithc-case statement"""
			dictionary = {
				"exit": f_exit.com_exit,
				"ls": f_placeholder.com_placeholder,
				"script": f_script.com_script,
			}
			
			try:		
				dictionary[command[0]](self,args)
			except KeyError:
				print command[0] + ": Command not found."
	
	"""Main loop of the terminal, asks for a command and executes it."""
	def mainLoop(self):
		while(self.__seguir):
			#Handle execption if user press Ctrl+C
			try:
				comando=raw_input(self.__prompt)
			except (KeyboardInterrupt, EOFError) as error:
				print "Execution interrupted by User"
				os._exit(0)

			self.evaluarComando(comando)

		print "finishing..."
		return 0


	#---------------------------------------------
	#----COMMANDS-IMPLEMENTATION------------------
	#---------------------------------------------
	#Moved to commands package
	

if __name__ == "__main__":
	t = PTerm()
	t.mainLoop()
