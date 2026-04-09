# U04. 數字精度的陷阱與選擇（3.1–3.7）
# 說明：本程式碼示範 Python 處理數字（尤其是浮點數）時常見的陷阱：
# 1. 內建的 round() 函數採用「銀行家捨入法」(四捨六入五取偶)，而非一般數學課教的「四捨五入」。
# 2. NaN (Not a Number) 的比較陷阱，NaN 無法使用 == 進行比對。
# 3. float (浮點數) 的精度誤差問題，以及何時該使用 Decimal 來確保計算的絕對精確。

import math
import timeit
from decimal import Decimal, ROUND_HALF_UP

# ── 銀行家捨入（3.1）─────────────────────────────────
# 陷阱：Python 內建的 round() 函數預設採用 IEEE 754 標準的「銀行家捨入法」(Banker's rounding)
# 規則是「四捨六入五取偶」。當數字恰好在中間 (例如 .5) 時，它會捨入到最近的「偶數」。
# 這樣做的目的是在處理大量統計數據時，減少因為永遠向上捨入而累積的誤差。
print(round(0.5))  # 輸出: 0（因為最近的偶數是 0，不是一般數學教的 1！）
print(round(2.5))  # 輸出: 2（因為最近的偶數是 2，不是 3！）
print(round(3.5))  # 輸出: 4（因為最近的偶數是 4）


# 解法：如果你的系統（例如財務報表）嚴格要求傳統的「四捨五入」，
# 必須使用 `decimal` 模組，並指定 rounding=ROUND_HALF_UP 模式。
def trad_round(x: float, n: int = 0) -> Decimal:
    # 先把 float 轉成字串，再放進 Decimal，可以避免浮點數本身的二進位誤差
    d = Decimal(str(x))
    # 決定你要保留的小數位數格式 (例如 n=0 就是 '1'，n=2 就是 '0.00')
    fmt = Decimal("1") if n == 0 else Decimal("0." + "0" * n)
    # 使用 quantize 方法，並設定強制 ROUND_HALF_UP (即我們熟知的遇五進位)
    return d.quantize(fmt, rounding=ROUND_HALF_UP)


print(trad_round(0.5))  # 輸出: 1（回歸傳統的四捨五入）
print(trad_round(2.5))  # 輸出: 3


# ── NaN 無法用 == 比較（3.7）─────────────────────────
# NaN (Not a Number) 常用來表示缺失值或無效的計算結果
c = float("nan")

# 陷阱：根據 IEEE 754 標準，NaN 永遠不等於任何東西，包括它自己！
print(c == c)  # 輸出: False（自己不等於自己！）
print(c == float("nan"))  # 輸出: False

# 正確解法：唯一安全且正確檢查一個變數是否為 NaN 的方式，是使用 math.isnan()
print(math.isnan(c))  # 輸出: True


# 實務應用：清理資料清單中的無效值 (NaN)
data = [1.0, float("nan"), 3.0, float("nan"), 5.0]
# 利用 list comprehension 搭配 math.isnan 濾除 NaN
clean = [x for x in data if not math.isnan(x)]
print(clean)  # 輸出: [1.0, 3.0, 5.0]


# ── float vs Decimal 選擇（3.2）──────────────────────
# 陷阱：float (浮點數) 底層是以二進位儲存的，而很多十進位的小數（如 0.1, 0.2）
# 在二進位中會變成無限循環小數。這會導致截斷誤差。
# 適用場景：科學計算、工程計算（速度快，容許極小誤差）
print(0.1 + 0.2)  # 輸出: 0.30000000000000004（尾數出現了奇怪的誤差）
print(0.1 + 0.2 == 0.3)  # 輸出: False（因為有誤差，所以判斷相等會失敗！）

# 解法：Decimal 模組是以十進位的方式來儲存和計算數字，完全沒有上述的二進位轉換誤差。
# 適用場景：金融、會計系統（需要絕對的精確度，不能有誤差）
# 注意：傳給 Decimal 的一定要是「字串」(例如 "0.1")，如果直接傳 Decimal(0.1)，一開始就會帶有 float 誤差了！
print(Decimal("0.1") + Decimal("0.2"))  # 輸出: 0.3
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))  # 輸出: True（精準判斷相等）

# 但天下沒有白吃的午餐，Decimal 的計算速度遠慢於硬體原生支援的 float
# 使用 timeit 測量十萬次乘法運算
t1 = timeit.timeit(lambda: 0.1 * 999, number=100_000)
t2 = timeit.timeit(lambda: Decimal("0.1") * 999, number=100_000)
print(f"float: {t1:.3f}s  Decimal: {t2:.3f}s（Decimal 約慢 {t2 / t1:.0f} 倍）")
