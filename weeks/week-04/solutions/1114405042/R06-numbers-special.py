# R06. 特殊數值：無窮大、NaN、分數、隨機（3.7–3.11）
#
# 這份範例整理幾種在資料處理、統計與演算法中常見的「特殊數值情境」：
# 1) 無窮大（inf）、非數值（NaN）的判斷與運算特性
# 2) Fraction 分數的精確有理數計算
# 3) random 模組常用隨機操作與固定種子重現結果
#
# 重點：這些主題常是 bug 的來源，尤其是 NaN 比較與隨機結果不可重現。

import math
import random
from fractions import Fraction

# ── 3.7 無窮大與 NaN ──────────────────────────────────
# 透過 float() 建立特殊浮點值
a = float("inf")
b = float("-inf")
c = float("nan")
print(a, b, c)  # inf -inf nan

# math.isinf() / math.isnan() 是判斷特殊值最可靠方式
print(math.isinf(a))  # True
print(math.isnan(c))  # True

# 和 inf 的運算：
# inf + 有限值 -> inf
# 有限值 / inf -> 0.0
print(a + 45, 10 / a)  # inf 0.0

# 未定義情境通常會得到 NaN，例如 inf/inf、inf + (-inf)
print(a / a, a + b)  # nan nan（未定義）

# NaN 有個重要特性：它不等於任何值，包含它自己
# 因此判斷 NaN 請用 math.isnan(x)，不要用 x == x
print(c == c)  # False（NaN 不等於自己！）

# ── 3.8 分數運算 ──────────────────────────────────────
# Fraction(分子, 分母) 以「有理數」精確表示，不會有浮點誤差
p = Fraction(5, 4)
q = Fraction(7, 16)
r = p * q

# 分數可直接做四則運算
print(p + q)  # 27/16

# 可取得最簡分數的分子與分母
print(r.numerator, r.denominator)  # 35 64

# 需要時可轉為 float（轉換後才可能有浮點表示誤差）
print(float(r))  # 0.546875

# limit_denominator(max_denominator)
# 用「分母上限」近似目前分數，常用於近似小數為好理解分數
print(r.limit_denominator(8))  # 4/7

# float.as_integer_ratio() 可把浮點值寫成「整數比」
# 搭配 Fraction(*) 可回復為分數表示
print(Fraction(*(3.75).as_integer_ratio()))  # 15/4

# ── 3.11 隨機選擇 ─────────────────────────────────────
values = [1, 2, 3, 4, 5, 6]

# 從序列中隨機取 1 個元素
print(random.choice(values))  # 隨機一個

# 取 k 個「不重複」樣本（不改變原序列）
print(random.sample(values, 3))  # 3 個不重複樣本

# 原地打亂（in-place），會直接改動 values
random.shuffle(values)
print(values)  # 打亂後的序列

# randint(a, b) 包含兩端點 a 與 b
print(random.randint(0, 10))  # 0~10 整數

# 設定固定種子可重現隨機流程，方便除錯與教學展示
random.seed(42)
print(random.random())  # 固定種子：可重現
