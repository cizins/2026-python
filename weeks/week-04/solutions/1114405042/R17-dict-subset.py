# R17. 字典子集（1.17）

# 原始資料：股票代號 -> 股價。
# 這裡示範如何從既有字典中「挑選部分鍵值」形成新字典。
prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55}

# 字典推導式（dict comprehension）語法：
# {新鍵: 新值 for ... if 條件}
# 這行的條件是 v > 200，表示只保留價格高於 200 的項目。
# 結果 p1 會是 prices 的「值條件子集」。
p1 = {k: v for k, v in prices.items() if v > 200}

# 先定義一組要保留的目標鍵（公司代號）。
# 使用 set 進行 membership 測試（k in tech_names）通常效率不錯。
tech_names = {'AAPL', 'IBM'}

# 這行改用「鍵條件」建立子集：
# 只有鍵在 tech_names 內的項目才會被保留。
# 結果 p2 會是 prices 的「鍵集合子集」。
p2 = {k: v for k, v in prices.items() if k in tech_names}
