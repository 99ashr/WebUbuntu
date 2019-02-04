#!/usr/bin/python3

import cgi
import cgitb
cgitb.enable()

mypage_data=cgi.FieldStorage()

str = 'hello from cgi!'
print "Content-type: text/html\n\n"
print "%s" % str