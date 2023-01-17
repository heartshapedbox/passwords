import csv


class Passwords():
    def __init__(self):
        self.users_id_list = []
        self.users_pass_list = []
    
    
    def show_header(self):
        underscore = ""
        for i in range(0, 15):
            underscore += "_"
        print(f"\n{underscore}MENU:{underscore}\n\n1. CREATE A NEW USER ID\n2. CHANGE A PASSWORD\n3. DISPLAY ALL USERS ID\n4. QUIT\n")
    
    
    def create_pass(self):
        pass
    
    
    def check_pass(self):
        new_pass = False
        while new_pass == False:
            new_user_pass_input = input("USER CREATED! ENTER A PASSWORD: ")
            self.create_pass()
            if new_user_pass_input in self.users_pass_list:
                print("THE PASSWORD ALREADY EXISTS! TRY AGAIN!")
            else:
                self.users_pass_list.append(new_user_pass_input)
                new_pass = True
                print("PASSWORD CREATED!")
    
    
    def create_new_user_id(self):
        new_user = False
        while new_user == False:
            new_user_id_input = input("ENTER A NEW USER ID: ")
            if new_user_id_input in self.users_id_list:
                print("THE USER ID ALREADY EXISTS! TRY AGAIN!")
            else:
                self.users_id_list.append(new_user_id_input)
                new_user = True
                self.check_pass()
                
        print(self.users_id_list)
        print(self.users_pass_list)
    
    
    def change_user_pass(self):
        pass
    
    
    def display_all_users_id(self):
        pass
    
    
    def quit_menu(self):
        pass
    
    
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