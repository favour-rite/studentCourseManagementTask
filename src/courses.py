from src.course import Course


class Courses:


    def __init__(self):
        self._courses_list = []

    @classmethod
    def add_course(self, course: Course):
        if isinstance(course, Course):
            self._courses_list.append(course)
        else:
            raise ValueError("You can only add instances of the Course class.")

    @classmethod
    def get_courses_list(self):
        return self._courses_list

    @classmethod
    def remove_course(self, course_code: str):
        course_to_remove = next((course for course in self.__courses_list if course.course_code == course_code),
                                        None)
        if course_to_remove:
            self.__courses_list.remove(course_to_remove)
        else:
            raise ValueError(f"No course found with code {course_code}")

    @classmethod
    def get_course(self, course_code: str):
        for course in self.courses_list:
            if course.course_code == course_code:
                return course
        else:
            raise ValueError(f"No course found with code {course_code}")


#     if self.__courses_list:
    #         for course in self.__courses_list:
    #             print(course)
    #     else:
    #         print("No courses available.")
    #

    # def get_courses_list(self):
    #     return self.__courses_list
    # def __str__(self):
    #         return f"Courses: {len(self.__courses_list)} courses available."


