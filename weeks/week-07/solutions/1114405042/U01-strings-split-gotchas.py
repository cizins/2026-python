# U01. 字串分割與匹配的陷阱（2.1–2.11）
# 說明：本程式碼示範了 Python 中常見的幾個字串處理陷阱與正確做法：
# 1. 使用正規表達式分割字串時，如何保留分隔符。
# 2. string.startswith() 判斷多個前綴條件時，必須傳入 tuple 而非 list。
# 3. string.strip() 只能清除字串頭尾的空白字元，對於中間多餘的空白無效。

import re

# ── 捕獲分組保留分隔符（2.1）─────────────────────────
line = "asdf fjdk; afed, fjek,asdf, foo"
# 陷阱：直接使用 re.split() 切割會導致原本的逗號、分號等分隔符遺失。
# 解法：將分隔符號包在括號內 `(;|,|\s)` 形成「捕獲分組」(capture group)。
# 這樣切割後，陣列中不僅會包含被切割出來的值，也會包含切割用的分隔符。
fields = re.split(r"(;|,|\s)\s*", line)

# 從 fields 取出實際的字串值（因為包含了分隔符，所以實際值會在 0, 2, 4... 等偶數索引）
values = fields[::2]  

# 從 fields 取出分隔符（分隔符會在 1, 3, 5... 等奇數索引）
# 因為最後一個值後面沒有分隔符了，所以手動在陣列最後補上一個空字串 [""]，以確保 zip 時兩邊長度一致
delimiters = fields[1::2] + [""]

# 利用 zip 將「值」與「分隔符」一對一綁定，並用 join 重新組裝回原本的字串形式
# 這確保了我們只清除了逗號或分號後面不必要的空白，但保留了原本的標點符號
rebuilt = "".join(v + d for v, d in zip(values, delimiters))
print(rebuilt)  # 輸出: 'asdf fjdk;afed,fjek,asdf,foo'


# ── startswith 必須傳 tuple（2.2）────────────────────
url = "http://www.python.org"
choices = ["http:", "ftp:"]

try:
    # 陷阱：如果我們想檢查字串開頭是否符合 `choices` 裡的其中一項，
    # startswith / endswith 方法「不接受」list 格式的參數，會引發 TypeError。
    url.startswith(choices)  # type: ignore[arg-type]
except TypeError as e:
    print(f"TypeError: {e}")  # 這裡會印出錯誤：不能傳 list！

# 解法：必須先將 list 轉型為 tuple（元組），這樣 startswith 就能一次檢查多個條件
print(url.startswith(tuple(choices)))  # 輸出: True（轉成 tuple 才行）


# ── strip 只處理頭尾，不處理中間（2.11）──────────────
s = "  hello     world  "

# 陷阱 1：strip() 只會清除字串最左邊與最右邊的空白，夾在單字中間的多餘空白還會留著。
print(repr(s.strip()))  # 輸出: 'hello     world'（中間多餘空白還在）

# 陷阱 2：如果用 replace 把所有空格換成空字串，又會清得太乾淨，導致正常的單字間隔也消失。
print(repr(s.replace(" ", "")))  # 輸出: 'helloworld'（過頭，連詞間空白也消）

# 正確解法：先用 strip() 去除頭尾空白，再利用正規表達式 `re.sub` 把中間一個以上的空白（\s+）替換為單一空格。
print(repr(re.sub(r"\s+", " ", s.strip())))  # 輸出: 'hello world'（正確）

# ── 補充：生成器逐行清理（高效，不預載入記憶體） ─────────
lines = ["  apple  \n", "  banana  \n"]
# 利用生成器表達式 (generator expression) `(l.strip() for l in lines)`
# 這種寫法不會一次把所有清理完的字串載入記憶體中，而是要多少給多少，適合處理超大檔案
for line in (l.strip() for l in lines):
    print(line)
