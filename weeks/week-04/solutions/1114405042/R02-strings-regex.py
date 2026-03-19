# R02. 正則表達式：搜尋、替換、旗標（2.4–2.8）
# 這個範例展示了 Python 中強大的 re (正規表示式) 模組的各種進階操作，
# 包括：預編譯、群組提取、字串替換、以及如何使用各種旗標 (Flags) 來改變匹配行為。

import re

# ── 2.4 匹配和搜尋 (findall, match, finditer) ────────────────────────────────────
text = "Today is 11/27/2012. PyCon starts 3/13/2013."

# 效能優化：re.compile()
# 如果同一個正規表示式會被多次使用，先用 re.compile() 將其「預編譯」成 Pattern 物件，可以大幅提升效能。
# `r` 前綴代表 Raw String (原始字串)，這樣我們就不需要為了反斜線跳脫而寫成 "\\d"。
# `\d+` 代表匹配一個或多個數字，外面的括號 `(...)` 稱為「捕獲群組 (Capturing Group)」，方便後續提取資料。
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")

# findall() 會找出字串中「所有」符合的子字串。
# 因為我們有設定捕獲群組，所以它會回傳一個包含 Tuple 的 List。
print("所有匹配結果 (findall):", datepat.findall(text))
# 預期結果: [('11', '27', '2012'), ('3', '13', '2013')]

# match() 只會從字串的「最開頭」開始嘗試匹配。
m = datepat.match("11/27/2012")
if m:
    # m.group(0) 代表整個匹配到的字串
    # m.groups() 則會回傳所有捕獲群組組成的 Tuple
    print("開頭匹配成功:", m.group(0), "提取群組:", m.groups())

# finditer() 和 findall 類似，但它會回傳一個迭代器 (Iterator)，每次吐出一個 Match 物件。
# 這在處理超大字串時非常節省記憶體，且可以對每個匹配結果做細緻的操作。
print("使用 finditer 逐一處理:")
for m in datepat.finditer(text):
    month, day, year = m.groups()
    print(f"  轉換格式: {year}-{month}-{day}")


# ── 2.5 搜尋和替換 (sub, subn) ───────────────────────────────────
# re.sub() 用來做進階的「尋找並取代」。
# 在替換字串 (第二個參數) 中，可以使用 `\1`, `\2`, `\3` 來反向參考 (Backreference) 剛剛匹配到的捕獲群組。
print("\n替換字串 (re.sub):", re.sub(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text))
# 預期結果: 'Today is 2012-11-27. PyCon starts 2013-3-13.'

# 命名群組 (Named Group)
# 如果群組太多，用數字 `\1` 容易搞混，可以在正規表示式中用 `?P<名稱>` 給群組取名字。
# 替換時則用 `\g<名稱>` 來呼叫它，這樣程式碼的可讀性會高非常多！
print("使用命名群組替換:", 
    re.sub(
        r"(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)",
        r"\g<year>-\g<month>-\g<day>",
        text,
    )
)

# re.subn() 則會多回傳一個資訊：總共替換了幾次。回傳格式為 Tuple: (新字串, 替換次數)
newtext, n = re.subn(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text)
print(f"總共替換了 {n} 次")


# ── 2.6 忽略大小寫 (IGNORECASE) ───────────────────────────────────
# 加入 flags=re.IGNORECASE (或 re.I)，可以讓比對不分大小寫。
s = "UPPER PYTHON, lower python, Mixed Python"
print("\n忽略大小寫匹配:", re.findall("python", s, flags=re.IGNORECASE))
# 預期結果: ['PYTHON', 'python', 'Python']


# ── 2.7 非貪婪匹配（最短匹配）────────────────────────────
text2 = 'Computer says "no." Phone says "yes."'

# 正規表示式中的 `*` 預設是「貪婪 (Greedy)」的，它會盡可能吃掉最多的字元。
# 所以它會從第一個引號開始，一直吃到「整句話最後一個引號」才停下來！
print("貪婪匹配:", re.compile(r'"(.*)"').findall(text2))  
# 預期結果: ['no." Phone says "yes.'] (糟糕！吃太多了)

# 解決方法：在 `*` 後面加上 `?`，變成 `*?`。
# 這代表「非貪婪 (Non-greedy) / 最小匹配」，它一遇到下一個符合的字元 (引號) 就會立刻停手。
print("非貪婪匹配:", re.compile(r'"(.*?)"').findall(text2))  
# 預期結果: ['no.', 'yes.'] (正確拆開了兩個引號內的內容)


# ── 2.8 多行匹配（DOTALL 旗標）────────────────────────────
code = "/* this is a\nmultiline comment */"

# 在正規表示式中，點號 `.` 預設可以匹配「除了換行符號 (\n) 以外」的所有字元。
# 所以如果你的註解橫跨了多行 (裡面有 \n)，預設情況下 `.` 是無法跨行匹配的。
# 加上 flags=re.DOTALL (或 re.S)，可以讓 `.` 的超能力升級，連換行符號也一起匹配進去！
print("\n多行註解匹配 (使用 DOTALL):", re.compile(r"/\*(.*?)\*/", re.DOTALL).findall(code))
# 預期結果: [' this is a\nmultiline comment ']