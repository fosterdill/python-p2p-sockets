from message_handler import MessageHandler

class DelegateHandler(MessageHandler):
    def __init__(self, command_handlers, parent_command):
        self.command_handlers = command_handlers
        self._handler_delegate = None
        self.parent_command = parent_command

    def handle_message(self, message, socket, address, protocol_buffer, is_client):
        if self._handler_delegate:
            if self._handler_delegate.handle_message(message.strip(), socket, address, protocol_buffer, is_client):
                self.stop_delegation()
                return True
        else:
            try:
                self.delegate_to(self.command_handlers[message.strip()])
            except KeyError:
                error_message = "Unknown command {} for parent {}".format(message.strip(), self.parent_command)

                if is_client:
                    print error_message
                else:
                    socket.send(error_message)
                    
                return True

    def delegate_to(self, handler):
        self._handler_delegate = handler

    def stop_delegation(self):
        self._handler_delegate = None