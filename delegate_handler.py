from message_handler import MessageHandler

class DelegateHandler(MessageHandler):
    def __init__(self, command_handlers, parent_command):
        self.command_handlers = command_handlers
        self._handler_delegate = None
        self.parent_command = parent_command

    def handle_message(self, message, socket, address):
        if self._handler_delegate:
            if self._handler_delegate.handle_message(message.strip(), socket, address):
                self.stop_delegation()
                return True
        else:
            try:
                self.delegate_to(self.command_handlers[message.strip()])
            except KeyError:
                socket.send("Unknown command {} for parent {}".format(message.strip(), self.parent_command))
                return True

    def delegate_to(self, handler):
        self._handler_delegate = handler

    def stop_delegation(self):
        self._handler_delegate = None