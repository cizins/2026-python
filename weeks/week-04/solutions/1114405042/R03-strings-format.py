# R03. 字串清理、對齊、拼接與格式化（2.11–2.16）
# 這個範例展示了 Python 字串處理中非常實用的內建方法：
# 去除多餘字元 (strip)、排版對齊 (ljust/rjust/center)、高效率的字串串接 (join)、
# 動態變數插入 (format/f-string) 以及處理過長文字的換行 (textwrap)。

import textwrap

# ── 2.11 清理字元 (strip) ─────────────────────────────────────
s = "  hello world \n"

# strip() 預設會去除字串「頭尾」的任何空白字元 (包含空格、tab \t、換行 \n)
# 注意：它不會影響字串「中間」的空白。
# repr() 可以讓我們在終端機印出時，清楚看到字串周圍的空白或換行符號。
print("去除頭尾空白:", repr(s.strip()))  # 'hello world'

# lstrip() 只去除左邊 (開頭)，rstrip() 只去除右邊 (結尾)
print("只去除左邊空白:", repr(s.lstrip()))  # 'hello world \n'

# strip() 也可以接受一個字串參數，告訴它要去除哪些「特定字元」。
# 它會從兩端開始剝除，只要遇到包含在 "-=" 裡面的字元就拔掉，直到遇到第一個不是 "-=" 的字元為止。
print("去除特定字元:", repr("-----hello=====".strip("-=")))  # 'hello'


# ── 2.13 字串對齊 (ljust, rjust, center, format) ─────────────────────────────────────
text = "Hello World"

# ljust(20) 代表將字串靠左對齊，總寬度設定為 20，不夠的部分預設補空白。
print("靠左對齊:", repr(text.ljust(20)))  # 'Hello World         '
print("靠右對齊:", repr(text.rjust(20)))  # '         Hello World'

# center(20, "*") 代表置中對齊，並指定不夠的部分用 "*" 填滿
print("置中對齊補星星:", repr(text.center(20, "*")))  # '****Hello World*****'

# 也可以使用 format() 函數來排版，這是比較現代且統一的做法：
# "^20" 代表置中且寬度 20 ( < 代表靠左, > 代表靠右 )
print("使用 format 置中:", repr(format(text, "^20")))  # '    Hello World     '

# format 非常強大，還能同時處理數字的排版：
# ">10.2f" 代表靠右對齊、總寬度 10、強制顯示小數點後 2 位
print("數字格式化排版:", repr(format(1.2345, ">10.2f")))  # '      1.23'


# ── 2.14 合併拼接 (join) ─────────────────────────────────────
parts = ["Is", "Chicago", "Not", "Chicago?"]

# 為什麼不用 `+` 來串接陣列裡的字串？
# 因為每次使用 `+`，Python 都要在記憶體裡建立一個新的字串物件，效能極差。
# 使用 "分隔符".join(list) 可以在底層一次性配置好記憶體，是最高效的做法。
print("用空白串接:", repr(" ".join(parts)))  # 'Is Chicago Not Chicago?'
print("用逗號串接:", repr(",".join(parts)))  # 'Is,Chicago,Not,Chicago?'

# 如果陣列裡面混雜了非字串的型別 (如數字)，直接 join 會報錯 (TypeError)。
# 我們可以搭配「生成器運算式 (Generator Expression)」在串接前將它們轉為字串。
data = ["ACME", 50, 91.1]
print("含數字的串接:", repr(",".join(str(d) for d in data)))  # 'ACME,50,91.1'


# ── 2.15 插入變量 (format, format_map, f-string) ─────────────────────────────────────
name, n = "Guido", 37

# 方法一：傳統的 format()，透過指定關鍵字參數來填入 `{}` 的位置
s = "{name} has {n} messages."
print("format() 寫法:", s.format(name=name, n=n))

# 方法二：format_map()，如果你有很多變數，可以直接傳入一個字典。
# vars() 是一個內建函數，會回傳當下所有區域變數所組成的字典。
print("format_map(vars()) 寫法:", s.format_map(vars()))

# 方法三：f-string (Python 3.6+ 加入)。
# 這是目前最推薦、最簡潔且執行速度最快的寫法！直接在字串前加上 f，並把變數塞進 `{}` 即可。
print("f-string 寫法:", f"{name} has {n} messages.")


# ── 2.16 指定列寬自動換行 (textwrap) ─────────────────────────────────────
long_s = (
    "Look into my eyes, look into my eyes, the eyes, "
    "not around the eyes, look into my eyes, you're under."
)

# 當你有很長一段文字要在終端機顯示，為了避免太長難以閱讀，可以使用 textwrap.fill()
# 它會聰明地在「單字之間」找到合適的空格幫你切斷並插入換行符號 \n，讓每一行都不超過指定寬度 (這裡為 40)。
print("\n=== textwrap 自動換行 (寬度 40) ===")
print(textwrap.fill(long_s, 40))

# 還可以透過 initial_indent 設定「第一行」開頭要縮排幾個空白。
print("\n=== textwrap 第一行縮排 ===")
print(textwrap.fill(long_s, 40, initial_indent="    "))