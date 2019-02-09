#!/usr/bin/python

import cgi
import  commands
import cgitb
cgitb.enable()



print("Content-type:text/html\r\n\r\n")
print  ("<html><head><title>Present Working Directory</title>")
print ("<body><h1>")

# gettting  html data 
mypage_data=cgi.FieldStorage()
FirstName=mypage_data.getvalue('FirstName')
LastName=mypage_data.getvalue('LastName')

print FirstName+" "+ LastName
print 
print ("</h1></body></html>")