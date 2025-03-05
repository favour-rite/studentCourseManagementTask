import unittest
from src.teacher import Teacher
from exceptions.exception import *


class MyTeacherTestCase(unittest.TestCase):

    def setUp(self):
        self.teacher = Teacher("Firstname lastName", "email@gmail.com", "passw")

    def test_that_two_teachers_can_register_with_valid_details(self):
        self.teacher.register("Dr Favour", "FavourIgwe12@gmail.com", "password")
        self.assertEqual(1, self.teacher.number_of_teachers())
        self.teacher.register("Dr Hamid", "HamidAbari@gmail.com", "password1")
        self.assertEqual(2, self.teacher.number_of_teachers())

    def test_that_a_teacher_cannot_register_with_empty_name_field(self):
        with self.assertRaises(NullException):
            self.teacher.register("", "FavourIgwe@gmail.com", "password")

    def test_that_a_teacher_cannot_register_with_special_characters_present_in_name(self):
        with self.assertRaises(InvalidNameException):
            self.teacher.register("Dr$$$ Favour", "FavourIgwe@gmail.com", "password")

    def test_that_a_teacher_cannot_register_with_first_name_or_last_name_only_name_field(self):
        with self.assertRaises(InvalidNameLengthException):
            self.teacher.register("Dr", "FavourIgwe@gmail.com", "password")

    def test_that_a_teacher_cannot_register_with_empty_email_field(self):
        with self.assertRaises(NullException):
            self.teacher.register("Dr Favour", "", "password")

    def test_that_a_teacher_cannot_register_with_empty_password_field(self):
        with self.assertRaises(NullException and InvalidPasswordLengthException):
            self.teacher.register("Dr Favour", "FavourIgwe@gmail.com", "")

    def test_that_a_teacher_cannot_register_with_invalid_email_pattern(self):
        with self.assertRaises(InvalidEmailPatternException):
            self.teacher.register("Dr Favour", "@FavourIgwe@gmail.com", "password")

    def test_that_a_teacher_cannot_register_with_incomplete_password_length(self):
        with self.assertRaises(InvalidPasswordLengthException):
            self.teacher.register("Dr Favour", "FavourIgwe@gmail.com", "pass")

    def test_that_teacher_login_with_correct_details(self):
        self.teacher.register("Dr Favour", "FavourIgwe@gmail.com", "password")
        login = self.teacher.login("FavourIgwe@gmail.com", "password")
        self.assertTrue(login)

    def test_that_a_teacher_can_create_course(self):
        self.teacher.register("Dr Favour", "FavourIgwe@gmail.com", "password")
        self.assertFalse(self.teacher.login_status())
        login = self.teacher.login("FavourIgwe@gmail.com", "password")
        self.assertTrue(login)
        self.teacher.create_course("201", "English")
        self.assertEqual(1, self.teacher.number_of_courses_created())
        self.teacher.create_course("202", "Maths")
        self.assertEqual(2, self.teacher.number_of_courses_created())

    def test_check_amount_of_students_no_courses(self):
        self.teacher.register("Dr Favour", "FavourIgwe@gmail.com", "password")
        self.assertFalse(self.teacher.login_status())
        login = self.teacher.login("FavourIgwe@gmail.com", "password")
        self.assertTrue(login)
        with self.assertRaises(NullException):
            course_one = self.teacher.create_course("", "")

            self.assertEqual(self.teacher.get_number_of_students_in_course(course_one), 0)

    def test_that_teacher_can_see_the_amount_of_students_enrolled_for_a_course(self):
        self.teacher.register("Dr Favour", "FavourIgwe@gmail.com", "password")
        self.assertFalse(self.teacher.login_status())
        login = self.teacher.login("FavourIgwe@gmail.com", "password")
        self.assertTrue(login)

        course_one = self.teacher.create_course("201", "English")
        course_two = self.teacher.create_course("202", "Yoruba")

        course_one.add_student("niyi")
        self.assertEqual(self.teacher.get_number_of_students_in_course(course_one), 1)
        course_one.add_student("Bibi")
        self.assertEqual(self.teacher.get_number_of_students_in_course(course_one), 2)

        course_two.add_student("Titi")
        self.assertEqual(self.teacher.get_number_of_students_in_course(course_two), 1)

    def test_check_amount_of_students_enrolled_in_multiple_courses(self):
        self.teacher.register("Dr Favour", "FavourIgwe@gmail.com", "password")
        self.assertFalse(self.teacher.login_status())
        login = self.teacher.login("FavourIgwe@gmail.com", "password")
        self.assertTrue(login)

        course_one = self.teacher.create_course("101", "Computer Science")
        course_one.add_student("niyi")
        course_one.students = ["niyi"]
        course_one.add_student("Bibi")
        self.assertEqual(self.teacher.get_number_of_students_in_course(course_one), 2)
        course_one.add_student("Titi")
        course_one.students = ["niyi", "Bibi", "Titi"]
        self.assertEqual(self.teacher.get_number_of_students_in_course(course_one), 3)

        course_two = self.teacher.create_course("Math121", "Matrix")
        course_two.add_student("Favour")
        course_two.students = ["Favour"]
        course_two.add_student("Ire")
        self.assertEqual(self.teacher.get_number_of_students_in_course(course_two), 2)
        course_two.add_student("Titi")
        course_two.add_student("Bayo")
        course_two.students = ["Favour", "Ire", "Titi", "Bayo"]
        self.assertEqual(self.teacher.get_number_of_students_in_course(course_one), 3)
        self.assertEqual(self.teacher.get_number_of_students_in_course(course_two), 4)

    def test_teacher_can_assign_grades_to_student_for_a_course(self):
        self.teacher.register("Dr Favour", "FavourIgwe@gmail.c om", "password")
        self.assertFalse(self.teacher.login_status())
        login = self.teacher.login("FavourIgwe@gmail.com", "password")
        self.assertTrue(login)

        course_one = self.teacher.create_course("201", "English")

        course_one.add_student("niyi")
        grade = self.teacher.assign_grade(course_one, "niyi", 15, 16, 45)
        self.assertEqual(course_one.get_grade("niyi"), grade)

    def test_teacher_can_assign_grades_to_student_for_multiple_courses(self):
        self.teacher.register("Dr Favour", "FavourIgwe@gmail.com", "password")
        self.assertFalse(self.teacher.login_status())
        login = self.teacher.login("FavourIgwe@gmail.com", "password")
        self.assertTrue(login)

        course_one = self.teacher.create_course("ENG201", "English")
        course_two = self.teacher.create_course("YOR202", "Yoruba")
        course_three = self.teacher.create_course("CMS203", "Computer Science")

        course_one.add_student("niyi")
        grade = self.teacher.assign_grade(course_one, "niyi", 15, 16, 45)
        self.assertEqual(course_one.get_grade("niyi"), grade)

        course_two.add_student("Titi")
        course_two.add_student("Bibi")
        grade_two = self.teacher.assign_grade(course_two, "Titi", 15, 16, 45)
        grade_two_student_two = self.teacher.assign_grade(course_two, "Bibi", 1, 12, 35)
        self.assertEqual(course_two.get_grade("Titi"), grade_two)
        self.assertEqual(course_two.get_grade("Bibi"), grade_two_student_two)



