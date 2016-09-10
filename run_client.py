#! /usr/bin/env python2

from client import Client
from protocol import ServerProtocol
from protocol_buffer import ProtocolBuffer
from delegate_handler import DelegateHandler
from upnp_client import UPnPClient
from commands import SERVER_COMMANDS

import sys

HOST = '127.0.0.1'

try:
    PORT = int(sys.argv[1])
except (ValueError, IndexError):
    PORT = 5335

def main():
    protocol_buffer = ProtocolBuffer(ServerProtocol)
    client = Client((HOST, PORT), protocol_buffer)
    delegate_handler = DelegateHandler(SERVER_COMMANDS, 'Client')

    client.connect(delegate_handler)

    try:
        while True:
            client.process(raw_input('> '))
    except KeyboardInterrupt:
        client.close()

if __name__ == '__main__':
    main()