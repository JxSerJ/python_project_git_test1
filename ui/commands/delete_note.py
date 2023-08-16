from ui.commands.command import Command


class DeleteNote(Command):
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    def __init__(self, console_ui):
        super().__init__(console_ui)
        self.description = 'Delete note'

    def execute(self):
        self.console_ui.delete_note()
