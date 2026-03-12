import unittest

from robot_core import RobotWorld


class TestRobotScent(unittest.TestCase):
    def setUp(self):
        self.world = RobotWorld(width=5, height=3)

    def test_first_lost_robot_leaves_scent(self):
        robot = self.world.spawn_robot(3, 3, "N")
        self.world.execute_command(robot, "F")
        self.assertIn((3, 3, "N"), self.world.scent)

    def test_second_robot_ignores_dangerous_forward_when_scent_exists(self):
        first = self.world.spawn_robot(3, 3, "N")
        self.world.execute_command(first, "F")

        second = self.world.spawn_robot(3, 3, "N")
        self.world.execute_command(second, "F")

        self.assertFalse(second.lost)
        self.assertEqual((second.x, second.y, second.direction), (3, 3, "N"))

    def test_same_cell_different_direction_does_not_share_scent(self):
        first = self.world.spawn_robot(3, 2, "N")
        self.world.execute_command(first, "F")

        second = self.world.spawn_robot(3, 2, "E")
        self.world.execute_command(second, "F")

        self.assertFalse(second.lost)
        self.assertEqual((second.x, second.y, second.direction), (4, 2, "E"))

    def test_scent_prevents_lost_only_for_exact_direction(self):
        first = self.world.spawn_robot(5, 1, "E")
        self.world.execute_command(first, "F")

        second = self.world.spawn_robot(5, 1, "N")
        self.world.execute_command(second, "F")

        self.assertFalse(second.lost)
        self.assertEqual((second.x, second.y, second.direction), (5, 2, "N"))


if __name__ == "__main__":
    unittest.main()
