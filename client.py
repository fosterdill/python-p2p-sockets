import socket
import sys
import signal

class Client(object):
    def __init__(self, host_and_port, protocol_buffer, recv_byte_size = 128):
        self.host_and_port = host_and_port
        self.protocol_buffer = protocol_buffer
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, delegate_handler):
        self.client_socket.connect(self.host_and_port)
        self.delegate_handler = delegate_handler

    def process(self, new_data):
        self.protocol_buffer.append_data(new_data)

        while True:
            message = self.protocol_buffer.get_message()
            if message:
                self.delegate_handler.handle_message(message.strip(), self.client_socket, self.client_socket.getsockname(), self.protocol_buffer, True)
            else:
                break

    def close(self):
        self.client_socket.close()