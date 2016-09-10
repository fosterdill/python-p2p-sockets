from message_handler import MessageHandler
from protocol_buffer import ProtocolBuffer

class ShowFileHandler(MessageHandler):
    def __init__(self, inverse = False):
        self.inverse = inverse

    def handle_message(self, message, socket, address, protocol_buffer, is_client):
        if (is_client and not self.inverse) or (not is_client and self.inverse):
            if not self.inverse:
                socket.sendall('get file {} '.format(message))
            file_size_buffer = ProtocolBuffer(protocol_buffer.get_protocol())
            file_size = None

            while not file_size:
                protocol_buffer.append_data(socket.recv(4))
                file_size = int(protocol_buffer.get_message())

            file_data = socket.recv(file_size)
            new_file = open("new-{}".format(message), 'w')
            new_file.write(file_data)
            new_file.close()
        else:
            if self.inverse:
                socket.sendall('give file {} '.format(message))
            file = open(message, 'r')
            protocol = protocol_buffer.get_protocol()
            file_data = file.read()
            socket.sendall("{} ".format(str(len(file_data))))

            file.close()
            socket.sendall(file_data)

        return True 