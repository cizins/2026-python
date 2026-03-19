# R01. 字串分割與匹配（2.1–2.3）
# 這個範例展示了 Python 中處理字串常見的三種技巧：
# 1. 使用正規表示式 (re) 處理多種不同界定符的字串分割。
# 2. 使用 startswith / endswith 檢查字串的開頭與結尾。
# 3. 使用 fnmatch 進行類似 Shell 命令列的通配符 (Wildcard) 匹配。

import re
from fnmatch import fnmatch, fnmatchcase

# ── 2.1 多界定符分割 (re.split) ──────────────────────────────────
# 當字串中的分隔符不只一種（例如同時有逗號、分號、空白），
# 內建的 str.split() 只能接受單一字串作為分隔符，這時就需要 re.split()。
line = "asdf fjdk; afed, fjek,asdf, foo"

# r"[;,\s]\s*" 的意思是：
# [;,\s] 匹配單一個分號、逗號或空白字元（空格、tab）。
# \s*    匹配 0 個或多個跟在後面的空白字元。
# 這樣就能完美處理像是 ", " 或 ";" 這種後面帶有不定數量空白的狀況。
print("正規表示式分割:", re.split(r"[;,\s]\s*", line))
# 預期結果: ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# 什麼是非捕獲分組 (Non-capturing group)？
# 如果我們在 re.split 中使用一般括號 (...) 來分組，re.split 會「連同分隔符本身」一起保留到結果陣列中。
# 如果我們需要用括號來建立邏輯 (例如 A|B|C)，但「不想」把分隔符保留在結果裡，
# 就要在括號內開頭加上 `?:`，變成 `(?:...)`，這就是非捕獲分組。
print("非捕獲分組分割:", re.split(r"(?:,|;|\s)\s*", line))
# 預期結果: ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']


# ── 2.2 開頭/結尾匹配 (startswith / endswith) ────────────────────────────────
# 要檢查字串的開頭或結尾，使用內建的字串方法最快也最乾淨。
filename = "spam.txt"
print("是否以 .txt 結尾:", filename.endswith(".txt"))  # True
print("是否以 file: 開頭:", filename.startswith("file:"))  # False

# 核心技巧：同時檢查多種後綴 (或前綴)
# 當你需要檢查多種可能性時，可以將這些後綴放進一個 Tuple 中傳入。
# 注意：這裡「必須」是 Tuple (元組)，如果你傳入 List (串列) 或 Set，會引發 TypeError 錯誤！
filenames = ["Makefile", "foo.c", "bar.py", "spam.c", "spam.h"]
c_or_h_files = [name for name in filenames if name.endswith((".c", ".h"))]
print("C 語言相關檔案:", c_or_h_files)
# 預期結果: ['foo.c', 'spam.c', 'spam.h']


# ── 2.3 Shell 通配符匹配 (fnmatch) ─────────────────────────────
# 有時候用正規表示式太牛刀小用了，如果你只需要像在終端機 (Terminal) 裡找檔案那樣：
# 用 `*.txt` 代表所有 txt 檔，或者 `?` 代表單一字元，你可以使用 fnmatch 模組。

print("匹配 *.txt:", fnmatch("foo.txt", "*.txt"))  # True
# [0-9] 代表匹配任何一個單一數字字元，* 代表後續任意長度的字元
print("匹配 Dat[0-9]*:", fnmatch("Dat45.csv", "Dat[0-9]*"))  # True

# 大小寫問題 (fnmatch vs fnmatchcase)
# fnmatch() 的大小寫敏感與否，是「取決於你的作業系統」！
# 在 Mac/Windows 上通常不分大小寫，但在 Linux 上通常區分大小寫。
# 為了讓程式碼在不同系統上行為一致，如果你需要「強制區分大小寫」，請使用 `fnmatchcase`。
print("強制區分大小寫匹配:", fnmatchcase("foo.txt", "*.TXT"))  # False

# 實務應用範例：過濾特定結尾的地址
addresses = ["5412 N CLARK ST", "1060 W ADDISON ST", "1039 W GRANVILLE AVE"]
st_addresses = [a for a in addresses if fnmatchcase(a, "* ST")]
print("結尾是 ST 的地址:", st_addresses)
# 預期結果: ['5412 N CLARK ST', '1060 W ADDISON ST']