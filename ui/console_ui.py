import service
from ui.menu import MainMenu


class ConsoleUI:
    working_flag: bool
    menu: MainMenu

    def __init__(self):
        self.working_flag = True
        self.menu = MainMenu(console_ui=self)

    def start_program(self):
        while self.working_flag:
            print(self.menu.form_menu())
            user_input = input("Choose menu entry: ")
            try:
                user_input = int(user_input)
                if user_input > self.menu.get_menu_size():
                    raise ValueError(f"There is no such menu entry. Max entry num is {self.menu.get_menu_size()}")
                else:
                    print('\n')
                    self.menu.execute(user_input)
                    print('\n')
            except ValueError as e:
                print(f'Incorrect input: no such entry found: {user_input}')

    def show_all_notes(self):
        service.service.print_all_notes()

    def new_note(self):
        print("Creating new note")
        title: str = input("Enter note title: ")
        body: str = input("Enter note body: ")
        print(f"You're gonna create note:\nTitle: {title}\nBody: {body}\nConfirm? y/n")
        user_input = input()
        if user_input == 'y':
            service.service.add_note(title=title, body=body)
            print("Note created")
        else:
            print("Creation cancelled")

    def edit_note(self):
        print("Edit note")
        service.service.print_all_notes_short()
        if service.service.notes_list.__len__() == 0:
            print("Canceling operation")
        else:
            try:
                note_id = int(input("Select ID of the note: "))
                if note_id is None:
                    print("No input. Canceling operation.")
                elif service.service.check_id(note_id):
                    title = input("Input new title: ")
                    body = input("Input new note body: ")
                    service.service.edit_note(note_id=note_id, title=title, body=body)
                    print(f"Note changed:\n"
                          f"{service.service.get_note_by_id(note_id=note_id).__str__()}")
                else:
                    print("No such note ID found")
            except Exception as e:
                print(f"Incorrect input: {str(e)}")

    def delete_note(self):
        print("Delete note")
        service.service.print_all_notes_short()
        if not service.service.notes_list.__len__() == 0:
            try:
                note_id = int(input("Select ID of the note: "))
                if note_id is None:
                    print("No input. Canceling operation.")
                elif service.service.check_id(note_id):
                    service.service.get_note_info_by_id(note_id=note_id)
                    user_input = input("Confirm deletion? y/n: ")
                    if user_input == "y":
                        service.service.delete_note(note_id=note_id)
                else:
                    print("No such note ID found")
            except Exception as e:
                print(f"Incorrect input: {str(e)}")
        else:
            print("Canceling operation")

    def save_to_file(self):
        service.service.save_to_file()

    def load_from_file(self):
        service.service.load_from_file()

    def change_working_file(self):
        print("Change working file")
        print(f"Current working file: {service.service.file_handler.get_file_path()}")
        user_input = input("Please, enter file name: ")
        if user_input:
            service.service.file_handler.set_file_path(file_path=user_input)
            print(f'Working file has been changed to: "{service.service.file_handler.get_file_path()}"\n')
        else:
            print("No input. Canceling operation.")

    def end_program(self):
        print("Exiting program")
        self.working_flag = False
