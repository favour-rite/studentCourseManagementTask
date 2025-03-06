import unittest

from src.course import Course
from src.courses import Courses



class TestCourses(unittest.TestCase):

    def setUp(self):
        self.course1 = Course("computer123", "Computer Science")
        self.course2 = Course("MATH201", "Intergerated science")
        self.courses = Courses


    def test_add_course(self):
        self.courses.add_course(self.course1)
        self.assertEqual(len(self.courses.get_courses_list()), 1)
        self.courses.add_course(self.course2)
        self.assertEqual(len(self.courses.get_courses_list()), 2)

    def test_remove_course(self):
        self.courses.add_course(self.course1)
        self.courses.add_course(self.course2)
        self.courses.remove_course("social studies")
        self.assertEqual(len(self.courses.get_courses_list()), 1)
        self.courses.remove_course("Math")
        self.assertEqual(len(self.courses.get_courses_list()), 0)

    def test_remove_non_existing_course(self):
        self.courses.add_course(self.course1)
        with self.assertRaises(ValueError):
            self.courses.remove_course("chemistry")

    def test_display_courses(self):
        self.courses.add_course(self.course1)
        self.courses.add_course(self.course2)

    def test_get_course(self):
        self.courses.add_course(self.course1)
        course = self.courses.get_course("crs")
        self.assertEqual(course, self.course1,"course has been added")

    def test_get_non_existing_course(self):
        course = self.courses.get_course("arabic")
        self.assertIsNone(course)

    def test_str_courses(self):
        self.assertEqual(str(self.courses), "Courses: 0 courses available.")
        self.courses.add_course(self.course1)
        self.courses.add_course(self.course2)
        self.assertEqual(str(self.courses), "Courses: 2 courses available.")


if __name__ == "__main__":
    unittest.main()
