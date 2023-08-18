from ui.commands.command import Command


class ShowAllNotes(Command):
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    def __init__(self, console_ui):
        super().__init__(console_ui)
        self.description = 'Show all notes'

    def execute(self):
        self.console_ui.show_all_notes()
