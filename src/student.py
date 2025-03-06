from exceptions.exception import NotFoundException, EmailAlreadyExistException, VerificationFailedException
from src.course import Course
from src.teacher import Teacher

class Student(Teacher):

    emails = set()

    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        super().validate_email(email)
        super().validate_name(name)
        super().validate_password(password)
        self.__courses = []
        self.__is_logged_in = False
        self.__teachers = []
        self.__students = []

    def register(self, new_name, new_email, new_password):
        super().validate_email(new_email)
        self.verify_email(new_email)
        super().validate_name(new_name)
        super().validate_password(new_password)
        super().register(new_name, new_email, new_password)

    def login(self, email, password):
        try:
            if super().login(email, password):
                self.__is_logged_in = True
                return True
            return False
        except VerificationFailedException:
            self.__is_logged_in = False
            return False

    def login_status(self):
        return self.__is_logged_in

    def add_course(self, new_course: Course):
        if not(isinstance(new_course, Course)):
            raise TypeError("new_course must be a Course.")
        for course in self.__courses:
            if course.title == new_course.title :
                raise NotFoundException("Course exit ")
        self.__courses.append(new_course)

    def view_courses(self) -> list:
        for course in self.__courses:
            return course

    def view_enrolled_courses(self) -> list:
        enrolled_courses = []
        for course in self.__courses:
            if course.enrolled_students:
                enrolled_courses.append(course)

        return enrolled_courses

    @staticmethod
    def verify_email(email):
        if email in Student.emails:
            raise EmailAlreadyExistException("Email already registered")
        Student.emails.add(email)

    @staticmethod
    def verify_name(name ):
        if not name in Student.validate_name(name):
            raise NotFoundException("Name doesnt exit ")




