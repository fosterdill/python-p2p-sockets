#! /usr/bin/env python2

from server import Server
from protocol import ServerProtocol
from protocol_buffer import ProtocolBuffer
from delegate_handler import DelegateHandler
from upnp_client import UPnPClient
from commands import SERVER_COMMANDS

import sys

HOST = ''

try:
    PORT = int(sys.argv[1])
except (ValueError, IndexError):
    PORT = 5335

def main():
    protocol_buffer = ProtocolBuffer(ServerProtocol)
    main_server = Server(protocol_buffer)
    delegate_handler = DelegateHandler(SERVER_COMMANDS, 'Server')
    upnp_client = UPnPClient()

    print "Mapping port {}...".format(PORT)
    if upnp_client.map(PORT):
        try:
            print "Starting server with external ip {} on port {}".format(upnp_client.get_external_ip(), PORT)
            main_server.listen((HOST, PORT), delegate_handler)

        except KeyboardInterrupt:
            main_server.close()
            
            if upnp_client.unmap(PORT):
                print "Unmapped port {}".format(PORT)
            else:
                print "Couldn't unmap port {}".format(PORT)
    else:
        print "Could not map port {}".format(PORT)


if __name__ == '__main__':
    main()