class ProtocolManager(object):
    def __init__(self, protocol):
        self.protocol = protocol

    def unshift_message(self, data):
        messages = filter(None, data.split(self.protocol.MESSAGE_END))

        if len(messages) > 1:
            unshifted_message = messages[0]

            return (unshifted_message, data[len(unshifted_message) + len(self.protocol.MESSAGE_END):])
        else:
            return (None, data)

    def did_close(self, data):
    	return self.protocol.DISCONNECT in data