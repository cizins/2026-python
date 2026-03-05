# 10 模組、類別、例外與 Big-O（最低門檻）範例

# ===== 1. 使用模組（Module）=====
# 從 collections 模組導入 deque（雙端隊列）
# deque 是比 list 更高效的隊列實現
from collections import deque

# 創建一個最多只能容納 2 個元素的 deque
# 當超過容量時，最舊的元素會自動被移除
q = deque(maxlen=2)
q.append(1)      # 加入 1，q = [1]
q.append(2)      # 加入 2，q = [1, 2]
q.append(3)      # 加入 3，q = [2, 3]（1 被自動丟掉）

print("deque 範例:")
print(f"  maxlen=2 的 deque: {list(q)}")  # 輸出：[2, 3]
print()

# ===== 2. 定義類別（Class）=====
# 類別是用來組織數據和方法的藍圖
class User:
    # __init__ 是構造函式，在創建對象時自動調用
    # self 代表這個對象本身
    def __init__(self, user_id):
        # 給這個 User 對象設置一個屬性 user_id
        self.user_id = user_id

# 根據 User 類別創建一個對象
u = User(42)
# 訪問對象的屬性
uid = u.user_id

print("類別範例:")
print(f"  User 對象的 user_id: {uid}")  # 輸出：42
print()

# ===== 3. 例外處理（Exception Handling）=====
# try-except 用來捕捉和處理程式運行時的錯誤

def is_int(val):
    """
    檢查一個值是否可以轉換為整數
    如果可以，返回 True；如果不能，返回 False（而不是讓程式崩潰）
    """
    try:
        # 嘗試將 val 轉換為整數
        int(val)
        # 如果成功，返回 True
        return True
    except ValueError:
        # 如果轉換失敗（發生 ValueError 例外），返回 False
        # 這樣程式就不會因為轉換失敗而崩潰
        return False

print("例外處理範例:")
print(f"  is_int('123'): {is_int('123')}")      # True
print(f"  is_int('hello'): {is_int('hello')}")  # False
print(f"  is_int('12.5'): {is_int('12.5')}")    # False
print()

# ===== 4. Big-O 時間複雜度概念 =====
# Big-O 表示演算法的執行時間如何隨著輸入大小增長

print("Big-O 時間複雜度說明:")
print("  list.append():     O(1) - 常數時間，無論列表多大都很快")
print("  list[0:n]:         O(N) - 線性時間，與切片長度成正比")
print("  list.insert(0, x): O(N) - 線性時間，需要移動後面的元素")
print("  'in' 運算符:        O(N) - 線性時間，需要逐一檢查每個元素")
print()

print("實際例子:")
# O(1) 操作 - 無論列表多大都很快
lst = [1, 2, 3, 4, 5]
lst.append(6)  # 非常快！
print(f"  append 後: {lst}")

# O(N) 操作 - 慢，特別是列表很大時
sliced = lst[0:3]  # 複製前 3 個元素，需要時間與 N 成正比
print(f"  切片 [0:3]: {sliced}")
