from ui.commands.command import Command


class NewNote(Command):

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    def __init__(self, console_ui):
        super().__init__(console_ui)
        self._description = 'Create new note'

    def execute(self):
        self.console_ui.new_note()

