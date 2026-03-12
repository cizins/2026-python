import unittest

from robot_core import RobotWorld


class TestRobotCore(unittest.TestCase):
    def setUp(self):
        self.world = RobotWorld(width=5, height=3)

    def test_turn_left_from_north_is_west(self):
        robot = self.world.spawn_robot(1, 1, "N")
        self.world.execute_command(robot, "L")
        self.assertEqual(robot.direction, "W")

    def test_turn_right_from_north_is_east(self):
        robot = self.world.spawn_robot(1, 1, "N")
        self.world.execute_command(robot, "R")
        self.assertEqual(robot.direction, "E")

    def test_four_right_turns_return_to_original_direction(self):
        robot = self.world.spawn_robot(1, 1, "N")
        self.world.execute_commands(robot, "RRRR")
        self.assertEqual(robot.direction, "N")

    def test_forward_inside_boundary_is_safe(self):
        robot = self.world.spawn_robot(1, 1, "N")
        self.world.execute_command(robot, "F")
        self.assertEqual((robot.x, robot.y, robot.direction, robot.lost), (1, 2, "N", False))

    def test_forward_out_of_boundary_causes_lost(self):
        robot = self.world.spawn_robot(0, 3, "N")
        self.world.execute_command(robot, "F")
        self.assertTrue(robot.lost)
        self.assertEqual((robot.x, robot.y, robot.direction), (0, 3, "N"))

    def test_lost_robot_stops_processing_remaining_commands(self):
        robot = self.world.spawn_robot(0, 3, "N")
        self.world.execute_commands(robot, "FRF")
        self.assertTrue(robot.lost)
        self.assertEqual((robot.x, robot.y, robot.direction), (0, 3, "N"))

    def test_invalid_command_raises_value_error(self):
        robot = self.world.spawn_robot(1, 1, "N")
        with self.assertRaises(ValueError):
            self.world.execute_command(robot, "X")


if __name__ == "__main__":
    unittest.main()
