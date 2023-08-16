from ui.commands.command import Command


class SaveToFile(Command):
    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    def __init__(self, console_ui):
        super().__init__(console_ui)
        self.description = 'Save to file'

    def execute(self):
        self.console_ui.save_to_file()
