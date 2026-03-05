# 9 比較、排序與 key 函式範例

# 比較運算（tuple 逐一比較）
a = (1, 2)
b = (1, 3)
result = a < b
print(f"(1, 2) < (1, 3): {result}")  # True，因為第二個元素 2 < 3
print()

# key 排序
rows = [{'uid': 3}, {'uid': 1}, {'uid': 2}]
rows_sorted = sorted(rows, key=lambda r: r['uid'])
print("原始列表:", rows)
print("按 uid 排序:", rows_sorted)
print()

# min/max 搭配 key
smallest = min(rows, key=lambda r: r['uid'])
largest = max(rows, key=lambda r: r['uid'])
print("最小元素 (uid 最小):", smallest)
print("最大元素 (uid 最大):", largest)
print()

# reverse 排序
rows_reverse = sorted(rows, key=lambda r: r['uid'], reverse=True)
print("反向排序 (uid 大到小):", rows_reverse)
print()

# 字符串排序範例
words = ['apple', 'pie', 'a', 'longer']
sorted_by_length = sorted(words, key=len)
print("原始字符串:", words)
print("按長度排序:", sorted_by_length)
print()

# 複合排序
students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 85},
]
sorted_by_score = sorted(students, key=lambda s: s['score'], reverse=True)
print("學生按分數排序 (高到低):")
for student in sorted_by_score:
    print(f"  {student['name']}: {student['score']}")
