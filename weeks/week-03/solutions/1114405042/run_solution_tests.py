#!/usr/bin/env python3
"""
執行解決方案程式的測試腳本
"""

from solution_question_100 import solve_batch

print("=" * 60)
print("題目 100 - Collatz 序列 解決方案執行測試")
print("=" * 60)
print()

# 測試用例（來自題目的預期輸出）
test_cases = [
    (1, 10),
    (100, 200),
    (201, 210),
    (900, 1000),
]

# 預期輸出
expected_results = [
    (1, 10, 20),
    (100, 200, 125),
    (201, 210, 89),
    (900, 1000, 174),
]

# 求解
results = solve_batch(test_cases)

# 顯示結果
print("測試結果對比：")
print("-" * 60)
print(f"{'測試':8} {'輸入':^15} {'預期':^10} {'實際':^10} {'狀態':<10}")
print("-" * 60)

all_passed = True
for idx, (result, expected) in enumerate(zip(results, expected_results), 1):
    i, j, max_cycle = result
    exp_i, exp_j, exp_max = expected
    
    # 檢查結果是否符合預期
    passed = (i == exp_i and j == exp_j and max_cycle == exp_max)
    status = "✓ PASS" if passed else "✗ FAIL"
    
    if not passed:
        all_passed = False
    
    print(f"測試 {idx:<2} ({i:>3},{j:>3}){max_cycle:>12}{exp_max:>12}{status}")

print("-" * 60)
print()

# 摘要
print("測試摘要：")
print(f"{'總測試數':16} {len(test_cases)}")
print(f"{'通過數':16} {sum(1 for r, e in zip(results, expected_results) if r == e)}")
print(f"{'失敗數':16} {sum(1 for r, e in zip(results, expected_results) if r != e)}")
print()

if all_passed:
    print("✓ 所有測試通過！")
else:
    print("✗ 某些測試失敗")

print()
print("=" * 60)
