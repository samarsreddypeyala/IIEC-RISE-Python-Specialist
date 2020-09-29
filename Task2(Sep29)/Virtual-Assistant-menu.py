#!/usr/bin/python3
print("content-type: text/html")
print()
import subprocess as sp
import cgi
form=cgi.FieldStorage()
cmd=form.getvalue("x")

if(cmd=="Open Chrome"):
	sp.getoutput("chrome")
elif(cmd=="Open Firefox"):
	sp.getoutput("firefox")
elif(cmd=="Open Notepad"):
	sp.getoutput("notepad")
elif(cmd=="Open Virtualbox"):
	sp.getoutput("virtualbox")
elif(cmd=="Show Today's Date")
	sp.getoutput("Date")
elif(cmd=="Show Calendar"):
	sp.getoutput("cal")
else:
	print("Wrong Input Action, Please input a valid one...\n")