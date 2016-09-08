from server import Server
from protocol import Protocol
from protocol_manager import ProtocolManager

HOST = ''
PORT = 5334

def handle(message):
    print message

def main():
    manager = ProtocolManager(Protocol)
    main_server = Server(manager)

    main_server.listen((HOST, PORT), handle)

if __name__ == '__main__':
    main()