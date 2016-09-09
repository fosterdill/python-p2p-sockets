class MessageHandler(object):
    def handle_message(self, message, socket, address):
        print "from: ip {}, port {}".format(address[0], address[1])
        print 'message: {}'.format(message)
        socket.send("Your ip is {}".format(address[0]))