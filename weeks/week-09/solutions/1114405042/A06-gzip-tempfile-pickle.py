# A06. 壓縮檔、臨時資料夾、物件序列化（5.7 / 5.19 / 5.21）
# Bloom: Apply — 能把標準庫工具組合起來解一個小任務

import gzip
import pickle
import tempfile
from pathlib import Path

# 本檔案示範三個常見但很實用的標準庫工具：
# 1) gzip：直接讀寫壓縮檔，介面幾乎和 open 一樣
# 2) tempfile：建立臨時資料夾或臨時檔，離開作用域後自動清理
# 3) pickle：把 Python 物件直接序列化成 bytes 再存檔
# 注意：這三者的用途完全不同，分別對應壓縮、暫存、物件保存

# ── 5.7 讀寫壓縮檔：gzip.open 幾乎和 open 一樣 ─────────
# gzip.open 的用法和 open 非常像，只是資料會在讀寫時自動壓縮/解壓縮。
# 若處理的是文字內容，仍然要指定 encoding，否則會回到預設編碼。
# .gz 常用在日誌、備份、資料交換，能有效節省磁碟空間。
with gzip.open("notes.txt.gz", "wt", encoding="utf-8") as f:
    # 'wt' 表示「文字寫入」：先把字串用 UTF-8 編碼，再壓縮寫到檔案。
    f.write("第一行筆記\n")
    f.write("第二行筆記\n")

# 讀回時也可以像一般文字檔一樣逐行迭代。
# 'rt' 表示「文字讀取」：先解壓縮，再用 UTF-8 解碼回字串。
with gzip.open("notes.txt.gz", "rt", encoding="utf-8") as f:
    for line in f:
        # rstrip() 去掉行尾換行，避免 print 再補一個換行造成空白行。
        print("gz:", line.rstrip())

# 也能直接處理二進位資料，例如圖片、模型檔、原始 bytes。
# 'wb'/'rb' 代表二進位模式，不涉及 encoding。
with gzip.open("blob.bin.gz", "wb") as f:
    f.write(b"\x00\x01\x02\x03")

# stat().st_size 可以查看壓縮檔目前的磁碟大小。
# 注意這是壓縮後的大小，不是原始資料大小。
print("blob size:", Path("blob.bin.gz").stat().st_size, "bytes")

# ── 5.19 臨時檔案與資料夾：離開 with 自動清理 ──────────
# 場景：想跑個小實驗，但不想在專案資料夾留下多餘檔案。
# TemporaryDirectory 會建立一個隨機命名的暫存資料夾，
# 離開 with 區塊後通常會自動刪除整個目錄樹。
with tempfile.TemporaryDirectory() as tmp:
    # 傳回來的 tmp 一開始是字串路徑，轉成 Path 後比較好做路徑運算。
    tmp = Path(tmp)
    print("暫存資料夾:", tmp)

    # 在暫存資料夾裡建立幾個測試檔。
    # 這些檔案只會活在 with 區塊內，離開後不需要手動清理。
    (tmp / "a.txt").write_text("hello\n", encoding="utf-8")
    (tmp / "b.txt").write_text("world\n", encoding="utf-8")

    # iterdir() 只列出目前目錄層級的內容，不會遞迴。
    for p in tmp.iterdir():
        print("  ", p.name, "→", p.read_text(encoding="utf-8").rstrip())

# 離開 with 後，TemporaryDirectory 會自動清理；此時路徑通常已不存在。
print("離開後還存在嗎？", tmp.exists())  # False

# 單一臨時檔：NamedTemporaryFile
# 適合只想取得一個臨時檔路徑，或需要把結果交給其他 API 使用的情境。
# delete=False 表示不要在關閉時立刻刪掉，方便後續再讀或手動刪除。
with tempfile.NamedTemporaryFile("wt", delete=False, suffix=".log",
                                 encoding="utf-8") as f:
    f.write("暫存 log\n")
    log_path = f.name
print("暫存檔位置:", log_path)
# 用完手動刪除，避免殘留在系統暫存區。
Path(log_path).unlink()  # 用完自己刪

# ── 5.21 pickle：把 Python 物件「原樣」存檔 ────────────
# pickle 適合存 Python 物件樹，例如 dict、list、tuple、set、甚至自訂類別。
# 但它不是通用資料交換格式：
# 1) 跨語言支援差
# 2) 檔案內容不可讀
# 3) 長期保存與版本相容性較弱
# 如果是交換資料，通常 JSON 更穩定。
scores = {
    "alice": [90, 85, 92],
    "bob":   [70, 75, 80],
    "carol": [88, 91, 95],
}

# 注意：pickle 存出來的是 bytes，所以一定要用 'wb' / 'rb'。
# 不能用文字模式，因為文字模式會嘗試編碼/解碼，與 pickle 的資料型態不相容。
with open("scores.pkl", "wb") as f:
    pickle.dump(scores, f)

# load() 會把 bytes 還原成 Python 物件，前提是檔案內容可信且完整。
with open("scores.pkl", "rb") as f:
    loaded = pickle.load(f)

print("讀回的物件:", loaded)
# type(loaded) is dict 用來確認還原出來的物件類型與原本一致。
print("型別一致?", type(loaded) is dict)         # True
# == 用來確認內容是否完全相同。
print("內容相等?", loaded == scores)              # True
# 讀回後可以直接對物件做一般 Python 運算，像計算平均。
print("alice 平均:", sum(loaded["alice"]) / 3)   # 89.0

# ⚠️ 安全提醒：pickle.load 可能執行內嵌的還原指令，
# 絕對不要對「來路不明」或不可信的 .pkl 檔做 load。
# 換句話說，pickle 適合自己產生、自己使用的檔案，不適合公開資料交換。

# ── 課堂延伸挑戰 ───────────────────────────────────────
# 以下是延伸練習，用來把 gzip / tempfile / pickle 串在一起思考。
# 1) 把 scores 存成 gzip 壓縮後的 pickle：gzip.open('scores.pkl.gz','wb')
# 2) 用 TemporaryDirectory 跑完整流程（寫→讀→比對），不在專案留任何檔
# 3) 試著 pickle 一個 lambda，觀察錯誤訊息（pickle 不能存 lambda）
