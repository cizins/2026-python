# R11. 命名切片 slice（1.11）

# 這是一筆「固定欄位寬度」的字串資料。
# 雖然看起來很多點，但其中某些固定位置其實藏有數值：
# - index 20~22: 股份數量（100）
# - index 31~36: 單價（513.25）
#
# 這種格式在舊系統報表、文字檔匯出中很常見。
record = '....................100 .......513.25 ..........'
print("=== 使用命名 slice 提取資料 ===")
print(f"原始記錄：{record}")

# 用「命名切片」提高可讀性：
# SHARES 代表股份欄位位置，PRICE 代表價格欄位位置。
#
# slice(start, stop) 是「左閉右開」：
# - start 位置會包含
# - stop 位置不包含
# 所以 slice(20, 23) 會抓 index 20, 21, 22 三個字元。
SHARES = slice(20, 23)
PRICE = slice(31, 37)
print(f"\nslice 定義：")
print(f"  SHARES = slice(20, 23)  # 股份數量位置")
print(f"  PRICE = slice(31, 37)   # 價格位置")

# 直接把 slice 物件拿去做字串切片。
# 這樣做比寫死 record[20:23] 更易維護：
# 之後欄位位置改了，只要改 SHARES/PRICE 定義即可。
shares_str = record[SHARES]
price_str = record[PRICE]
print(f"\n提取的資料：")
print(f"  股份：'{shares_str}'")
print(f"  價格：'{price_str}'")

# 提取結果目前還是字串，先轉型後才能做數學計算。
# int('100') -> 100
# float('513.25') -> 513.25
shares = int(shares_str)
price = float(price_str)

# 成本公式：總成本 = 股份數量 × 單價
cost = shares * price
print(f"\n計算成本：")
print(f"  {shares} 股 × ${price} = ${cost}")
