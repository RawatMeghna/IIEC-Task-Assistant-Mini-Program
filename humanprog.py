import pyttsx3
import os

pyttsx3.speak("Welcome to voice command software")
print("Welcome to voice command software")

while True:
	pyttsx3.speak("What can I Help for you ")
	print("What can I Help for you : ", end='')
	p=input()

	if (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("chrome" in p) or ("google" in p)):
		
		if (("dont" in p) or ("not" in p) or ("don't" in p)):
			print("", end='')
		else:
			pyttsx3.speak("opening  google chrome")
			os.system("start chrome")

	elif (("run" in p) or ("launch" in p) or ("open" 	in p) or ("execute" in p)) and (("notepad" in p) or("notebook" in p) or ("editor" in p)):
		
		if (("dont" in p) or ("not" in p) or ("don't" in p)):
			print("", end='')
		else:
		
			pyttsx3.speak("opening notepad")
			os.system("notepad")

	elif (("run" in p) or ("launch" in p) or 	("execute" in p) or ("open" in p)) and (("media" in p) and ("player" in p)):
		
		if (("dont" in p) or ("not" in p) or ("don't" in p)):
			print("", end='')
		else:
		
			pyttsx3.speak("opening windows media player")
			os.system("wmplayer")

	elif (("run" in p) or ("launch" in p) or 	("execute" in p) or ("open" in p)) and (("explorer" in p) or ("browser" in p)):

		if (("dont" in p) or ("not" in p) or ("don't" in p)):
			print("", end='')
		else:

			pyttsx3.speak("opening internet explorer")
			os.system("start iexplore")

	elif (("run" in p) or ("launch" in p) or 	("execute" in p) or ("open" in p)) and (("outlook" in p)):
		if (("dont" in p) or ("not" in p) or ("don't" in p)):
			print("", end='')
		else:

			pyttsx3.speak("opening microsoft outlook")
			os.system("start outlook")

	elif (("run" in p) or ("launch" in p) or 	("execute" in p) or ("open" in p)) and (("powerpoint" in p)):
		if (("dont" in p) or ("not" in p) or ("don't" in p)):
			print("", end='')
		else:
			pyttsx3.speak("opening microsoft powerpoint")
			os.system("start powerpnt")

	elif (("run" in p) or ("launch" in p) or 	("execute" in p) or ("open" in p)) and (("computer" in p) or ("pc" in p)):
		if (("dont" in p) or ("not" in p) or ("don't" in p)):
			print("", end='')
		else:
			pyttsx3.speak("opening my computer")
			os.system("start explorer")

	elif (("run" in p) or ("launch" in p) or 	("execute" in p) or ("open" in p)) and (("calculator" in p) or ("calculations" in p)):
		if (("dont" in p) or ("not" in p) or ("don't" in p)):
			print("", end='')
		else:
			pyttsx3.speak("opening calculator")
			os.system("calc")

	elif (("run" in p) or ("launch" in p) or 	("execute" in p) or ("open" in p)) and (("magnifier" in p) or ("zoom" in p)):
		if (("dont" in p) or ("not" in p) or ("don't" in p)):
			print("", end='')
		else:
			pyttsx3.speak("opening magnifier")
			os.system("start magnify")

	elif (("run" in p) or ("launch" in p) or 	("execute" in p) or ("open" in p)) and (("paint" in p) or ("draw" in p)):
		if (("dont" in p) or ("not" in p) or ("don't" in p)):
			print("", end='')
		else:
			pyttsx3.speak("opening paint")
			os.system("start mspaint")

	elif (("run" in p) or ("launch" in p) or 	("execute" in p) or ("open" in p)) and (("registry" in p) and ("editor" in p)):
		if (("dont" in p) or ("not" in p) or ("don't" in p)):
			print("", end='')
		else:
			pyttsx3.speak("opening registry editor")
			os.system("start regedit")

	elif (("run" in p) or ("launch" in p) or 	("execute" in p) or ("open" in p)) and (("wordpad" in p) or ("word" in p)):
		if (("dont" in p) or ("not" in p) or ("don't" in p)):
			print("", end='')
		else:
			pyttsx3.speak("opening wordpad")
			os.system("start write")

	elif (("run" in p) or ("launch" in p) or 	("execute" in p) or ("open" in p)) and (("system" in p) and ("configuration" in p)):
		if (("dont" in p) or ("not" in p) or ("don't" in p)):
			print("", end='')
		else:
			pyttsx3.speak("opening system configuration")
			os.system("msconfig")
	
	elif (("run" in p) or ("launch" in p) or 	("execute" in p) or ("open" in p)) and (("command" in p) and ("promt" in p) or ("cmd" in p)):
		if (("dont" in p) or ("not" in p) or ("don't" in p)):
			print("", end='')
		else:
			pyttsx3.speak("opening command promt")
			os.system("start cmd.exe")

	elif (("make" in p) or ("open" in p) or ("create" in p)) and (("directory" in p) or ("folder" in p)):
		if (("dont" in p) or ("not" in p) or ("don't" in p)):
			print("", end='')
		else:
			path = input("Enter thr name of Folder:")
			pyttsx3.speak("opening path") 
			os.mkdir("path")
	elif (("run" in p) or ("launch" in p) or 	("execute" in p) or ("open" in p)) and (("whatsapp" in p)):
		if (("dont" in p) or ("not" in p) or ("don't" in p)):
			print("", end='')
		else:
			pyttsx3.speak("opening whatsapp") 
			os.system("whatsapp.lnk")
	elif (("run" in p) or ("launch" in p) or 	("execute" in p) or ("open" in p)) and (("tasklist" in p)):
		if (("dont" in p) or ("not" in p) or ("don't" in p)):
			print("", end='')
		else:
			pyttsx3.speak("opening tasklist") 
			os.system("tasklist")
	elif (("run" in p) or ("launch" in p) or 	("execute" in p) or ("open" in p)) and (("excel" in p)):
		if (("dont" in p) or ("not" in p) or ("don't" in p)):
			print("", end='')
		else:
			pyttsx3.speak("opening microsoft excel") 
			os.system("start excel.exe")
	elif (("run" in p) or ("launch" in p) or 	("execute" in p) or ("open" in p)) and (("control" in p) and ("panel" in p)):
		if (("dont" in p) or ("not" in p) or ("don't" in p)):
			print("", end='')
		else:
			pyttsx3.speak("opening control panel") 
			os.system("control panel")

	elif ("stop" in p) or ("close" in p) or ("exit" in p) or ("end" in p):
		pyttsx3.speak("closing the software")
		break

	else:
		pyttsx3.speak("don't support, Try again")