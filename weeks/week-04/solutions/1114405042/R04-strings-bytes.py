# R04. 位元組字串操作（2.20）
#
# 本範例示範 Python 中 bytes（不可變）與 bytearray（可變）
# 在「常見字串操作」上的用法，以及它們和一般 str 的關鍵差異。
#
# 觀念先記住：
# 1) str 是「文字」（Unicode）
# 2) bytes 是「原始位元資料」（0~255 的整數序列）
#
# 因此，當資料是檔案內容、網路封包、二進位協定時，通常會先用 bytes；
# 真正要顯示或做文字語意處理時，再 decode 成 str。

import re

# 建立一個 bytes 物件（前面加 b 前綴）
data = b"Hello World"

# 切片行為和字串很像，仍然回傳 bytes
print(data[0:5])  # b'Hello'

# startswith() 可用於檢查 bytes 前綴（參數也必須是 bytes）
print(data.startswith(b"Hello"))  # True

# split() 預設以空白分割，結果是由 bytes 組成的 list
print(data.split())  # [b'Hello', b'World']

# replace() 同樣可用於 bytes 取代（新舊值都需是 bytes）
print(data.replace(b"Hello", b"Hello Cruel"))  # b'Hello Cruel World'

# 正則表達式也必須使用 bytes 模式：
# - 模式字串要寫成 rb"..."（raw bytes 字面值）
# - 被匹配資料也要是 bytes
raw = b"FOO:BAR,SPAM"
# 以 ':' 或 ',' 作為分隔符號
print(re.split(rb"[:,]", raw))  # [b'FOO', b'BAR', b'SPAM']

# 差異 1：索引回傳值不同
# - str 索引回傳「字元」
# - bytes 索引回傳「整數」（該位元組的數值）
a = "Hello"
b = b"Hello"
print(a[0])  # 'H'（字元）
print(b[0])  # 72（整數，即 ord('H')）

# 差異 2：bytes 沒有 str.format() 這種格式化流程
# 常見做法：
# 1) 先在 str 上做 format()
# 2) 再 encode() 成 bytes（此處用 ascii）
# 注意：若字串中有 ASCII 以外的字元，encode("ascii") 會噴錯
formatted = "{:10s} {:10d}".format("ACME", 100).encode("ascii")
print(formatted)  # b'ACME            100'
