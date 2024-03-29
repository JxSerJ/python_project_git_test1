import datetime

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

    def update_id(self):
        id_max: int = 0
        for note in self.notes_list:
            if note.id > id_max:
                id_max = note.id
        self.id = id_max + 1

    def add_note(self, title: str, body: str):
        new_note: Note = Note(id=self.id, title=title, body=body)
        self.notes_list.append(new_note)
        self.id += 1

    def edit_note(self, note_id: int, title: str, body: str):
        note = self.notes_list[note_id]
        note.update_data(title=title, body=body)

    def check_id(self, note_id: int) -> bool:
        for note in self.notes_list:
            if note.id == note_id:
                return True
        return False

    def get_note_by_id(self, note_id) -> Note:
        for i in range(self.notes_list.__len__()):
            if self.notes_list[i].id == note_id:
                return self.notes_list[i]

    def get_note_info_by_id(self, note_id: int):
        return self.notes_list[note_id].short_info()

    def print_all_notes_short(self):
        if self.notes_list.__len__() == 0:
            print("No notes. Empty.")
        else:
            print('Show all notes in memory\n')
            for note in self.notes_list:
                print(note.short_info())

    def print_all_notes(self):
        if self.notes_list.__len__() == 0:
            print("No notes. Empty.")
        else:
            print('Show all notes in memory\n')
            for note in self.notes_list:
                print(note)
                # print(f"ID: {note.id}. {note.title}\n{note.body}")

    def delete_note(self, note_id: int) -> bool:
        for i in range(self.notes_list.__len__()):
            if self.notes_list[i].id == note_id:
                self.notes_list.pop(i)
                self.update_id()
                return True
        return False

    def save_to_file(self):
        print(f"Trying to save current data to file: {self.file_handler.get_file_path()}")
        result: bool = self.file_handler.save_notes_to_file(notes=self.notes_list)
        print("Save successful") if result else print("Data not saved")

    def load_from_file(self):
        print(f"Trying to load data to file: {self.file_handler.get_file_path()}")
        self.notes_list, result = self.file_handler.load_notes_from_file()
        self.update_id()
        print("Data loaded successful") if result else print("Data not loaded")
        print("test string2")


service = Service()
