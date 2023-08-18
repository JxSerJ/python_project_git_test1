from config import FILE_PATH
from file_handler.file_handler import FileHandler
from note import Note
from ui.console_ui import ConsoleUI


class Service:
    console_ui: ConsoleUI
    file_handler: FileHandler
    notes_list: list[Note]
    id: int = 0

    def __init__(self):
        self.console_ui: ConsoleUI = ConsoleUI()
        self.file_handler: FileHandler = FileHandler(FILE_PATH)
        self.notes_list = []

    def set_id(self):
        self.id = self.notes_list.__len__()

    def add_note(self, title: str, body: str):
        new_note: Note = Note(id=self.id, title=title, body=body)
        self.notes_list.append(new_note)
        self.set_id()

    def print_all_notes(self):
        if self.notes_list.__len__() == 0:
            print("No notes. Empty.")
        else:
            print('Show all notes in memory\n')
            for note in self.notes_list:
                print(note)
                # print(f"ID: {note.id}. {note.title}\n{note.body}")

    def delete_note(self):
        pass

    def save_to_file(self):
        print(self.file_handler.save_notes_to_file(notes=self.notes_list))


service = Service()
