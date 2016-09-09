from message_handler import MessageHandler

class GetFileHandler(MessageHandler):
    def handle_message(self, message, socket, address):
        for file_name in message.split(','):
            socket.send("here is file {}\n".format(file_name))

        return True