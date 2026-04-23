# R01. 文本 I/O 基本式（5.1 / 5.2 / 5.3 / 5.17）
# Bloom: Remember — 會叫出 open/print 的基本參數

from pathlib import Path

# 本檔案聚焦在「文字檔 I/O」的基本功：
# 1) 如何開啟與關閉檔案（建議使用 with）
# 2) 如何指定模式 mode（讀/寫/附加 + 文字模式）
# 3) 如何處理編碼 encoding（避免亂碼）
# 4) print() 寫檔時常用參數（file / sep / end）
# 5) 文字模式與位元組模式型別不相容的常見錯誤

# ── 5.1 讀寫文本檔 ─────────────────────────────────────
# 寫入：mode='wt'（預設 't'），一定要指定 encoding
# Path 物件可讀性高，也方便後續做跨平台路徑操作。
path = Path("hello.txt")
with open(path, "wt", encoding="utf-8") as f:
    # with 區塊結束後會自動 close()，
    # 即使中途例外也會嘗試正確釋放檔案資源。
    # 'w' 代表覆寫（檔案存在會清空重寫，不存在則建立）。
    f.write("你好，Python\n")
    f.write("第二行\n")

# 讀回：一次讀完 vs 逐行讀
with open(path, "rt", encoding="utf-8") as f:
    # f.read() 一次把整個檔案內容讀進記憶體。
    # 適合小檔案，若檔案過大可能造成記憶體負擔。
    print(f.read())  # 一次讀完（小檔才適合）

with open(path, "rt", encoding="utf-8") as f:
    # 檔案物件本身可被迭代，會逐行回傳字串。
    # 這是處理大檔最常見且穩定的寫法。
    for line in f:  # 大檔必備：逐行迭代
        # rstrip() 去掉尾端換行，避免 print 再補一個換行導致空白行。
        print(line.rstrip())

# ── 5.2 print 導向檔案 ─────────────────────────────────
with open("log.txt", "wt", encoding="utf-8") as f:
    # print(..., file=f) 可直接把輸出導向檔案。
    # 好處是語法簡潔，且自動處理字串化與換行。
    print("登入成功", file=f)
    print("使用者:", "alice", file=f)

# ── 5.3 調整分隔符與行終止符 ───────────────────────────
fruits = ["apple", "banana", "cherry"]
with open("fruits.csv", "wt", encoding="utf-8") as f:
    # *fruits 會把清單拆成多個參數交給 print。
    # sep="," 指定欄位分隔符，end="\n" 指定行結尾。
    # 這種寫法可快速輸出簡單 CSV 形式的一行資料。
    print(*fruits, sep=",", end="\n", file=f)

# end='' 可避免多一個換行
with open("fruits.csv", "at", encoding="utf-8") as f:
    # 'a' 代表附加（append）：保留舊內容，在檔案尾端新增。
    # 第一個 print 設 end=","，避免換行並在尾端補逗號。
    print("date", end=",", file=f)
    # 第二個 print 用預設 end='\n' 收尾成完整一行。
    print("2026-04-23", file=f)

# read_text() 是 Path 提供的便利方法，
# 等同 open(...).read() 的精簡版，適合快速讀小檔。
print(Path("fruits.csv").read_text(encoding="utf-8"))
# apple,banana,cherry
# date,2026-04-23

# ── 5.17 文字模式 vs 位元組模式提醒 ────────────────────
# 'wt' 寫 str、'wb' 寫 bytes；寫錯型別會 TypeError
try:
    with open("bad.txt", "wt", encoding="utf-8") as f:
        # 文字模式（t）期望寫入 str。
        # 下面刻意傳入 bytes，會觸發 TypeError，
        # 用來示範常見的新手錯誤。
        f.write(b"bytes in text mode")  # ← 會錯
except TypeError as e:
    # 捕捉並印出錯誤，方便在教學中觀察型別不匹配的訊息。
    print("錯誤示範:", e)
