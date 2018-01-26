import os
import subprocess

"""The first argument must be the name of the script"""
def com_script(pterm, args):
	
	"""CODE TO CHANGE DIR.
	TAKING FOR GRANTE$D THE FIRST ARGUMENT IS
	THE PATH TO GO TO."""
	"""
	#print(type(args))
	if len(args)>0:
		try:
			os.chdir(args[0])
		except OSError as e:
			print("PTERM:script.py: "+str(e))
	"""

	#Save original path where we start
	original_path = os.getcwd()
	print(os.getcwd())
	
	#change to path where scripts are
	rootPath = pterm.getRootPath()
	os.chdir(rootPath+"/scripts")
	print(os.getcwd())
	###SHOW-AVAILABLE-SCRIPTS###
	if pterm.getDebug():
		script_list = subprocess.check_output("ls").split()
		print("Available Scripts:")
		for i in xrange(0, len(script_list)):
			print("- "+script_list[i])
	###EXECUTE-SCRIPT###
	if len(args)>0:
		#Continue if no errors occurred.
		#Set to False if errors occur.
		goOn = True
		#Take first armunet as name of the script
		try:
			script_file=open(args[0])
		except IOError as e:
			print("PTERM:script.py: "+str(e))
			goOn=False
			return
		if goOn:
			#get lines of script in a list
			lineas_script = script_file.read().splitlines()
			#Security
			print("These are the lines to be executed: ")
			for linea in xrange(0,len(lineas_script)):
				print(lineas_script[linea])
			print("WARNING: this could cause irreversible damage to your computer")
			choice = raw_input("CONTINUE?(Y/N)")
			if choice.lower() != "y":
				goOn=False
			
			if goOn:
				#Execute lines in the cript file
				for linea in xrange(0,len(lineas_script)):
					#os.system(lineas_script[linea])
					subprocess.call(lineas_script[linea], shell=True)
	
	#Restore starting path
	os.chdir(original_path)
	print(os.getcwd())
