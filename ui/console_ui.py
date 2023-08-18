import connector
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
            except ValueError as e:
                print(f'Incorrect input: no such entry found: {user_input}')

    def new_note(self):
        print("Creating new note")

    def edit_note(self):
        print("Edit note")

    def delete_note(self):
        print("Delete note")

    def save_to_file(self):
        print("Save to file")

    def load_from_file(self):
        print("Load from file")

    def change_working_file(self):
        print("Change working file")
        user_input = input("Please, enter file name: ")
        connector.con.file_handler.set_file_path(file_path=user_input)
        print(f'Working file has been changed to: "{connector.con.file_handler.get_file_path()}"\n')

    def end_program(self):
        print("Exiting program")
        self.working_flag = False
