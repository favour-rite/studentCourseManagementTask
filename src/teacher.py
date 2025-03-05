from .grade import Grade
from .course import Course
import re
from exceptions.exception import *
import bcrypt

class Teacher:

    def __init__(self, name, email, password):
        self.__email = email
        self.__password = password
        self.__name = name
        self.students = []
        self.__courses = { }
        self.teachers = []
        self.__logged_in = False


    def login_status(self):
        return self.__logged_in

    @property
    def email(self):
        return self.__email

    @property
    def course(self):
        return self.__courses

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @staticmethod
    def hash_password(password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    @staticmethod
    def validate_email(email):
        if not email or not email.strip():
            raise NullException("Fields cannot be empty.")
        email_pattern = r'[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+'

        if not re.match(email_pattern, email):
            raise InvalidEmailPatternException("Invalid email address.")

        with open("teacher_details", 'r') as file:
            for line in file:
                stored_email, stored_password = line.split(':')
                if stored_email == email:
                    return bcrypt.hashpw(stored_password.encode('utf-8'), stored_password.encode('utf-8'))

    @staticmethod
    def validate_name(name):
        if not name:
            raise NullException("Fields cannot be empty.")

        names = name.split(':')

        if len(names) < 2:
            raise InvalidNameLengthException("First name and last name is required.")

        for every_char in names:
            if not every_char.isalpha():
                raise InvalidNameException("Name must contain only alphabetic character.")
            
    @staticmethod
    def validate_password(password):
        if len(password) < 5:
            raise InvalidPasswordLengthException("Password must be at least 5 characters.")
        return bcrypt.checkpw(password.encode('utf-8'), bcrypt.gensalt())


    def register(self, name: str, email: str, password:str):
        self.validate_email(email)
        self.validate_name(name)
        self.validate_password(password)
        details = name, email, password
        self.teachers.append(details)

    def create_course(self, course_code: str, course_title: str):

        if self.__logged_in == False:
            raise VerificationFailedException("You are not logged in.")
        course = Course(course_code, course_title)
        self.__courses.append(course)
        return course

    def login(self, email: str, password: str) -> bool:
        self.validate_email(email)
        self.validate_password(password)
        for each_detail in self.teachers:
            if each_detail[1] == email and each_detail[2] == password:
                self.__logged_in = True
                return True

        raise InvalidDetailsException("Invalid details.")

    def number_of_courses_created(self) -> int:
        return len(self.__courses)

    def number_of_teachers(self) -> int:
        return len(self.teachers)

    def get_number_of_students_in_course(self, course) -> int:
        if course in self.__courses:
            return course.number_of_enrolled_students()

        raise NotFoundException("Course does not exist.")

    def assign_grade(self, course, student: str, first_ca: int, second_ca: int, exam: int):
        if course not in self.__courses:
            raise Exception("Course not taught by this teacher")
        grade = Grade(first_ca, second_ca, exam)
        course.add_grade(student, grade)
        return grade

    @staticmethod
    def save_to_file(name, email, password):
        with open('teacher_details', 'a') as file:
            file.write(f"{name}:{email}:{password}\n")


















