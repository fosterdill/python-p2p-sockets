class MessageHandler(object):
    def handle_message(self, message, socket, address, protocol_buffer, is_client):
        raise NotImplementedError( "MessageHandler interface not implemented" )