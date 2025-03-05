from exceptions.exception import *


class Grade:

    MAXIMUM_GRADE = 100

    def __init__(self, first_ca, second_ca, exam):
        self.validate_ca(first_ca)
        self.validate_ca2(second_ca)
        self.validate_exam(exam)
        self.__first_ca = first_ca
        self.__second_ca = second_ca
        self.__exam = exam
        self.__total_grade = 0

    @property
    def first_ca(self):
        return self.__first_ca

    @first_ca.setter
    def first_ca(self, first_ca):
        self.__first_ca = first_ca

    @property
    def second_ca(self):
        return self.__second_ca

    @second_ca.setter
    def second_ca(self, second_ca):
        self.__second_ca = second_ca

    @property
    def exam(self):
        return self.__exam

    @exam.setter
    def exam(self, exam):
        self.__exam = exam


    def calculate_total_grade(self, first_ca:int, second_ca: int, exam: int) -> int:
        self.__total_grade = first_ca + second_ca + exam
        return self.__total_grade

    @staticmethod
    def validate_ca(first_ca):
        if not first_ca:
            raise NullException("This person is not serious")
        if not isinstance(first_ca, int) or first_ca > 20 or first_ca < 0:
            raise InvalidGradeException("You must be doing something wrong, check again")

    @staticmethod
    def validate_ca2(second_ca):
        if not second_ca:
            raise NullException("This person is not serious sha")
        if not isinstance(second_ca, int) or second_ca > 20 or second_ca < 0:
            raise InvalidGradeException("You must be doing something wrong, check again")

    @staticmethod
    def validate_exam(exam):
        if not exam:
            raise NullException("This person is not serious sha")
        if not isinstance(exam, int) or exam > 60 or exam < 0:
            raise InvalidGradeException("You must be doing something wrong with the grade, check again")



