from ui.commands.command import Command
from ui.commands.delete_note import DeleteNote
from ui.commands.edit_note import EditNote
from ui.commands.end_program import EndProgram
from ui.commands.load_from_file import LoadFromFile
from ui.commands.new_note import NewNote
from ui.commands.save_to_file import SaveToFile


class MainMenu:
    command_list: list[Command]
    console_ui = None

    def __init__(self, console_ui):
        self.console_ui = console_ui
        self.command_list = []
        self.command_list.append(NewNote(self.console_ui))
        self.command_list.append((EditNote(self.console_ui)))
        self.command_list.append((DeleteNote(self.console_ui)))
        self.command_list.append((SaveToFile(self.console_ui)))
        self.command_list.append((LoadFromFile(self.console_ui)))
        self.command_list.append(EndProgram(self.console_ui))

    def add_command(self, command):
        self.command_list.append(command)

    def form_menu(self) -> str:
        menu: str = ""
        for i in range(self.command_list.__len__()):
            menu += f"{i + 1}. " + self.command_list[i].get_description() + "\n"
        return menu

    def execute(self, choice: int):
        self.command_list[choice - 1].execute()

    def get_menu_size(self) -> int:
        return self.command_list.__len__()
