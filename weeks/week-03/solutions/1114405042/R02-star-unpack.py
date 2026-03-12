# R2. 解包數量不固定：星號解包（1.2）

# 這支程式示範「星號解包」(asterisk unpacking)。
# 核心觀念：在解包時，帶 * 的變數可以吃掉「不固定數量」的元素。
# 例如：a, *b, c = [1, 2, 3, 4]
# - a 會拿到第一個元素 1
# - c 會拿到最後一個元素 4
# - b 會拿到中間所有元素 [2, 3]
def drop_first_last(grades):
    # first 與 last 分別接第一個、最後一個成績
    # *middle 會接住中間所有成績（數量可變）
    first, *middle, last = grades

    # 只計算中間成績平均，忽略頭尾
    # sum(middle) / len(middle) 是平均值公式
    return sum(middle) / len(middle)


# ------------------------------
# 範例 1：函式中使用星號解包
# ------------------------------
print("=== 範例 1：函式中使用星號解包 ===")
grades = [98, 92, 88, 94, 99]
print(f"原始成績：{grades}")
avg_middle = drop_first_last(grades)
print(f"去掉第一個與最後一個後，中間平均分數：{avg_middle}")


# ------------------------------
# 範例 2：收集不固定欄位
# ------------------------------
# 假設一筆資料由：姓名、Email、多個電話號碼組成。
# 電話數量可能是 0 個、1 個或很多個，
# 用 *phone_numbers 可以彈性接收剩下所有電話。
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print("\n=== 範例 2：收集不固定數量欄位 ===")
print(f"原始 record：{record}")
print(f"name = {name}")
print(f"email = {email}")
print(f"phone_numbers = {phone_numbers}")


# ------------------------------
# 範例 3：抓最後一筆，其餘打包
# ------------------------------
# *trailing 會接前面所有元素，current 接最後一個。
# 常見於「前面是歷史資料，最後一筆是最新資料」的情境。
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print("\n=== 範例 3：前段收集 + 最後一個元素 ===")
print(f"trailing = {trailing}")
print(f"current = {current}")
