"""UVA 948 假幣問題解法。

此版本是較通用、結構清楚的寫法：
1. 先把每次秤重資料整理成結構化資料。
2. 逐一假設每顆硬幣可能是「較重的假幣」或「較輕的假幣」。
3. 只要某個假設能同時滿足所有秤重結果，就代表該硬幣有可能是假幣。
4. 若最後只有一顆硬幣可行，輸出其編號；否則輸出 0。
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class Weighing:
    """紀錄一次秤重的左右硬幣與結果。"""

    left: List[int]
    right: List[int]
    result: str  # '<'、'>'、'='


def _skip_blank_lines(lines: List[str], idx: int) -> int:
    """略過空白行，回傳下一個非空白行索引。"""
    while idx < len(lines) and not lines[idx].strip():
        idx += 1
    return idx


def _parse_cases(text: str) -> List[tuple[int, List[Weighing]]]:
    """把整份輸入解析成多組測資。"""
    lines = text.splitlines()
    idx = _skip_blank_lines(lines, 0)
    if idx >= len(lines):
        return []

    case_count = int(lines[idx].strip())
    idx += 1
    cases: List[tuple[int, List[Weighing]]] = []

    for _ in range(case_count):
        idx = _skip_blank_lines(lines, idx)
        n, k = map(int, lines[idx].split())
        idx += 1

        weighings: List[Weighing] = []
        for _ in range(k):
            idx = _skip_blank_lines(lines, idx)
            row = list(map(int, lines[idx].split()))
            idx += 1

            p = row[0]
            left = row[1 : 1 + p]
            right = row[1 + p : 1 + 2 * p]

            idx = _skip_blank_lines(lines, idx)
            result = lines[idx].strip()
            idx += 1

            weighings.append(Weighing(left=left, right=right, result=result))

        cases.append((n, weighings))

    return cases


def _fits_weighing(fake_coin: int, fake_is_heavier: bool, weighing: Weighing) -> bool:
    """檢查某次秤重是否符合指定假設（某顆硬幣為較重/較輕的假幣）。"""
    delta = 1 if fake_is_heavier else -1

    # 因為只有一顆假幣，所以左右重量差只會來自假幣是否在盤上。
    left_weight_effect = sum(delta for coin in weighing.left if coin == fake_coin)
    right_weight_effect = sum(delta for coin in weighing.right if coin == fake_coin)

    if weighing.result == "=":
        return left_weight_effect == right_weight_effect
    if weighing.result == "<":
        return left_weight_effect < right_weight_effect
    return left_weight_effect > right_weight_effect


def find_counterfeit_coin(n: int, weighings: List[Weighing]) -> int:
    """回傳假幣編號；若無法唯一確定，回傳 0。"""
    candidates = []

    for coin in range(1, n + 1):
        heavier_ok = all(_fits_weighing(coin, True, w) for w in weighings)
        lighter_ok = all(_fits_weighing(coin, False, w) for w in weighings)

        if heavier_ok or lighter_ok:
            candidates.append(coin)

    return candidates[0] if len(candidates) == 1 else 0


def solve_from_text(text: str) -> str:
    """把整份輸入文字轉成題目要求的輸出文字。"""
    cases = _parse_cases(text)
    outputs = [str(find_counterfeit_coin(n, weighings)) for n, weighings in cases]
    return "\n\n".join(outputs)


def main() -> None:
    """標準輸入輸出進入點。"""
    import sys

    data = sys.stdin.read()
    print(solve_from_text(data))


if __name__ == "__main__":
    main()
