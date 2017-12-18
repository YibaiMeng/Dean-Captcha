#! /usr/bin/python3
import cgi
#import cgitb; cgitb.enable() # Optional; for debugging only
import access_database
form = cgi.FieldStorage()
if "nextNumber" in form:
    print ("Content-Type: application/json")
    print ("")
    print('{')
    a, b = access_database.get_next_captchas()
    print('"number_now" : %r,' % a)
    print('"number_next" : %r' % b)
    print('}')
elif "id" in form and "value" in form:
    print ("Content-Type: application/json")
    print ("")
    print('{')
    print('"code" : 1')
    print('}')
    access_database.store_value_into_db(ID=form["id"].value, text_value=form["value"].value)
