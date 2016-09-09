from get_file_handler import GetFileHandler
from delegate_handler import DelegateHandler

GET_COMMANDS = {
    'file': GetFileHandler()
}

SERVER_COMMANDS = {
    'get': DelegateHandler(GET_COMMANDS, 'get')
}