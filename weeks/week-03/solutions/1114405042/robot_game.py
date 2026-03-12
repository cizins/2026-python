import os
import importlib
from dataclasses import dataclass
from datetime import datetime
from typing import List, Tuple

import pygame

from robot_core import RobotState, RobotWorld


WINDOW_WIDTH = 980
WINDOW_HEIGHT = 720
MARGIN = 60
HUD_PANEL_HEIGHT = 170
GRID_COLOR = (70, 70, 70)
BG_COLOR = (242, 248, 255)
ROBOT_COLOR = (220, 80, 60)
SCENT_COLOR = (30, 130, 90)
TEXT_COLOR = (30, 30, 30)
ALERT_COLOR = (200, 20, 20)
PANEL_BG_COLOR = (228, 236, 245)


@dataclass
class Snapshot:
    robot_x: int
    robot_y: int
    direction: str
    lost: bool
    scent: set
    action: str


class RobotGame:
    def __init__(self, width: int = 5, height: int = 3):
        pygame.init()
        pygame.display.set_caption("Robot Lost - Week 03")

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = self._load_cjk_font(22)
        self.small_font = self._load_cjk_font(18)

        self.world = RobotWorld(width=width, height=height)
        self.robot = self.world.spawn_robot(1, 1, "N")

        self.history: List[Snapshot] = []
        self.replay_index = 0
        self.replaying = False
        self.status_message = "按 L/R/F 操作，N 新機器人，C 清除保護記錄，P 回放，G 匯出 GIF，S 截圖"

        self.play_area_bottom = WINDOW_HEIGHT - MARGIN - HUD_PANEL_HEIGHT
        self.cell_size = min(
            (WINDOW_WIDTH - 2 * MARGIN) // (self.world.width + 1),
            (self.play_area_bottom - MARGIN) // (self.world.height + 1),
        )
        self.origin_x = MARGIN
        self.origin_y = self.play_area_bottom

        self._record_snapshot("INIT")

    @staticmethod
    def _load_cjk_font(size: int) -> pygame.font.Font:
        # Prefer concrete font files known to render Traditional Chinese on macOS.
        path_candidates = [
            "/System/Library/Fonts/STHeiti Medium.ttc",
            "/System/Library/Fonts/STHeiti Light.ttc",
            "/System/Library/Fonts/PingFang.ttc",
        ]
        for font_path in path_candidates:
            if os.path.exists(font_path):
                return pygame.font.Font(font_path, size)

        # Cross-platform fallback by font family name.
        name_candidates = [
            "PingFang TC",
            "Heiti TC",
            "Microsoft JhengHei",
            "Noto Sans CJK TC",
            "Noto Sans CJK",
            "Arial Unicode MS",
        ]
        for name in name_candidates:
            font_path = pygame.font.match_font(name)
            if font_path:
                return pygame.font.Font(font_path, size)
        return pygame.font.Font(None, size)

    def run(self) -> None:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    running = self._handle_keydown(event.key)

            if self.replaying:
                self._play_replay_step()

            self._draw()
            pygame.display.flip()
            self.clock.tick(10)

        pygame.quit()

    def _handle_keydown(self, key: int) -> bool:
        if key == pygame.K_ESCAPE:
            return False

        if key == pygame.K_n:
            self.robot = self.world.spawn_robot(1, 1, "N")
            self.status_message = "已建立新機器人，保留 scent。"
            self._record_snapshot("NEW_ROBOT")
            return True

        if key == pygame.K_c:
            self.world.clear_scent()
            self.status_message = "已清除所有保護記錄。"
            self._record_snapshot("CLEAR_SCENT")
            return True

        if key == pygame.K_p:
            self.replaying = True
            self.replay_index = 0
            self.status_message = "開始回放。"
            return True

        if key == pygame.K_g:
            self._export_replay_gif()
            return True

        if key == pygame.K_s:
            self._save_gameplay_screenshot()
            return True

        command_map = {
            pygame.K_l: "L",
            pygame.K_r: "R",
            pygame.K_f: "F",
        }

        if key in command_map:
            command = command_map[key]
            try:
                result = self.world.execute_command(self.robot, command)
                self.status_message = f"指令 {command} => {self._describe_result(result)}"
                self._record_snapshot(command)
            except ValueError as exc:
                self.status_message = str(exc)
            return True

        return True

    def _record_snapshot(self, action: str) -> None:
        self.history.append(
            Snapshot(
                robot_x=self.robot.x,
                robot_y=self.robot.y,
                direction=self.robot.direction,
                lost=self.robot.lost,
                scent=set(self.world.scent),
                action=action,
            )
        )

    def _play_replay_step(self) -> None:
        if not self.history:
            self.replaying = False
            self.status_message = "沒有可回放內容。"
            return

        snapshot = self.history[self.replay_index]
        self.robot.x = snapshot.robot_x
        self.robot.y = snapshot.robot_y
        self.robot.direction = snapshot.direction
        self.robot.lost = snapshot.lost
        self.world.scent = set(snapshot.scent)
        self.status_message = f"回放中 {self.replay_index + 1}/{len(self.history)}: {snapshot.action}"

        self.replay_index += 1
        if self.replay_index >= len(self.history):
            self.replaying = False
            self.replay_index = 0
            self.status_message = "回放結束。"

    def _grid_to_screen(self, x: int, y: int) -> Tuple[int, int]:
        px = self.origin_x + x * self.cell_size
        py = self.origin_y - y * self.cell_size
        return px, py

    def _cell_top_left(self, x: int, y: int) -> Tuple[int, int]:
        px = self.origin_x + x * self.cell_size
        py = self.origin_y - (y + 1) * self.cell_size
        return px, py

    def _draw(self) -> None:
        self.screen.fill(BG_COLOR)
        self._draw_grid()
        self._draw_scent()
        self._draw_robot()
        self._draw_hud()

    def _draw_grid(self) -> None:
        top_y = self.origin_y - (self.world.height + 1) * self.cell_size
        right_x = self.origin_x + (self.world.width + 1) * self.cell_size

        for x in range(self.world.width + 2):
            line_x = self.origin_x + x * self.cell_size
            pygame.draw.line(self.screen, GRID_COLOR, (line_x, self.origin_y), (line_x, top_y), 1)

        for y in range(self.world.height + 2):
            line_y = self.origin_y - y * self.cell_size
            pygame.draw.line(self.screen, GRID_COLOR, (self.origin_x, line_y), (right_x, line_y), 1)

        for x in range(self.world.width + 1):
            for y in range(self.world.height + 1):
                px, py = self._cell_top_left(x, y)
                label = self.small_font.render(f"{x},{y}", True, (110, 110, 110))
                self.screen.blit(label, (px + 4, py + 4))

    def _draw_scent(self) -> None:
        for sx, sy, _ in self.world.scent:
            px, py = self._cell_top_left(sx, sy)
            center = (px + self.cell_size // 2, py + self.cell_size // 2)
            pygame.draw.circle(self.screen, SCENT_COLOR, center, 6)

    def _draw_robot(self) -> None:
        px, py = self._cell_top_left(self.robot.x, self.robot.y)
        center_x = px + self.cell_size // 2
        center_y = py + self.cell_size // 2
        radius = self.cell_size // 3

        direction_vector = {
            "N": (0.0, -1.0),
            "E": (1.0, 0.0),
            "S": (0.0, 1.0),
            "W": (-1.0, 0.0),
        }
        fx, fy = direction_vector[self.robot.direction]
        # Perpendicular vector to form an isosceles base.
        pxv, pyv = -fy, fx

        tip_len = float(radius)
        base_offset = float(radius) * 0.55
        half_base = float(radius) * 0.75

        tip = (center_x + fx * tip_len, center_y + fy * tip_len)
        base_center = (center_x - fx * base_offset, center_y - fy * base_offset)
        base_left = (base_center[0] + pxv * half_base, base_center[1] + pyv * half_base)
        base_right = (base_center[0] - pxv * half_base, base_center[1] - pyv * half_base)

        points = [
            (int(round(tip[0])), int(round(tip[1]))),
            (int(round(base_left[0])), int(round(base_left[1]))),
            (int(round(base_right[0])), int(round(base_right[1]))),
        ]

        color = ALERT_COLOR if self.robot.lost else ROBOT_COLOR
        pygame.draw.polygon(self.screen, color, points)

    def _draw_hud(self) -> None:
        status_color = ALERT_COLOR if self.robot.lost else TEXT_COLOR
        lost_text = "已遺失" if self.robot.lost else "正常"
        top_text = f"機器人: ({self.robot.x}, {self.robot.y}) 方向: {self._direction_zh(self.robot.direction)} | 狀態: {lost_text}"
        hint = "鍵盤: L/R/F 操作 | N 新機器人 | C 清除保護記錄 | P 回放 | G 匯出 GIF | S 存截圖 | ESC 離開"

        panel_x = MARGIN - 12
        panel_y = self.play_area_bottom + 18
        panel_width = WINDOW_WIDTH - 2 * (MARGIN - 12)
        panel_height = HUD_PANEL_HEIGHT - 26

        pygame.draw.rect(self.screen, PANEL_BG_COLOR, (panel_x, panel_y, panel_width, panel_height), border_radius=10)
        pygame.draw.rect(self.screen, GRID_COLOR, (panel_x, panel_y, panel_width, panel_height), width=1, border_radius=10)

        self.screen.blit(self.font.render("規則與狀態（下方固定區）", True, TEXT_COLOR), (MARGIN, panel_y + 10))
        self.screen.blit(self.small_font.render(top_text, True, status_color), (MARGIN, panel_y + 44))
        self.screen.blit(self.small_font.render(self.status_message, True, TEXT_COLOR), (MARGIN, panel_y + 70))
        self.screen.blit(self.small_font.render(hint, True, TEXT_COLOR), (MARGIN, panel_y + 96))

    @staticmethod
    def _direction_zh(direction: str) -> str:
        mapping = {
            "N": "北(N)",
            "E": "東(E)",
            "S": "南(S)",
            "W": "西(W)",
        }
        return mapping.get(direction, direction)

    @staticmethod
    def _describe_result(result: str) -> str:
        mapping = {
            "TURN_LEFT": "左轉 90 度",
            "TURN_RIGHT": "右轉 90 度",
            "MOVED": "前進一格",
            "LOST": "越界遺失（LOST）",
            "IGNORED_BY_SCENT": "偵測到 scent，忽略危險前進",
            "SKIPPED_LOST": "機器人已遺失，略過",
        }
        return mapping.get(result, result)

    def _export_replay_gif(self) -> None:
        if not self.history:
            self.status_message = "尚無回放內容可匯出。"
            return

        try:
            imageio = importlib.import_module("imageio.v2")
        except Exception:
            self.status_message = "缺少 GIF 套件：請安裝 imageio 與 pillow。"
            return

        temp_surfaces = []
        original = Snapshot(
            robot_x=self.robot.x,
            robot_y=self.robot.y,
            direction=self.robot.direction,
            lost=self.robot.lost,
            scent=set(self.world.scent),
            action="ORIGINAL",
        )

        for snapshot in self.history:
            self.robot.x = snapshot.robot_x
            self.robot.y = snapshot.robot_y
            self.robot.direction = snapshot.direction
            self.robot.lost = snapshot.lost
            self.world.scent = set(snapshot.scent)
            self.status_message = f"匯出中: {snapshot.action}"
            self._draw()
            frame = pygame.surfarray.array3d(self.screen)
            temp_surfaces.append(frame.swapaxes(0, 1))

        self.robot.x = original.robot_x
        self.robot.y = original.robot_y
        self.robot.direction = original.direction
        self.robot.lost = original.lost
        self.world.scent = set(original.scent)

        out_dir = os.path.join(os.path.dirname(__file__), "assets")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "replay.gif")
        try:
            imageio.mimsave(out_path, temp_surfaces, duration=0.35)
        except Exception as exc:
            self.status_message = f"GIF 輸出失敗：{type(exc).__name__}: {exc}"
            return

        timestamp = datetime.now().strftime("%H:%M:%S")
        self.status_message = f"{timestamp} 已輸出 {out_path}"

    def _save_gameplay_screenshot(self) -> None:
        out_dir = os.path.join(os.path.dirname(__file__), "assets")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "gameplay.png")

        try:
            # Render one fresh frame before capture to ensure HUD and map are up to date.
            self._draw()
            pygame.display.flip()
            pygame.image.save(self.screen, out_path)
        except Exception as exc:
            self.status_message = f"截圖失敗：{type(exc).__name__}: {exc}"
            return

        timestamp = datetime.now().strftime("%H:%M:%S")
        self.status_message = f"{timestamp} 已儲存 {out_path}"


def main() -> None:
    game = RobotGame(width=5, height=3)
    game.run()


if __name__ == "__main__":
    main()
