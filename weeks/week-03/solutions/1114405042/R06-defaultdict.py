# R6. 多值字典 defaultdict / setdefault（1.6）

# defaultdict 是 dict 的子類別。
# 最大特色：當你存取一個不存在的 key 時，
# 它會自動用你指定的「工廠函式」建立預設值。
#
# 例如 defaultdict(list)：
# - 第一次讀取 d['a'] 時，會自動建立空列表 []
# - 所以可以直接 d['a'].append(...)，不用先 if 檢查 key 是否存在
from collections import defaultdict

print("=== 範例 1：defaultdict(list) ===")

# 建立「值型別為 list」的 defaultdict。
# 每個新 key 的預設值都會是 []。
d = defaultdict(list)

# 因為 'a' 還不存在，第一次 d['a'] 會先自動建立 []，再 append(1)。
d['a'].append(1)
# 第二次直接在同一個列表後面加 2。
d['a'].append(2)
print(f"加入 1、2 到 'd[\"a\"]'：{dict(d)}")

print("\n=== 範例 2：defaultdict(set) ===")

# 建立「值型別為 set」的 defaultdict。
# 每個新 key 的預設值都會是 set()。
d = defaultdict(set)

# set 會自動去重：重複 add 相同元素只會保留一份。
d['a'].add(1)
d['a'].add(2)
print(f"新增 1、2 到 'd[\"a\"]'（集合）：{dict(d)}")

print("\n=== 範例 3：setdefault（用於普通字典）===")

# 這裡改用普通 dict，沒有自動初始化功能。
d = {}
print(f"初始字典：{d}")

# setdefault(key, default) 的行為：
# 1) 若 key 已存在：回傳既有值
# 2) 若 key 不存在：先放入 default，再回傳 default
#
# 因此這行可拆成概念：
# - 若 'a' 不在 d，就先設定 d['a'] = []
# - 再對那個列表 append(1)
d.setdefault('a', []).append(1)
print(f"使用 setdefault('a', []).append(1) 後：{d}")

# defaultdict vs setdefault 的理解重點：
# - defaultdict：初始化規則在「字典建立時」一次定義
# - setdefault：初始化規則在「每次操作 key 時」寫進程式
print(f"說明：setdefault 會先檢查 key，如果不存在則設為預設值，再執行操作。")
