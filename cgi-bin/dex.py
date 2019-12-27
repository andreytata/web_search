#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cgi, cgitb
form = cgi.FieldStorage() 

# Get data from fields
first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')

print ("Content-type: text/html\r\n\r\n")
print ("<!DOCTYPE html>")
print ("<html>")
print ("<head>")
print ("Content-type: text/html")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h2>Hello %s %s</h2>" % (first_name, last_name))
print ("</body>")
print ("</html>")
