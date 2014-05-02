#!/usr/local/bin/python2.7 -u
__author__ = "Peter Shipley"


import os
import keyring
import ConfigParser

from  ISY.IsyEvent import ISYEvent

def main() :

    config = ConfigParser.ConfigParser()
    config.read('isy.cfg')
    
    server = ISYEvent()

    # you can subscribe to multiple devices
    # server.subscribe('10.1.1.25')

    isy_addr = config.get('isy', 'addr')
    isy_user = config.get('isy', 'user')

    server.subscribe(
	addr=isy_addr,
	userl=isy_user,
	userp=keyring.get_password("isy", isy_user) )

    server.set_process_func(ISYEvent.print_event, "")

    try:
	print('Use Control-C to exit')
	server.events_loop()   #no return
    #    for d in  server.event_iter( ignorelist=["_0", "_11"] ):
    #	server.print_event(d, "")
    except KeyboardInterrupt:
	print('Exiting')



if __name__ == '__main__' :
    main()
    exit(0)
