import pyttsx3
import os
pyttsx3.speak("welcome to my tools")

print("\n")
print("press1: To open chrome browser")
print("press2: To open notepad")
print("press3: To open media player")
print("\n")

print("enter ur choice:" ,end='')  
p=input()
#os.system(p)

if p==1:
	os.sytem("chrome")
if p==2:
	os.sytem("notepad")
if p==2:
	os.sytem("wmplayer")
else:
	print("dont support")

