from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class TestStudentReportCard(TestCase):

    def setUp(self):
        self.card = StudentReportCard("Ivan", 3)

    def test_initialization_if_all_inputs_are_valid(self):

        self.assertEqual("Ivan", self.card.student_name)
        self.assertEqual(3, self.card.school_year)
        self.assertEqual({}, self.card.grades_by_subject)

    def test_initialization_when_student_name_is_empty_string(self):

        with self.assertRaises(ValueError) as ve:
            self.card = StudentReportCard("", 3)

        self.assertEqual("Student Name cannot be an empty string!", str(ve.exception))

    def test_initialization_when_school_year_is_above_max(self):

        with self.assertRaises(ValueError) as ve:
            self.card = StudentReportCard("Ivan", 13)

        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_initialization_when_school_year_is_below_min(self):

        with self.assertRaises(ValueError) as ve:
            self.card = StudentReportCard("Ivan", 0)

        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_add_grade_when_subject_does_not_exist(self):
        self.card.add_grade("Math", 6)

        self.assertEqual({"Math": [6]}, self.card.grades_by_subject)

    def test_add_grade_when_subject_exist(self):
        self.card.grades_by_subject["Math"] = [4]
        self.card.add_grade("Math", 6)

        self.assertEqual({"Math": [4, 6]}, self.card.grades_by_subject)

    def test_average_grade_by_subject(self):
        self.card.grades_by_subject["Math"] = [4, 6]
        self.card.grades_by_subject["Biology"] = [4, 6]

        self.assertEqual("Math: 5.00\nBiology: 5.00", self.card.average_grade_by_subject())

    def test_average_grade_for_all_subjects(self):
        self.card.grades_by_subject["Math"] = [4, 6]
        self.card.grades_by_subject["Biology"] = [4, 6]

        self.assertEqual("Average Grade: 5.00", self.card.average_grade_for_all_subjects())

    def test_repr_method(self):
        self.card.grades_by_subject["Math"] = [4, 6]
        self.card.grades_by_subject["Biology"] = [4, 6]

        self.assertEqual("Name: Ivan\n"
                         "Year: 3\n"
                         "----------\n"
                         "Math: 5.00\n"
                         "Biology: 5.00\n"
                         "----------\n"
                         "Average Grade: 5.00", self.card.__repr__())


if __name__ == '__main__':
    main()