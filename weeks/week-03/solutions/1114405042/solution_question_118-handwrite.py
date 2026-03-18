"""UVA 118 - Mutant Flatworld Explorers（手打版）。

這份程式刻意保持「短、直覺、好背」：
1. 讀入世界邊界。
2. 逐台機器人執行指令。
3. 越界時依 scent 規則決定 LOST 或忽略前進。
"""

from __future__ import annotations


def turn_left(d: str) -> str:
    """方向左轉 90 度。"""
    order = "NESW"
    return order[(order.index(d) - 1) % 4]


def turn_right(d: str) -> str:
    """方向右轉 90 度。"""
    order = "NESW"
    return order[(order.index(d) + 1) % 4]


def next_position(x: int, y: int, d: str) -> tuple[int, int]:
    """依目前方向計算前進後座標。"""
    if d == "N":
        return x, y + 1
    if d == "S":
        return x, y - 1
    if d == "E":
        return x + 1, y
    return x - 1, y


def solve(data: str) -> str:
    """把整份輸入轉成題目要求的輸出。"""
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if not lines:
        return ""

    # 世界右上角座標（左下角固定是 0,0）
    max_x, max_y = map(int, lines[0].split())

    # scent 記錄「在某格、朝某方向前進會掉出去」的危險狀態。
    scents: set[tuple[int, int, str]] = set()
    out: list[str] = []

    i = 1
    while i + 1 < len(lines):
        x, y, d = lines[i].split()
        x = int(x)
        y = int(y)
        commands = lines[i + 1]
        i += 2

        lost = False

        for cmd in commands:
            if cmd == "L":
                d = turn_left(d)
                continue

            if cmd == "R":
                d = turn_right(d)
                continue

            # cmd == 'F'
            nx, ny = next_position(x, y, d)

            # 還在邊界內，直接前進。
            if 0 <= nx <= max_x and 0 <= ny <= max_y:
                x, y = nx, ny
                continue

            # 會越界：若這個狀態已有 scent，就忽略這次前進。
            key = (x, y, d)
            if key in scents:
                continue

            # 第一次在這裡這個方向掉落：留下 scent 並標記 LOST。
            scents.add(key)
            lost = True
            break

        if lost:
            out.append(f"{x} {y} {d} LOST")
        else:
            out.append(f"{x} {y} {d}")

    return "\n".join(out)


def main() -> None:
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
