from abc import ABC, abstractmethod


class Command(ABC):

    _description: str = None
    _console_ui = None

    def __init__(self, console_ui):
        self._console_ui = console_ui

    @property
    def console_ui(self):
        return self._console_ui

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    @abstractmethod
    def description(self, value: str):
        self._description = value

    @abstractmethod
    def execute(self):
        ...

    def get_description(self) -> str:
        return self._description
