#!/usr/bin/env python3
"""驗證簡化版本的正確性"""

# 直接定義函數（簡化版本）
def cycle_length(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    if n % 2 == 1:
        result = 1 + cycle_length(3 * n + 1, memo)
    else:
        result = 1 + cycle_length(n // 2, memo)
    memo[n] = result
    return result

def solve(i, j):
    start, end = min(i, j), max(i, j)
    max_len = max(cycle_length(n) for n in range(start, end + 1))
    return (i, j, max_len)

# 測試
test_cases = [(1, 10), (100, 200), (201, 210), (900, 1000)]
expected = [(1, 10, 20), (100, 200, 125), (201, 210, 89), (900, 1000, 174)]

print("=" * 60)
print("簡化版本 (Easy) 測試結果")
print("=" * 60)
print()

for result, exp in zip([solve(*tc) for tc in test_cases], expected):
    status = "✓ PASS" if result == exp else "✗ FAIL"
    print(f"{status}")
    print(f"  結果: {result}")
    print(f"  期望: {exp}")
    print()

all_pass = all(solve(*tc) == exp for tc, exp in zip(test_cases, expected))
print("=" * 60)
print(f"總結: {'全部通過 ✓' if all_pass else '有失敗 ✗'}")
print("=" * 60)
