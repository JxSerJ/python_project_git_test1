from config import FILE_PATH
from file_handler.file_handler import FileHandler
from ui.console_ui import ConsoleUI


class Connector:
    console_ui: ConsoleUI
    file_handler: FileHandler

    def __init__(self):
        self.console_ui: ConsoleUI = ConsoleUI()
        self.file_handler: FileHandler = FileHandler(FILE_PATH)


con = Connector()
