"""
Implementation of a terminal in Pyhon
"""

class PTerm:
	

	def __init__(self):
		self.__seguir=True
		self.__prompt="> "

	def printPrompt(self):
		print self.__prompt
	
	"""Execute a given command if it is implemented"""
	def evaluarComando(self, com):
		"""Use of dictionary (or associative array) as a 
		substitute for the swithc-case statement"""
		dictionary = {
			"exit": self.com_exit,
			"ls": self.com_placeholder,
		}
		
		try:		
			dictionary[com]()
		except KeyError:
			print com + ": Command not found."
	
	"""Main loop of the terminal, asks for a command and executes it."""
	def mainLoop(self):
		while(self.__seguir):
			#Handle execption if user press Ctrl+C
			try:
				comando=raw_input(self.__prompt)
			except (KeyboardInterrupt, EOFError) as error:
				print "Execution interrupted by User"
				exit()

			self.evaluarComando(comando)

		print "finishing..."
		return 0


	#---------------------------------------------
	#----COMMANDS-IMPLEMENTATION------------------
	#---------------------------------------------

	def com_exit(self):
		self.__seguir=False

	def com_placeholder(self):
		print "ima placholder"
	



if __name__ == "__main__":
	t = PTerm()
	t.mainLoop()
