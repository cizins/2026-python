# R19. 轉換+聚合：生成器表達式（1.19）

# 範例資料：一串數字。
nums = [1, 2, 3]

# sum(...) 搭配生成器表達式：
# 逐個計算 x*x 並交給 sum 聚合，不會先建立完整中間 list。
# 寫法等價於 sum([x*x for x in nums])，但通常更省記憶體。
sum(x * x for x in nums)

# tuple 範例：元素型別可不同（字串、整數、浮點數）。
s = ('ACME', 50, 123.45)

# join 需要字串序列，因此先用 str(x) 轉型。
# 這裡同樣用生成器表達式，逐個產生字串後再串接。
','.join(str(x) for x in s)

# 投資組合資料：每筆為 dict。
portfolio = [{'name': 'AOL', 'shares': 20}, {'name': 'YHOO', 'shares': 75}]

# 寫法 1：先投影出 shares 欄位，再取最小值。
# 回傳結果是「最小持股數字」（例如 20）。
min(s['shares'] for s in portfolio)

# 寫法 2：直接對整筆資料取 min，並用 key 指定比較依據。
# 回傳結果是「最小 shares 對應的整筆 dict」。
min(portfolio, key=lambda s: s['shares'])
