#!/usr/bin/env python

import cgi

form = cgi.FieldStorage()

name = form.getvalue('name')
family = form.getvalue('family')

print """Content-type: text/html

<form method="post" action="get_name_family.py">
Birthdate: <input type="text" name="birthdate" />
<br/>
Main Hobby: <input type="text" name="main hobby" />
<br/>
<input type="submit" value="Submit">
</form>"""

print "Your name is %s, your family is %s" % (name, family)
