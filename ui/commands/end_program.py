from ui.commands.command import Command


class EndProgram(Command):
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    def __init__(self, console_ui):
        super().__init__(console_ui)
        self.description = 'End program'

    def execute(self):
        self.console_ui.end_program()
