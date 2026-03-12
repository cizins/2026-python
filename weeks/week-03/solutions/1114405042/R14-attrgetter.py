# R14. 物件排序 attrgetter（1.14）

# 從 operator 模組匯入 attrgetter。
# attrgetter('user_id') 會回傳一個「取值函式」，
# 這個函式接收物件後，會取出該物件的 .user_id。
# 常用在 sorted(..., key=...) 讓排序規則更簡潔。
from operator import attrgetter


# 建立一個簡單的 User 類別。
# 這裡每個 User 只有一個屬性：user_id。
class User:
    # 建構子：建立物件時把 user_id 存進物件。
    def __init__(self, user_id):
        self.user_id = user_id

    # __repr__ 會影響「直接印出物件」時的顯示字串。
    # 沒有這個方法時，通常會看到像 <__main__.User object at 0x...>
    # 加上 __repr__ 後，輸出會變成 User(user_id=23) 這種可讀格式。
    def __repr__(self):
        return f"User(user_id={self.user_id})"


# 建立一組 User 物件，故意打亂順序（23, 3, 99），方便觀察排序效果。
users = [User(23), User(3), User(99)]
print("=== attrgetter 物件排序範例 ===")
print(f"排序前：{users}")

# sorted 會回傳「新列表」，不會改動原本的 users。
# key=attrgetter('user_id') 表示：
# 1) sorted 逐一拿出每個 User 物件
# 2) 用 attrgetter 取出 user_id 當作比較依據
# 3) 依 user_id 由小到大排列
#
# 它等價於：sorted(users, key=lambda u: u.user_id)
# 但 attrgetter 在語意上更直接，通常也更簡潔。
sorted_users = sorted(users, key=attrgetter('user_id'))
print(f"排序後（依 user_id 由小到大）：{sorted_users}")
