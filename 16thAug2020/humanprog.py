import pyttsx3
import os

# pyttsx3.speak("Welcome to my tools")


while True:
	print("chat with me with your requirements : "  , end='')
	p = input()

	# print(p)
	# os.system(p)

	if ("run" in p)  and ("chrome" in p):
	  os.system("chrome")

	elif (("run" in p) or  ("execute" in p )) and  (("notepad" in p) or ("editor" in p) ) :
	  os.system("notepad")

	elif ("run" in p)  and ("player" in p) and ("media" in p):
	  os.system("wmplayer")

	elif  ("exit" in p)  or ("quit" in p):
	  break

	else:
	  print("dont support")


