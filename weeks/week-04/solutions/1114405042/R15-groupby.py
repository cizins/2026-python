# R15. 分組 groupby（1.15）

# groupby 會把「連續且鍵值相同」的元素分成同一組。
# 也就是說，它不是先掃完全部資料再做全域分組，
# 而是邊走邊分，因此通常要先依照分組鍵排序。
from itertools import groupby
# itemgetter('date') 可快速取得每筆資料中的 date 欄位，
# 常用在 sort 的 key 與 groupby 的 key。
from operator import itemgetter

# 範例資料：每個元素是一筆 dict，含日期與地址。
rows = [{'date': '07/01/2012', 'address': '...'}, {'date': '07/02/2012', 'address': '...'}]

# 先依 date 排序是 groupby 正確分組的關鍵。
# 若未排序，groupby 只會把「相鄰」的同日期資料放在一起，
# 同日期但分散在不同位置時會被拆成多段群組。
rows.sort(key=itemgetter('date'))

# 外層迴圈：每次取得一個群組的鍵值（date）與該群組的迭代器（items）。
# 注意 items 是 iterator，不是 list；讀過一次就會被消耗。
for date, items in groupby(rows, key=itemgetter('date')):
    # 內層迴圈：走訪同一日期群組裡的每一筆資料。
    # 實務上可在此做統計、輸出或彙整。
    for i in items:
        # 這份教材範例先保留空操作，聚焦在 groupby 的使用方式。
        pass
