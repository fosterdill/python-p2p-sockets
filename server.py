import socket
import sys
import signal

class Server(object):
    def __init__(self, protocol_manager):
        self.protocol_manager = protocol_manager
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def listen(self, host_and_port, message_handler, concurrent_connections = 5):
        self.server_socket.bind(host_and_port)
        self.server_socket.listen(concurrent_connections)

        while True:
            (client_socket, client_address) = self.server_socket.accept()
            data = ""

            while not self.protocol_manager.did_close(data):
                data += client_socket.recv(128)

                if not data:
                    break

                while True:
                    (message, data) = self.protocol_manager.unshift_message(data)

                    if message:
                        message_handler(message)
                    else:
                        break

            client_socket.close()

