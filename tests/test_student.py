import unittest

from exceptions.exception import EmailAlreadyExistException
from src.course import Course
from src.student import Student
from src.teacher import Teacher


class MyStudentTestCase(unittest.TestCase):
    def test_that_student_can_register_and_in_with_email_password_and_name(self):
        student = Student("favour Igwe", "abimbolaabishat@gmail.com", "password")
        student.register("favour Ike", "Favourites@gmail.com", "password")

    def test_that_student_can_register_and_login(self):
        student = Student("favour Igwe", "abimbolaabishat@gmail.com", "password")
        student.register("favour Ike", "Favourites@gmail.com", "password1")
        login = student.login("Favourites@gmail.com", "password1")
        self.assertTrue(login)
        self.assertTrue(student.login_status())

    def test_for_duplicate_email(self):
        student = Student("favour Igwe", "abimbolaabishat@gmail.com", "password")
        student.register("favour Ike", "Favourites@gmail.com", "password1")
        with self.assertRaises(EmailAlreadyExistException):
            student.register("favour hume", "Favourites@gmail.com", "password1")
        login = student.login("Favourites@gmail.com", "password1")
        self.assertTrue(login)
        self.assertTrue(student.login_status())


    def test_that_student_can_add_course(self):
        student = Student("favour Igwe", "abimbolaabishat@gmail.com", "password")
        student_one = student.register("favour Ike", "Favourites@gmail.com", "password1")
        login = student.login("Favourites@gmail.com", "password1")
        self.assertTrue(login)
        self.assertTrue(student.login_status())

        student_one_course = student_one.add_course("MATH201")

        self.assertEqual(student_one_course, student_one.)




