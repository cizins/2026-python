# U03. 文字 vs 位元組、編碼觀念（5.1 encoding / 5.4）
# Bloom: Understand — 能解釋什麼時候用 'rb'、為什麼要指定 encoding

from pathlib import Path

# 本檔案核心重點：
# 1) Python 的 str（文字）與 bytes（位元組）是兩種截然不同的型別
# 2) encode / decode 是二者轉換的橋樑，必須指定編碼標準
# 3) 寫錯 encoding 會導致亂碼或解碼錯誤
# 4) 二進位檔案（PNG、ZIP 等）一定要用 'rb'/'wb' 讀寫

# ── 5.4 二進位讀寫：圖片、zip、任何非文字 ───────────────
# 所有非文字檔（圖片、ZIP、執行檔等）都含有隨意位元組序列。
# 這些位元組無法「解碼」成有意義的文字，只能當 bytes 處理。
# 
# 先造一個「假 PNG」：只寫前 8 bytes 的 magic number。
# PNG 檔案的開頭總是固定的 8 位元組序列（稱為 magic number），
# 用來識別「這真的是 PNG 檔」而不是其他格式。
magic = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])
# write_bytes() 是 Path 提供的便利方法，直接寫 bytes 不需指定 encoding。
Path("fake.png").write_bytes(magic)

# 讀回前 8 bytes，對照 PNG 檔頭。
# 'rb' 模式表示「二進位讀取」，檔案操作直接回傳 bytes 物件。
with open("fake.png", "rb") as f:
    # f.read(8) 讀取最多 8 位元組，傳回 bytes 物件。
    head = f.read(8)
# 十六進制表示法：\x89 表示十進制 137，\r 是回車符（0x0D），\n 是換行（0x0A）。
print(head)           # b'\x89PNG\r\n\x1a\n'
# bytes 物件支援 == 比較，檢驗是否與預期 magic number 一致。
print(head == magic)  # True

# bytes 可逐位元組迭代。
# 每次迭代得到的是整數（int），代表該位元組的十進制值（0～255）。
# hex() 函數可把十進制轉成十六進制字串（方便人類閱讀）。
for b in head[:4]:
    # 例如 0x89 在十進制是 137。
    print(b, hex(b))

# ── 文字 vs 位元組的型別差異與轉換 ─────────────────────────────
# Python 區分 str（文字序列）與 bytes（位元組序列）兩種型別。
# 在磁碟或網路傳輸時，文字必須「編碼」成位元組序列。
# 讀回時，位元組必須「解碼」回文字。
s = "你好"
# encode(encoding) 把字串轉成位元組。
# UTF-8 是現代 Python 預設編碼，中文字會佔 3～4 位元組。
b = s.encode("utf-8")   # str → bytes
print(s, type(s))       # <class 'str'>
print(b, type(b))       # <class 'bytes'>
# decode(encoding) 把位元組轉回字串，必須用相同的編碼標準。
print(b.decode("utf-8"))  # bytes → str

# ── 5.1 encoding 參數：寫錯會爛掉 ──────────────────────
# write_text() 與 read_text() 都需要指定 encoding，
# 否則 Python 會用系統預設編碼（Windows 可能是 GBK，Mac/Linux 通常是 UTF-8）。
# 為了跨平台相容，建議一律顯式指定 encoding='utf-8'。
Path("zh.txt").write_text("中文測試\n", encoding="utf-8")

# 情況 1（正確）：用 UTF-8 讀用 UTF-8 寫的檔。
# 編碼標準一致，檔案內容正確顯示。
print(Path("zh.txt").read_text(encoding="utf-8"))

# 情況 2（錯誤）：用 Big5 讀用 UTF-8 寫的檔。
# 位元組序列的詮釋方式不同，會導致亂碼或拋出 UnicodeDecodeError。
# Big5 是臺灣/香港常用的舊編碼，與 UTF-8 位元組結構截然不同。
try:
    print(Path("zh.txt").read_text(encoding="big5"))
except UnicodeDecodeError as e:
    # 這個例外說明哪裡發生解碼失敗，方便除錯。
    print("解碼錯誤:", e)

# ╭─ 小結與最佳實踐 ──────────────────────────────────────╮
# │                                                     │
# │ 文字檔（.txt/.csv/.py 等）：                        │
# │   1. 讀取：open(..., 'rt', encoding='utf-8')        │
# │   2. 寫入：open(..., 'wt', encoding='utf-8')        │
# │   3. 便利方法：Path.read_text/write_text(...)       │
# │   4. 一律明示 encoding='utf-8'，無論系統預設       │
# │                                                     │
# │ 二進位檔（.png/.zip/.exe/.pkl 等）：              │
# │   1. 讀取：open(..., 'rb')                          │
# │   2. 寫入：open(..., 'wb')                          │
# │   3. 便利方法：Path.read_bytes/write_bytes()        │
# │   4. 完全不涉及 encoding 參數                        │
# │                                                     │
# ╰─────────────────────────────────────────────────────╯
