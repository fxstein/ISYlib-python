#!/usr/local/bin/python2.7

from ISY import *


myisy = IsyClass( debug=0 )

for nod in myisy :
   if nod.type == "scene" :
       #print "%-20s %-12s\t%s" % (nod.name, nod.address, nod.members )
       print "%-20s %-12s" % (nod.name, nod.address )
   else :
       print "%-20s %-12s\t%s" % (nod.name, nod.address, nod.formatted)
