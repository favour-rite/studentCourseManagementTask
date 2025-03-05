def main():
    def get_choice(prompt):
        while True:
            choice = input(prompt)
            return choice

    while True:
        print("""\nWelcome to the STUDENT COURSE MANAGEMENT!
        1. Register
        2. Login
        3. Exit
        """)
        choice = get_choice("Enter your choice: ")
        match choice:
            case "1":
                print("""
        1. Are You Registering as student
        2. Are You Registering as Teacher
        3. Exit
                """)
                register_choice = get_choice("Enter your choice: ")
                match register_choice:
                    case "1":
                        s_name = input("Enter your name: ")
                        email = input("Enter your email: ")
                        set_password = input("Set Strong password: ")
                        print("""
                        1. View Notification
                        2. Register Course
                        3. View Grade
                        4. Exit""")
                        reg_s_choice = get_choice("Enter your choice: ")
                        match reg_s_choice:
                            case "1":
                                print("notification viewed")
                            case "2":
                                print("registered successfully")
                            case "3":
                                print("view grades already")
                            case "4":
                                print("Exiting...")
                                return
                            case _:
                                print("Invalid choice. Please try again.")
                    case "2":
                        t_name = input("Enter your name: ")
                        t_email = input("Enter your email: ")
                        set_t_password = input("Set Strong password: ")
                        print("""
                             1. create course
                             2. Assign Grades
                             3. Send Notification
                             4. Exit""")
                        reg_t_choice = get_choice("Enter your choice: ")
                        match reg_t_choice:
                            case "1":
                                print("create course successfully")
                            case "2":
                                print("Already Assign Grades")
                            case "3":
                                print("Notification sent successfully")
                            case "4":
                                print("Exiting...")
                                return
                            case _:
                                print("Invalid choice. Please try again.")
                    case "3":
                        print("Exiting...")
                        return
                    case _:
                        print("Invalid choice. Please try again.")
            case "2":
                print("""
                       1. Student
                       2. Teacher
                       3. Exit
                       """)
                login_choice = get_choice("Enter your choice: ")
                match login_choice:
                    case "1":
                        s_Email = input("Enter your Email: ")
                        s_Password = input("Enter your password: ")
                        print("Login successfully")
                        print("""
                               1. View Notification
                               2. Register Course
                               3. View Grade
                               4. Exit""")
                        Login_s_choice = get_choice("Enter your choice: ")
                        match Login_s_choice:
                            case "1":
                                print("notification viewed")
                            case "2":
                                print("registered successfully")
                            case "3":
                                print("view grades already")
                            case "4":
                                print("Exiting...")
                                return
                            case _:
                                print("Invalid choice. Please try again.")
                    case "2":
                        t_email = input("Enter your email: ")
                        unique_password = input("Enter teachers password: ")
                        set_t_password = input("Enter password: ")
                        print("""
                               1. create course
                               2. Assign Grades
                               3. Send Notification
                               4. Exit""")
                        Login_t_choice = get_choice("Enter your choice: ")
                        match Login_t_choice:
                            case "1":
                                print("create course successfully")
                            case "2":
                                print("Already Assign Grades")
                            case "3":
                                print("Notification sent successfully")
                            case "4":
                                print("Exiting...")
                                return
                            case _:
                                print("Invalid choice. Please try again.")
                    case "3":
                        print("Exiting...")
                        return
                    case _:
                        print("Invalid choice. Please try again.")
            case "3":
                print("Exiting...")
                return
            case _:
                print("Invalid choice. Please try again.")

print(main())