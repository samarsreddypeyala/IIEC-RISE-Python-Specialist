#Problem: "Convert the OS based program into a menu driven program using Python Code which will execute the required user query when user will give the input as a text."

#Solution:

import os

import pyttsx3


pyttsx3.speak("Hi, welcome to my menu driven and voice assistant program")


while True:

	print("chat with me with your requirements:")

p = input()


if ("hi" in p) or ("hii" in p) or ("hello" in p):

	print("Hello, how can I help you")


elif("introduce yourself"in p):
    
    pyttsx3.speak("I am Robo and your personal assistant....")
    
    print("\nI am Robo and your personal assistant....\n")
        

elif ((("run" in p) or ("launch " in p) or ("open" in p)) and ("chrome" in p)) :

	pyttsx3.speak("opeing chrome")
	
	os.system("chrome")

   
elif("powerpoint"in p):
    
    pyttsx3.speak("ok, opening powerpoint")
    
    os.system("start powerpnt")

elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p)) and (("notepad" in p) or ("editor" in p)):

	pyttsx3.speak("opening notepad")

	os.system("notepad")


elif (("open" in p) or ("run" in p) or ("play" in p)) and (("player" in p) or ("media" in p)):

	pyttsx3.speak("opening media player")

	os.system("wmplayer")


elif (("open" in p) or ("run" in p) or ("launch" in p)) and ("arduino" in p):

	pyttsx3.speak("opening arduino")

	os.system("arduino")

elif("system information"in p):

    pyttsx3.speak("this is all about your system")
    
    os.system("SYSTEMINFO") 

elif (("open" in p) or ("run" in p) or ("connect" in p) or ("launch" in p)) and ("skype" in p):
	
	pyttsx3.speak("opening skype")

	os.system("skype")


elif (("open" in p) or ("run" in p) or ("launch" in p)) and ("google" in p):

	pyttsx3.speak("lets google it")

	os.system("chrome www.google.co.in")


elif (("open" in p) or ("run" in p) or ("launch" in p)) and (("calculator" in p) or ("calc" in p)):

	pyttsx3.speak("opening calculator")

	os.system("calc")


elif ("open" in p) and ("settings" in p):

	pyttsx3.speak("opening settings")

	os.system("set")


elif (("send" in p) or ("message" in p)) and ("whatsapp" in p):

	pyttsx3.speak("lets use whatsapp")
	
	x = input("enter number to send message: ")

	y = input("enter the message to send: ")

	os.system("chrome wa.me/91 "+x+" /? text = "+y+"")


elif (("send" in p) or ("open" in p ) or ("message" in p)) and ("mail" in p):

	pyttsx3.speak("mail it")

	os.system("chrome mail.google.com")
  
elif("exit" in p) or ("quit"in p) or ("bye"in p) or ("no"in p):
    
    pyttsx3.speak("ok \n bye \n see u later\n have a nice day  ")
        
    print("\nHave a Nice Day !!")
        
    break

else:
    
    pyttsx3.speak("its invalid...\nplease write VALID for more info.")
    
    print("its invalid...\nplease write VALID for more info. Thank you, bye")