import csv
import os
os.chdir("C:\\Users\\Dima\\Documents\\GitHub\\passwords\\")


class Passwords():
    def __init__(self):
        self.users_id_list, self.users_pass_list = [], []
        self.numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        self.special_characters = ["!", "@", "#", "%",
                                   "$", "^", "&", "*", "?", "-", "_", ".", "~"]

    def open_csv_file(self):
        with open("users_id_database.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) > 0:
                    user_data = "".join(str(i) for i in row)
                    user_id = user_data.split(": ")[0]
                    self.users_id_list.append(user_id)
                    user_pass = user_data.split(": ")[1]
                    self.users_pass_list.append(user_pass)

    def write_csv_file(self):
        with open("users_id_database.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for i in range(0, len(self.users_id_list)):
                user_data = f"{self.users_id_list[i]}: {self.users_pass_list[i]}"
                writer.writerow([user_data])

    def show_header(self):
        underline = ""
        for i in range(0, 15):
            underline += "_"
        print(f"\n{underline}MENU:{underline}\n\n1. CREATE A NEW USER ID\n2. CHANGE A PASSWORD\n3. DISPLAY USERS ID DATABASE\n4. QUIT\n")

    def check_pass(self, new_user_pass_input):
        check_numbers_list, check_special_characters_list = [], []
        for i in new_user_pass_input:
            if i not in self.numbers and i not in self.special_characters:
                check_numbers_list.append("False")
                check_special_characters_list.append("False")
            elif i in self.numbers:
                check_numbers_list.append("True")
            else:
                check_special_characters_list.append("True")

        if "True" not in check_numbers_list:
            print("YOUR PASSWORD SHOULD INCLUDE NUMBERS! TRY AGAIN!")
            self.create_pass()
        elif "True" not in check_special_characters_list:
            print("YOUR PASSWORD SHOULD INCLUDE SPECIAL CHARACTERS! TRY AGAIN!")
            self.create_pass()
        else:
            self.users_pass_list.append(new_user_pass_input)
            print("YOUR PASSWORD IS GOOD! PASSWORD CREATED!")

    def create_pass(self):
        pass_is_created = False
        while pass_is_created == False:
            new_user_pass_input = input(
                'ENTER A PASSWORD (MIN. LENGTH: 8 CHARACTERS. NUMBERS AND SPECIAL SYMBOLS\n"!", "@", "#", "%", "$", "^", "&", "*", "?", "-", "_", ".", "~" ARE MANDATORY.): ')
            if len(new_user_pass_input) < 8:
                print("PASSWORD LENGTH IS SHORT! TRY AGAIN!")
            elif new_user_pass_input in self.users_pass_list:
                print("THE PASSWORD ALREADY EXISTS! TRY AGAIN!")
            else:
                self.check_pass(new_user_pass_input)
                pass_is_created = True

    def create_new_user_id(self):
        new_user = False
        while new_user == False:
            new_user_id_input = input("ENTER A NEW USER ID: ")
            if new_user_id_input in self.users_id_list:
                print("THE USER ID ALREADY EXISTS! TRY AGAIN!")
            else:
                self.users_id_list.append(new_user_id_input)
                new_user = True
                self.create_pass()
                self.write_csv_file()

    def change_user_pass(self):
        self.user_id_index, self.user_pass_index = 0, 0
        self.user_id_input_check = input("ENTER YOUR USER ID: ")
        if self.user_id_input_check not in self.users_id_list:
            print("USER ID WRONG!")
        else:
            self.user_pass_input_check = input("ENTER YOUR PASSWORD: ")
            if self.user_pass_input_check not in self.users_pass_list:
                print("PASSWORD WRONG!")
            else:
                self.user_id_index = self.users_id_list.index(
                    self.user_id_input_check)
                self.user_pass_index = self.users_pass_list.index(
                    self.user_pass_input_check)
                if self.user_id_index == self.user_pass_index:
                    self.create_pass()
                    self.users_id_list.remove(self.user_id_input_check)
                    self.users_pass_list.remove(self.user_pass_input_check)
                    self.users_id_list.append(self.user_id_input_check)
                    self.write_csv_file()
                else:
                    print("PASSWORD WRONG!")

    def show_users_id_database(self):
        if len(self.users_id_list) > 0:
            print("\nUSERS ID DATABASE:")
            for i in range(0, len(self.users_id_list)):
                print(f"{i+1}. {self.users_id_list[i]}")
        else:
            print("DATABASE IS EMPTY!")

    def quit_menu(self):
        print("DATABASE CLOSED!")

    def show_main_menu(self):
        self.open_csv_file()
        in_main_menu = True
        while in_main_menu == True:
            self.show_header()
            option = input("SELECT AN OPTION: ")
            if option == "1":
                self.create_new_user_id()
            elif option == "2":
                self.change_user_pass()
            elif option == "3":
                self.show_users_id_database()
            elif option == "4":
                self.quit_menu()
                in_main_menu = False
            else:
                print("WRONG OPTION! TRY AGAIN!")


if __name__ == "__main__":
    Passwords().show_main_menu()
