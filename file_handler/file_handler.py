import datetime
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
        try:
            with open(file=self.get_file_path(), mode="w", encoding="UTF-8") as file:
                data = notes
                json.dump(obj=data, cls=NoteSerializer, fp=file, indent=4)
                print("Data written to file.")
                return True
        except Exception as e:
            print(f"Error: {e.__traceback__}")
            return False

    def load_notes_from_file(self) -> (list[Note], bool):
        result_list: list[Note] = []
        try:
            with open(file=self.get_file_path(), mode="r", encoding="UTF-8") as file:
                loaded_data: list[dict] = json.load(fp=file)
                result_list = [Note(id=data_entry['id'], title=data_entry['title'], body=data_entry['body'],
                                    date_created=datetime.datetime.fromisoformat(data_entry['date_created']),
                                    date_modified=datetime.datetime.fromisoformat(data_entry['date_modified']))
                               for data_entry in loaded_data]
                return result_list, True
        except Exception as e:
            print(f"Error: {e.__traceback__}")
            return result_list, False

    def set_file_path(self, file_path: str) -> str:
        self._file_path = file_path
        return self._file_path

    def get_file_path(self):
        return self._file_path
