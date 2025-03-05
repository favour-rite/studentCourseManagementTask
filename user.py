from exceptions.exception import EmailAlreadyExistException


class user:
    def start(self, role):
        print("""
           Welcome! Please select your role.
           1. Facilitator
           2. Student
       """)
        role = input("Enter 'facilitator' or 'student': ").strip().lower()
        if role == 'facilitator':
            self.main_menu()
        elif role == 'student':
            self.main_menu()
        else:
            print("Invalid role! Please choose either 'facilitator' or 'student'.")
            self.start()


    def main_menu(self):
        print("""
           Welcome to Python Student Course
           1. -> Register
           2. -> Login
           3. -> Exit
       """)
    choice = input("Choose an option: ")
        if choice == '1':
            self.register()
        elif choice == '2':
            self.login()
        elif choice == '3':
            self.exit()
        else:
            print("Invalid choice, please select again.")
            self.main_menu()


    def login(self, last_name=None, first_name=None):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        print(f"User {first_name} {last_name} Logged in successfully. ")


    def register(self):
        try:
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            phone_number = input("Enter your phone number: ")
        except EmailAlreadyExistException:
            print("Email already registered, please try again.")
        except ValueError:
            print("Invalid input, please try again.")
        except
        print(f"User {first_name} {last_name} registered successfully.")
        self.main_menu()
