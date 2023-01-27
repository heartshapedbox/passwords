import csv


class Passwords():
    def __init__(self):
        self.users_id_list = []
        self.users_pass_list = []
        self.numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        self.special_symbols = ["!", "@", "#", "%",
                                "$", "^", "&", "*", "?", "-", "_", ".", "~"]

    def show_header(self):
        underscore = ""
        for i in range(0, 15):
            underscore += "_"
        print(f"\n{underscore}MENU:{underscore}\n\n1. CREATE A NEW USER ID\n2. CHANGE A PASSWORD\n3. DISPLAY ALL USERS ID\n4. QUIT\n")

    def check_pass(self, new_user_pass_input):
        check_num_list, check_sp_char_list = [], []
        for i in new_user_pass_input:
            if i not in self.numbers and i not in self.special_symbols:
                check_num_list.append("False")
                check_sp_char_list.append("False")
            elif i in self.numbers:
                check_num_list.append("True")
            else:
                check_sp_char_list.append("True")

        if "True" not in check_num_list:
            print("YOUR PASSWORD SHOULD INCLUDE NUMBERS! TRY AGAIN!")
            self.create_pass()
        elif "True" not in check_sp_char_list:
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

    def change_user_pass(self):
        self.user_id_index, self.user_pass_index = 0, 0
        self.user_id_check = input("ENTER YOUR USER ID: ")
        if self.user_id_check not in self.users_id_list:
            print("USER ID WRONG!")
        else:
            self.user_pass_check = input("ENTER YOUR PASSWORD: ")
            if self.user_pass_check not in self.users_pass_list:
                print("PASSWORD WRONG!")
            else:
                self.user_id_index = self.users_id_list.index(
                    self.user_id_check)
                self.user_pass_index = self.users_pass_list.index(
                    self.user_pass_check)
                if self.user_id_index == self.user_pass_index:
                    self.create_pass()
                    self.users_id_list.remove(self.user_id_check)
                    self.users_pass_list.remove(self.user_pass_check)
                    self.users_id_list.append(self.user_id_check)
                    print("DONE! PASSWORD CHANGED!")
                else:
                    print("PASSWORD WRONG!")

    def display_all_users_id(self):
        print("\nALL USERS ID LIST:")
        for i in range(0, len(self.users_id_list)):
            print(f"{i+1}. {self.users_id_list[i]}")

    def quit_menu(self):
        print("PROGRAM CLOSED!")

    def main(self):
        in_main_menu = True
        while in_main_menu == True:
            self.show_header()
            option = input("SELECT AN OPTION: ")
            if option == "1":
                self.create_new_user_id()
            elif option == "2":
                self.change_user_pass()
            elif option == "3":
                self.display_all_users_id()
            elif option == "4":
                self.quit_menu()
                in_main_menu = False
            else:
                print("WRONG OPTION! TRY AGAIN!")


if __name__ == "__main__":
    Passwords().main()
