"""UVA 948 假幣問題（-easy 版本，超好記口訣）。

口訣只有三句：
1. 猜哪一顆是假幣。
2. 猜它是偏重還是偏輕。
3. 拿這個猜測去檢查每一次秤重。

只要某顆硬幣在「偏重」或「偏輕」其中一種情況下，
可以通過全部秤重，它就可能是假幣。

最後：
- 可能的硬幣只有一顆 -> 輸出該編號
- 否則（多顆或零顆） -> 輸出 0
"""

from __future__ import annotations


def _skip_blanks(lines: list[str], i: int) -> int:
    """把索引 i 往後移到第一個非空白行。"""
    while i < len(lines) and not lines[i].strip():
        i += 1
    return i


def parse_input(text: str) -> list[tuple[int, list[tuple[list[int], list[int], str]]]]:
    """解析題目輸入。

    回傳格式：
    [
      (n, [([左盤硬幣...], [右盤硬幣...], 結果字元), ...]),
      ...
    ]
    """
    lines = text.splitlines()
    i = _skip_blanks(lines, 0)
    if i >= len(lines):
        return []

    m = int(lines[i].strip())
    i += 1
    cases: list[tuple[int, list[tuple[list[int], list[int], str]]]] = []

    for _ in range(m):
        i = _skip_blanks(lines, i)
        n, k = map(int, lines[i].split())
        i += 1

        weighings: list[tuple[list[int], list[int], str]] = []
        for _ in range(k):
            i = _skip_blanks(lines, i)
            row = list(map(int, lines[i].split()))
            i += 1

            p = row[0]
            left = list(row[1 : 1 + p])
            right = list(row[1 + p : 1 + 2 * p])

            i = _skip_blanks(lines, i)
            result = lines[i].strip()
            i += 1

            weighings.append((left, right, result))

        cases.append((n, weighings))

    return cases


def check_weighing(fake_coin: int, is_heavy: bool, left: list[int], right: list[int], result: str) -> bool:
    """檢查一次秤重是否符合假設。

    假設：fake_coin 是假幣，且 is_heavy 決定它是偏重還是偏輕。
    """
    # 偏重用 +1，偏輕用 -1，這樣左右盤只要比較數值大小即可。
    effect = 1 if is_heavy else -1

    left_delta = effect if fake_coin in left else 0
    right_delta = effect if fake_coin in right else 0

    # 題目符號意義：
    # '<' 代表左盤比較輕
    # '>' 代表左盤比較重
    # '=' 代表一樣重
    if result == "<":
        return left_delta < right_delta
    if result == ">":
        return left_delta > right_delta
    return left_delta == right_delta


def solve_case(n: int, weighings: list[tuple[list[int], list[int], str]]) -> int:
    """解單一測資。

    這裡就是最好記的三層檢查：
    1. 猜 coin
    2. 猜 heavy / light
    3. 對所有秤重做驗證
    """
    candidates: list[int] = []

    for coin in range(1, n + 1):
        can_be_fake = False

        for is_heavy in (True, False):
            all_ok = True

            for left, right, result in weighings:
                if not check_weighing(coin, is_heavy, left, right, result):
                    all_ok = False
                    break

            if all_ok:
                can_be_fake = True
                break

        if can_be_fake:
            candidates.append(coin)

    return candidates[0] if len(candidates) == 1 else 0


def solve_from_text(text: str) -> str:
    """處理整份輸入，回傳題目要求輸出字串。"""
    cases = parse_input(text)
    answers = [str(solve_case(n, weighings)) for n, weighings in cases]
    return "\n\n".join(answers)


def main() -> None:
    """標準輸入輸出進入點。"""
    import sys

    text = sys.stdin.read()
    print(solve_from_text(text))


if __name__ == "__main__":
    main()
