# R18. namedtuple（1.18）

# namedtuple 讓你建立「具欄位名稱」的 tuple 類型。
# 相較於一般 tuple 用索引存取（如 x[0]），
# namedtuple 可用屬性名稱存取（如 x.addr），可讀性更好。
from collections import namedtuple

# 定義一個 Subscriber 類型，包含 addr（信箱）與 joined（加入日期）兩個欄位。
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])

# 以欄位順序建立實例。
sub = Subscriber('jonesy@example.com', '2012-10-19')

# 透過屬性名稱讀值，語意比索引 sub[0] 更清楚。
sub.addr

# 再定義一個 Stock 類型，表示股票資料。
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock('ACME', 100, 123.45)

# namedtuple 是「不可變（immutable）」的，
# 不能直接寫 s.shares = 75。
# _replace(...) 會回傳「新的」namedtuple 實例，
# 並替換指定欄位值；原本的 s 不會被原地修改。
s = s._replace(shares=75)
