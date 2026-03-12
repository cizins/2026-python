# R1. 序列解包（1.1）

# 序列解包（unpacking）的核心：
# 把一個序列（tuple、list）中的元素，依序指定給多個變數。
#
# 基本規則：
# - 左邊變數數量，通常要和右邊元素數量一致
# - 依照位置對應（第 1 個給第 1 個變數，以此類推）
p = (4, 5)
x, y = p
print("=== 範例 1：元組解包 ===")
print(f"原始元組 p：{p}")
print(f"解包後 x = {x}, y = {y}")

# data 是一筆混合資料：
# - 公司名稱（字串）
# - 股數（整數）
# - 單價（浮點數）
# - 日期（內層 tuple）
data = ['ACME', 50, 91.1, (2012, 12, 21)]

# 一般解包：先把第 4 個元素整包接到 date（它本身是 tuple）。
name, shares, price, date = data
print("\n=== 範例 2：列表解包 ===")
print(f"原始資料 data：{data}")
print(f"name = {name}, shares = {shares}, price = {price}, date = {date}")

# 巢狀解包：直接把內層日期 tuple 再拆成 year、mon、day。
# 這可避免後續再手動寫 date[0]、date[1]、date[2]。
name, shares, price, (year, mon, day) = data
print("\n=== 範例 3：巢狀解包 ===")
print(f"name = {name}, shares = {shares}, price = {price}")
print(f"year = {year}, mon = {mon}, day = {day}")

# 丟棄不需要的值（占位）
# 使用 _ 當占位符，表示「這個值我不打算使用」。
# 這裡只關心 shares 和 price，其他欄位用 _ 接住即可。
#
# 注意：_ 只是一般變數名稱，並非語法關鍵字。
# 但在慣例上，它代表「可忽略的值」。
_, shares, price, _ = data
print("\n=== 範例 4：使用 _ 丟棄不需要的值 ===")
print(f"只保留 shares 和 price：shares = {shares}, price = {price}")
