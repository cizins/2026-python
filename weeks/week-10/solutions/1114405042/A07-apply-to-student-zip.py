# A07. 綜合應用：把 I/O 技巧實際套用到真實學生資料
# Bloom：Apply — 目標是把 R01~A06 學過的 API 串起來做完整資料處理
#
# 資料來源：assets/npu-stu-109-114-anon.zip（6 屆新生資料庫，學號已匿名化）
# 這支範例會同時示範以下重點：
#   5.11 pathlib：用 Path 乾淨地組合路徑，避免手寫字串拼接出錯
#   5.12 exists：先確認檔案是否存在，讓錯誤訊息更早、更清楚地出現
#   5.7  zipfile：直接讀 zip 壓縮檔內容，不必先解壓到磁碟
#   5.1  encoding='utf-8-sig'：正確處理 Excel 常見的 BOM，避免第一欄欄名怪異
#   5.6  io.StringIO：把 bytes 轉成 csv 模組可直接讀取的文字檔物件
#   5.19 TemporaryDirectory：把中間產物放進暫存沙箱，離開後自動清理
#   5.5  open(..., 'x')：用只允許「新建」的模式寫報告，避免不小心覆蓋舊檔
#   5.21 pickle：把統計結果序列化，方便之後直接載入重用
#   5.2  print(file=)：直接把 Markdown 內容輸出到檔案，簡潔又直觀

import csv
import io
import pickle
import tempfile
import zipfile
from collections import Counter
from pathlib import Path

# ── 5.11 / 5.12：定位資料檔並確認路徑有效 ─────────────
HERE = Path(__file__).resolve().parent
ZIP_PATH = HERE.parent.parent.parent / "assets" / "npu-stu-109-114-anon.zip"
assert ZIP_PATH.exists(), f"找不到資料：{ZIP_PATH}"
print("資料來源:", ZIP_PATH.name)


# ── 5.7 + 5.6 + 5.1：直接從 zip 讀取 CSV，不先解壓到磁碟 ─────
def iter_year_csv(zip_path: Path):
    """依序產生每一年的資料，回傳 (年度, 欄名列, 資料列清單)。

    這個函式把 zip 檔內每個 CSV 逐一讀出來，並在記憶體中完成文字解碼、
    CSV 解析與資料切片。呼叫端只需要專心處理年度統計，不必管壓縮檔細節。
    """
    with zipfile.ZipFile(zip_path) as z:
        for info in z.infolist():
            # 這裡假設檔名已是正常的 UTF-8；若來源 zip 編碼異常，檔名會先亂掉
            name = info.filename
            if not name.endswith(".csv"):
                continue
            year = name[:3]  # 取檔名前三碼，對應 109~114 學年

            raw = z.read(info)                       # 先從壓縮檔讀出原始 bytes
            text = raw.decode("utf-8-sig")          # 用 utf-8-sig 去掉 BOM，避免欄名出問題
            reader = csv.reader(io.StringIO(text))   # 交給 StringIO 轉成 csv 可讀的文字檔介面
            rows = list(reader)
            yield year, rows[0], rows[1:]


# ── 跨屆統計：整理每一屆的系所分布與入學方式分布 ─────────────
summary = {}        # {年度: {'total': n, 'by_dept': Counter, 'by_entry': Counter}}
all_depts = Counter()

for year, header, rows in iter_year_csv(ZIP_PATH):
    dept_idx  = header.index("系所名稱")
    entry_idx = header.index("入學方式")

    by_dept  = Counter(r[dept_idx]  for r in rows if len(r) > dept_idx)
    by_entry = Counter(r[entry_idx] for r in rows if len(r) > entry_idx)

    summary[year] = {
        "total":    len(rows),
        "by_dept":  by_dept,
        "by_entry": by_entry,
    }
    all_depts.update(by_dept)

# ── 終端輸出：快速查看整體概況 ────────────────────────
print("\n=== 6 屆新生人數 ===")
for year in sorted(summary):
    print(f"  {year} 學年：{summary[year]['total']:>4} 人")

print("\n=== 全體最熱門 5 個系所（累計 6 屆） ===")
for dept, n in all_depts.most_common(5):
    print(f"  {n:>4} 人  {dept}")

print("\n=== 114 學年入學方式分布 ===")
for kind, n in summary["114"]["by_entry"].most_common():
    print(f"  {n:>4} 人  {kind}")


# ── 5.19 + 5.5 + 5.2：在沙箱中產生報告，並用 pickle 存統計快照 ──
with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)

    # 先把整份 summary 序列化存起來，方便之後直接載入，不必重新掃描 zip
    snap = tmp / "summary.pkl"
    with open(snap, "wb") as f:
        pickle.dump(summary, f)
    print(f"\n快照寫入 {snap.name}：{snap.stat().st_size} bytes")

    # 用 'x' 模式建立 Markdown 報告：如果檔案已存在就會報錯，避免覆蓋舊報告
    report = tmp / "report.md"
    with open(report, "x", encoding="utf-8") as f:
        print("# 6 屆新生概況報告\n", file=f)
        print("| 學年 | 人數 | 第一大系所 |", file=f)
        print("|------|------|------------|", file=f)
        for year in sorted(summary):
            top_dept, top_n = summary[year]["by_dept"].most_common(1)[0]
            print(f"| {year} | {summary[year]['total']} | "
                  f"{top_dept} ({top_n}) |", file=f)

    # 讀回剛剛寫好的 Markdown，確認內容完整且可直接預覽
    print("\n=== Markdown 報告預覽 ===")
    print(report.read_text(encoding="utf-8"))

    # 驗證 pickle 可以正常還原，確認快照內容與原始 summary 一致
    with open(snap, "rb") as f:
        loaded = pickle.load(f)
    print("pickle 讀回 key:", sorted(loaded.keys()))

# 離開 with 區塊後，TemporaryDirectory 會自動刪除暫存資料夾，不會把中間檔留在專案裡
print("\n(沙箱已自動清理)")


# ── 課堂延伸挑戰：你可以再往下做的幾個方向 ───────────────
# 1) 把報告改寫到 HERE / 'report.md'：實際輸出到專案資料夾中；注意 'w' 會覆蓋、'x' 會要求檔案不存在。
# 2) 增加「女性比例」欄位：先找出資料中的性別欄，再用 Counter 或比例計算方式統計。
# 3) 把 summary 壓縮存成 summary.pkl.gz：可搭配 gzip.open('wb') 與 pickle.dump，減少檔案大小。
# 4) 找出「逐年下降最明顯」的系所：需要把每個系所按年份整理成序列，再比較變化趨勢。
