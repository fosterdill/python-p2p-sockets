from server import Server
from protocol import Protocol
from protocol_buffer import ProtocolBuffer
from message_handler import MessageHandler
from upnp_client import UPnPClient

import sys

HOST = ''

try:
	PORT = int(sys.argv[0])
except ValueError:
	PORT = 5335

def main():
    protocol_buffer = ProtocolBuffer(Protocol)
    main_server = Server(protocol_buffer)
    message_handler = MessageHandler()
    upnp_client = UPnPClient()
    port_is_mapped = upnp_client.map(PORT)

    print "Mapping port {}...".format(PORT)
    if upnp_client.map(PORT):
    	try:
    		print "Starting server on external ip {} on port {}".format(upnp_client.get_external_ip(), PORT)
    		main_server.listen((HOST, PORT), message_handler)

    	except KeyboardInterrupt:
    		if upnp_client.unmap(PORT):
    			print "Unmapped port {}".format(PORT)
    		else:
    			print "Couldn't unmap port {}".format(PORT)
    else:
    	print "Could not map port {}".format(PORT)


if __name__ == '__main__':
    main()