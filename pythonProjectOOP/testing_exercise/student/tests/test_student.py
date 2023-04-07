from unittest import TestCase, main
from testing_exercise.student.project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student = Student("student")
        self.student_with_course = Student("student", {"Python": ["python_notes"]})

    def test_correct_initialization(self):

        self.assertEqual("student", self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({"Python": ["python_notes"]}, self.student_with_course.courses)

    def test_enroll_when_course_already_in_the_dictionary(self):

        self.assertEqual("Course already added. Notes have been updated.", self.student_with_course.enroll("Python", ["a", "b"]))
        self.assertEqual({"Python": ["python_notes", "a", "b"]}, self.student_with_course.courses)

    def test_enroll_when_course_does_not_exist_and_notes_should_be_added(self):

        self.assertEqual("Course and course notes have been added.", self.student.enroll("name", ["a", "b"], "Y"))
        self.assertEqual({"name": ["a", "b"]}, self.student.courses)

        self.student.courses = {}

        self.assertEqual("Course and course notes have been added.", self.student.enroll("name", ["a", "b"]))
        self.assertEqual({"name": ["a", "b"]}, self.student.courses)

    def test_enroll_when_course_does_not_exist_and_notes_should_not_be_added(self):

        self.assertEqual("Course has been added.", self.student.enroll("name", ["a", "b"], "N"))
        self.assertEqual({"name": []}, self.student.courses)

    def test_add_notes_when_course_does_not_exist(self):

        with self.assertRaises(Exception) as ex:
            self.student.add_notes("name", ["a", "b"])

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_when_course_exist(self):

        self.assertEqual("Notes have been updated", self.student_with_course.add_notes("Python", ["a", "b"]))
        self.assertEqual({"Python": ["python_notes", ["a", "b"]]}, self.student_with_course.courses)

    def test_leave_if_course_does_not_exist(self):

        with self.assertRaises(Exception) as ex:
            self.student.leave_course("name")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_if_course_does_exist(self):

        self.assertEqual("Course has been removed", self.student_with_course.leave_course("Python"))
        self.assertEqual({}, self.student_with_course.courses)


if __name__ == '__main__':
    main()
