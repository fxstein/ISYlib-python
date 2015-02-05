#!/usr/local/bin/python3.4 -u
__author__ = "Peter Shipley"


import os
import ConfigParser

from  ISY.IsyEvent import ISYEvent

def main() :

    config = ConfigParser.ConfigParser()
    config.read(os.path.expanduser('~/home.cfg'))

    server = ISYEvent()

    isy_addr = config.get('isy', 'addr')
    isy_user = config.get('isy', 'user')
    isy_pass = config.get('isy', 'pass')

    server.subscribe(
            addr=isy_addr,
            userl=isy_user,
            userp=isy_pass )

    server.set_process_func(ISYEvent.print_event, "")

    try:
        print('Use Control-C to exit')
        server.events_loop()   #no return
    except KeyboardInterrupt:
        print('Exiting')



if __name__ == '__main__' :
    main()
    exit(0)
