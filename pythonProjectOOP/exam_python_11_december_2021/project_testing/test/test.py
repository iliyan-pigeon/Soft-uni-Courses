from exam_python_11_december_2021.project import Team
from unittest import TestCase, main


class TestTeam(TestCase):

    def setUp(self):
        self.team = Team("abc")

    def test_correct_initialization(self):

        self.assertEqual("abc", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_initialization_with_invalid_name(self):

        with self.assertRaises(ValueError) as ve:
            self.team.name = "ab1"

        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

        self.assertEqual({}, self.team.members)

    def test_add_member_to_dictionary(self):
        members_to_add = {"Ivan": 18, "Georgi": 20, "Natasha": 30}

        self.assertEqual("Successfully added: Ivan, Georgi, Natasha", self.team.add_member(**members_to_add))
        self.assertEqual({"Ivan": 18, "Georgi": 20, "Natasha": 30}, self.team.members)

    def test_add_member_when_member_is_already_added(self):
        members_to_add = {"Ivan": 18, "Georgi": 20, "Natasha": 30}
        self.team.members["Georgi"] = 20

        self.assertEqual("Successfully added: Ivan, Natasha", self.team.add_member(**members_to_add))
        self.assertEqual({"Georgi": 20, "Ivan": 18, "Natasha": 30}, self.team.members)

    def test_remove_member_when_member_exist(self):
        self.team.members = {"Ivan": 18, "Georgi": 20, "Natasha": 30}

        self.assertEqual("Member Natasha removed", self.team.remove_member("Natasha"))
        self.assertEqual({"Ivan": 18, "Georgi": 20}, self.team.members)

    def test_remove_member_when_member_does_not_exist(self):
        self.team.members = {"Ivan": 18, "Georgi": 20, "Natasha": 30}

        self.assertEqual("Member with name Peter does not exist", self.team.remove_member("Peter"))
        self.assertEqual({"Ivan": 18, "Georgi": 20, "Natasha": 30}, self.team.members)

    def test_gt_magic_method_when_self_members_are_more(self):
        self.team.members = {"Ivan": 18, "Georgi": 20, "Natasha": 30}
        other = Team("cba")
        other.members = {"Georgi": 20, "Natasha": 30}

        self.assertEqual(True, self.team.__gt__(other))

    def test_gt_magic_method_when_other_members_are_more(self):
        self.team.members = {"Georgi": 20, "Natasha": 30}
        other = Team("cba")
        other.members = {"Ivan": 18, "Georgi": 20, "Natasha": 30}

        self.assertEqual(False, self.team.__gt__(other))

    def test_len_magic_method(self):
        self.team.members = {"Ivan": 18, "Georgi": 20, "Natasha": 30}

        self.assertEqual(3, len(self.team))

    def test_add_magic_method_merging_two_instances_into_one_new(self):
        self.team.members = {"Ivan": 20, "Georgi": 20, "Natasha": 30}
        other = Team("cba")
        other.members = {"Ivan": 18, "Marin": 38}
        new_team = self.team.__add__(other)

        self.assertEqual("Team name: abccba\nMember: Marin - 38-years old\n"
                         "Member: Natasha - 30-years old\n"
                         "Member: Georgi - 20-years old\n"
                         "Member: Ivan - 20-years old"
                         , str(new_team))
        self.assertEqual("abccba", new_team.name)
        self.assertEqual({"Ivan": 20, "Georgi": 20, "Natasha": 30, "Marin": 38}, new_team.members)

    def test_str_magic_method(self):
        self.team.members = {"Iliyan": 25, "Ivan": 20, "Georgi": 22, "Natasha": 30}

        self.assertEqual("Team name: abc\nMember: Natasha - 30-years old\n"
                         "Member: Iliyan - 25-years old\n"
                         "Member: Georgi - 22-years old\n"
                         "Member: Ivan - 20-years old", str(self.team))

    def test_str_magic_method_when_no_members(self):

        self.assertEqual("Team name: abc", str(self.team))


if __name__ == '__main__':
    main()
