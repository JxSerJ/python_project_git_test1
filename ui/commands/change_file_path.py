from ui.commands.command import Command


class ChangeWorkingFile(Command):
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    def __init__(self, console_ui):
        super().__init__(console_ui)
        self.description = 'Change working file'

    def execute(self):
        self.console_ui.change_working_file()
