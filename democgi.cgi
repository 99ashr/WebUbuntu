#!/usr/bin/python
import cgi
import os
import commands
import sys
print("Content-type:text/html\r\n\r\n")
print("")
form = cgi.FieldStorage()
if form.getvalue("name"):
	name = form.getvalue("name")
	print("<h1>Hello "+name+"! Thanks for using my script!</h1><br />")
if form.getvalue("happy"):
	print("<p> Yay! I'm happy too! </p>")
if form.getvalue("sad"):
	print("<p> Oh no! Why are you sad? </p>")
if form.getvalue("cmd"):
	sys.stdout.flush()
	x=os.system("pwd")
	print x
