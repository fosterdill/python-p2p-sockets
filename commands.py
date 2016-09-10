from show_file_handler import ShowFileHandler
from delegate_handler import DelegateHandler

GET_COMMANDS = {
    'file': ShowFileHandler(),
}

GIVE_COMMANDS = {
    'file': ShowFileHandler(True),
}

SERVER_COMMANDS = {
    'get': DelegateHandler(GET_COMMANDS, 'get'),
    'give': DelegateHandler(GIVE_COMMANDS, 'give'),
}