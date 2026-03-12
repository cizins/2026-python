# R13. 字典列表排序 itemgetter（1.13）

# 從 operator 匯入 itemgetter。
# itemgetter('fname') 會建立一個函式：給它一筆字典資料，
# 它會回傳該字典中 key='fname' 的值。
# 這種函式常用在 sorted(..., key=...) 當作「排序依據」。
from operator import itemgetter

# rows 是「字典組成的列表」，每個字典代表一筆資料。
# 例如第一筆：{'fname': 'Brian', 'uid': 1003}
# 可以理解為：名字是 Brian，使用者編號是 1003。
rows = [{'fname': 'Brian', 'uid': 1003}, {'fname': 'John', 'uid': 1001}]

# 依 fname（名字）排序。
# key=itemgetter('fname') 等價於 key=lambda r: r['fname']
# sorted 會回傳新列表，不會修改原本 rows。
sorted_by_fname = sorted(rows, key=itemgetter('fname'))

# 依 uid（使用者編號）排序。
# key=itemgetter('uid') 等價於 key=lambda r: r['uid']
sorted_by_uid = sorted(rows, key=itemgetter('uid'))

# 多欄位排序：先 uid，再 fname。
# itemgetter('uid', 'fname') 會回傳一個 tuple，像 (1001, 'John')。
# Python 會對 tuple 進行字典序比較：
# 1) 先比第一個元素 uid
# 2) 若 uid 相同，才比第二個元素 fname
sorted_by_uid_then_fname = sorted(rows, key=itemgetter('uid', 'fname'))
