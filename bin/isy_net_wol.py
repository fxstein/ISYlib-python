#!/usr/local/bin/python2.7

"""

Simple example to send a WoL to a registared system on the ISY

if this script is call without any arg 
we print a list of registared WoL systems

if we have any args we treat them as registared WoL Id's
and attempt to send a WoL packet 

"""

import sys
import ISY
from ISY.IsyExceptionClass import IsyResponseError, IsyValueError
 
  
myisy= ISY.Isy(debug=0)
   
myisy.load_net_wol()

if len(sys.argv[1:]) > 0:
    for a in sys.argv[1:] :
	try :
	    myisy.net_wol(a)
	except (IsyValueError, IsyResponseError), errormsg :
	    print "problem sending WOL to {!s} : {!s}".format(a, errormsg)
	    next
	else :
	    print "WOL sent to {!s}".format(a)
else :
    pfmt = "{:<5}{:<16} {:<20}"
    print(pfmt.format("Id", "Name", "Mac"))
    print(pfmt.format("-" * 4, "-" * 20, "-" * 20))
    for w in myisy.net_wol_iter():
       if "id" in w :
	   print(pfmt.format(w['id'], w['name'], w['mac']))


