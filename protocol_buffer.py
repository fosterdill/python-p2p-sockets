class ProtocolBuffer(object):
    def __init__(self, protocol, data = None):
        self._protocol = protocol
        self._data = data

    def append_data(self, data):
    	if self._data:
    		self._data += data
    	else:
    		self._data = data

    def clear(self):
    	self._data = None

    def did_close(self):
    	if self._data is None:
    		return False

    	return self._protocol.DISCONNECT in self._data

    def get_message(self):
        messages = filter(None, self._data.split(self._protocol.MESSAGE_END))

        if len(messages) > 1:
            self._data = self._data[len(messages[0]) + len(self._protocol.MESSAGE_END):]
            return messages[0]
        else:
        	return None