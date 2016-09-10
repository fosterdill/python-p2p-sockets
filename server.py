import socket
import sys
import signal

class Server(object):
    def __init__(self, protocol_buffer, recv_byte_size = 128):
        self.protocol_buffer = protocol_buffer
        self.recv_byte_size = recv_byte_size
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def close(self):
        self.server_socket.close()

    def listen(self, host_and_port, message_handler, concurrent_connections = 5):
        self.server_socket.bind(host_and_port)
        self.server_socket.listen(concurrent_connections)

        while True:
            (client_socket, client_address) = self.server_socket.accept()

            while not self.protocol_buffer.did_close():
                new_data = client_socket.recv(self.recv_byte_size)
                self.protocol_buffer.append_data(new_data)

                if not new_data:
                    break

                self.handle_messages(message_handler.handle_message, client_socket, client_address)

            client_socket.close()
            self.protocol_buffer.clear()

    def handle_messages(self, handle_message, client_socket, client_address):
        while True:
            message = self.protocol_buffer.get_message()

            if message:
                handle_message(message, client_socket, client_address, self.protocol_buffer, False)
            else:
                break

