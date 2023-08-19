import json
from typing import Any

from note import Note


class NoteSerializer(json.JSONEncoder):
    def default(self, o: Note) -> Any:
        o.date_created = o.date_created.isoformat()
        o.date_modified = o.date_modified.isoformat()
        return o.__dict__


class FileHandler:
    _file_path: str
    note_instance: Note

    def __init__(self, file_path):
        self._file_path = file_path

    def save_notes_to_file(self, notes: list[Note]) -> bool:
        with open(file=self.get_file_path(), mode="w", encoding="UTF-8") as file:
            data = notes
            json.dump(obj=data, cls=NoteSerializer, fp=file, indent=4)
            print("Data written to file.")
        return True

    def load_notes_from_file(self) -> list[Note]:
        result_list: list[Note] = []
        with open(file=self.get_file_path(), mode="r", encoding="UTF-8") as file:
            result_list = json.load(obj=result_list, fp=file)
        return result_list

    def set_file_path(self, file_path: str) -> str:
        self._file_path = file_path
        return self._file_path

    def get_file_path(self):
        return self._file_path
