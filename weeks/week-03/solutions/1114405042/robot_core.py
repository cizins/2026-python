from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Set, Tuple

DIRECTIONS = ("N", "E", "S", "W")
MOVE_VECTOR = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}
VALID_COMMANDS = {"L", "R", "F"}


@dataclass
class RobotState:
    x: int
    y: int
    direction: str
    lost: bool = False

    def as_tuple(self) -> Tuple[int, int, str, bool]:
        return self.x, self.y, self.direction, self.lost


class RobotWorld:
    def __init__(self, width: int, height: int):
        if width < 0 or height < 0:
            raise ValueError("width and height must be non-negative")
        self.width = width
        self.height = height
        self.scent: Set[Tuple[int, int, str]] = set()

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x <= self.width and 0 <= y <= self.height

    def spawn_robot(self, x: int, y: int, direction: str) -> RobotState:
        direction = direction.upper()
        if direction not in DIRECTIONS:
            raise ValueError("direction must be one of N/E/S/W")
        if not self.in_bounds(x, y):
            raise ValueError("spawn position out of bounds")
        return RobotState(x=x, y=y, direction=direction)

    def execute_commands(self, robot: RobotState, commands: Iterable[str]) -> List[str]:
        outcomes: List[str] = []
        for command in commands:
            if robot.lost:
                break
            outcomes.append(self.execute_command(robot, command))
        return outcomes

    def execute_command(self, robot: RobotState, command: str) -> str:
        if robot.lost:
            return "SKIPPED_LOST"

        normalized = command.upper()
        if normalized not in VALID_COMMANDS:
            raise ValueError(f"invalid command: {command}")

        if normalized == "L":
            robot.direction = self._turn_left(robot.direction)
            return "TURN_LEFT"

        if normalized == "R":
            robot.direction = self._turn_right(robot.direction)
            return "TURN_RIGHT"

        return self._step_forward(robot)

    def clear_scent(self) -> None:
        self.scent.clear()

    def get_10x10_matrix(self, robot: RobotState | None = None) -> List[str]:
        matrix_size = 10
        board = [["." for _ in range(matrix_size)] for _ in range(matrix_size)]

        for sx, sy, _ in self.scent:
            if 0 <= sx < matrix_size and 0 <= sy < matrix_size:
                board[matrix_size - 1 - sy][sx] = "*"

        if robot is not None and 0 <= robot.x < matrix_size and 0 <= robot.y < matrix_size:
            marker = robot.direction if not robot.lost else "X"
            board[matrix_size - 1 - robot.y][robot.x] = marker

        return ["".join(row) for row in board]

    def _step_forward(self, robot: RobotState) -> str:
        dx, dy = MOVE_VECTOR[robot.direction]
        next_x = robot.x + dx
        next_y = robot.y + dy

        if self.in_bounds(next_x, next_y):
            robot.x = next_x
            robot.y = next_y
            return "MOVED"

        scent_key = (robot.x, robot.y, robot.direction)
        if scent_key in self.scent:
            return "IGNORED_BY_SCENT"

        self.scent.add(scent_key)
        robot.lost = True
        return "LOST"

    @staticmethod
    def _turn_left(direction: str) -> str:
        idx = DIRECTIONS.index(direction)
        return DIRECTIONS[(idx - 1) % 4]

    @staticmethod
    def _turn_right(direction: str) -> str:
        idx = DIRECTIONS.index(direction)
        return DIRECTIONS[(idx + 1) % 4]
