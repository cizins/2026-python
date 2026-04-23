# U04. 類檔案物件 StringIO 與逐行處理（5.6 / 5.1 逐行）
# Bloom: Understand — 知道 file-like 是鴨子型別，能把記憶體當檔案用

import io
from pathlib import Path

# 本檔案重點：
# 1) StringIO 是類似檔案的物件，住在記憶體不是磁碟
# 2) File-like 介面：有 read/write/seek 方法就可以彼此使用
# 3) 鴨子型別（Duck Typing）：不管是真檔案或 StringIO，
#    只要行為一樣就能用
# 4) 適合在沒有磁碟、檔案不存在的情況下測試

# ── 5.6 StringIO：記憶體裡的「假檔案」 ─────────────────
# StringIO 是 io 模組提供的「記憶體串流」（in-memory text stream）。
# StringIO 是記憶體串流，數據住記憶體不是磁碟。
buf = io.StringIO()
# print(..., file=buf) 把輸出導向 StringIO 物件，而不是控制臺。
print("第一行", file=buf)
print("第二行", file=buf)
print("第三行", file=buf)

# 取出整段字串。getvalue() 是 StringIO 特有的方法。
text = buf.getvalue()
print("---StringIO 內容---")
print(text)

# 也能當讀檔用：seek() 回到開頭。
buf.seek(0)
# 逐行迭代 StringIO，每次只讀一行到記憶體。
for i, line in enumerate(buf, 1):
    # rstrip() 去掉行尾的換行符 \n。
    print(i, line.rstrip())

# 為什麼有用？鴨子型別的強大之處。
# 任何接口如果預期接受 file-like 物件（通常是檔案），
# 你都可以塞 StringIO 進去，不必真的寫磁碟。
# 被用情況：單元測試、後處理、日誌阻止器。
import csv
# 在記憶體中建立一個 CSV 庫（不寫磁碟）。
mem = io.StringIO()
writer = csv.writer(mem)
writer.writerow(["name", "score"])
writer.writerow(["alice", 90])
print("---CSV in memory---")
# 透過 getvalue() 取出 CSV 文本，可以獨立檢查或用於接下來的處理。
print(mem.getvalue())

# ── 5.1 延伸：逐行處理檔案（大檔友善） ─────────────────
# 逐行迭代的最大優勢：永遠只會在記憶體存一行（不管檔案大小）。
# 對比 read() 一次讀全部，大檔案容易 OOM。
# 先造一個多行檔案，含有空行。
src = Path("poem.txt")
src.write_text("床前明月光\n\n疑是地上霜\n\n舉頭望明月\n低頭思故鄉\n", encoding="utf-8")

# 任務：過濾空行、加上行號、寫到新檔。
# 這是逐行處理大檔案的實務範本。
dst = Path("poem_numbered.txt")
# 串聯多個 with 敘述，永遠有效處理至二個檔案同時開放。
with open(src, "rt", encoding="utf-8") as fin, \
     open(dst, "wt", encoding="utf-8") as fout:
    n = 0
    # 逐行迭代輸入檔。每次迴圈只處理一行。
    for line in fin:               # 逐行：一次只讀一行到記憶體
        line = line.rstrip()
        # 空行是「只含 \n」的行，rstrip 後會變成空字串。
        if not line:
            continue               # 跳過空行（不記行號）
        n += 1
        # 整數格式字符：:02d 表示「至少 2 位，前導零」。
        print(f"{n:02d}. {line}", file=fout)

print("---加行號後---")
# 讀新檔並日誌結果，驗證逐行處理是否正確。
print(dst.read_text(encoding="utf-8"))
