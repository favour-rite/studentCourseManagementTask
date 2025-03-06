from exceptions.exception import *


class Course:

    def __init__(self, course_code: str, title: str):
        self.validate_course_code(course_code)
        self.validate_title(title)
        self.__course_code = course_code
        self.__title = title
        # self.__enrolled_students = []
        self.__grades = {}


    @property
    def course_code(self):
        return self.__course_code

    @course_code.setter
    def course_code(self, course_code):
        self.__course_code = course_code

    @property
    def title(self):
        return self.__title

    # @property
    # def enrolled_students(self):
    #     return self.__enrolled_students

    @title.setter
    def title(self, title):
        self.__title = title

    @staticmethod
    def validate_course_code(course_code: str):
        if not course_code:
            raise NullException("Course Code is required")
        if not isinstance(course_code, str) or len(course_code) < 3 or len(course_code) > 7 or not course_code.isalnum():
            raise InvalidCourseCodeException("Course code must between a 3 and 7 characters long")


    @staticmethod
    def validate_title(title):
        if not title:
            raise NullException("Fill the title field")
        if not isinstance(title, str) :
            raise InvalidCourseTitleException("title is not valid")

    # def add_student(self, student: str):
    #     if student in self.__enrolled_students:
    #         raise StudentAlreadyEnrolledException("Student is already enrolled in this course")
    #     self.__enrolled_students.append(student)
    #
    # def remove_student(self, student):
    #     if not student in self.__enrolled_students:
    #         raise CourseAlreadyRegisteredException("Course is already registered")
    #     self.__enrolled_students.remove(student)
    #
    # def number_of_enrolled_students(self):
    #     return len(self.__enrolled_students)

    def add_grade(self, student, grade):
        self.__grades[student] = grade

    def get_grade(self, student):
        return self.__grades.get(student)



    def __str__(self):
        return f"Course = {self.course_code}, Title =  {self.title}"

# def save_course_data(course, filename:str="course.pickle"):
#     with open(filename, "wb") as file:
#         pickle.dump(course, file)
#
# def load_course_data(filename="course.pickle"):
#     with open(filename, "rb") as file:
#         course = pickle.load(file)
#
# course = Course("291", "yoruba")
# save_course_data(course)
# load_course_data(filename="course.pickle")

