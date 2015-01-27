#!/usr/bin/env python

import cgi

form = cgi.FieldStorage()

birthdate = form.getvalue('birthdate')
hobby = form.getvalue('main hobby')


print """Content-type: text/html

<form method="post" action="receive_name_family.py">
Name: <input type="text" name="name" />
<br/>
Family: <input type="text" name="family" />
<br/>
<input type="submit" value="Submit">
</form>"""

print "Your birthday is %s" % (birthdate)
print "Your main hobby is %s" % (hobby)
