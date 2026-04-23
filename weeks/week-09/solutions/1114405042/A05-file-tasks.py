# A05. 綜合應用：僅寫新檔 + 目錄統計（5.5 / 5.13 / 5.1）
# Bloom: Apply — 把前面學到的 API 組起來解小任務

from pathlib import Path
from datetime import date

# 這份範例把前面學過的檔案操作組合起來：
# 1) 用 'x' 模式建立「只能新建、不能覆蓋」的檔案
# 2) 用 rglob() 遞迴找出某個資料夾底下所有 .py 檔
# 3) 用逐行讀取統計每個檔案的行數與特定模式
# 4) 將檔案處理與路徑處理結合成一個小工具

# ── 任務一：日記小工具（5.5 的 'x' 模式） ──────────────
# 規則：每天只能建一次；同一天重複執行要提示「已存在」。
# date.today() 取得今天日期，isoformat() 轉成 YYYY-MM-DD 的標準字串。
today = date.today().isoformat()          # 例如 2026-04-23
diary = Path(f"diary-{today}.txt")

try:
    # 'x' = exclusive create：只允許「建立新檔」，若檔案已存在就直接報錯。
    # 這種模式很適合日記、報名表、一次性輸出等不想被覆蓋的情境。
    with open(diary, "x", encoding="utf-8") as f:
        # 以 UTF-8 建立文字檔，確保中文內容跨平台可正常讀寫。
        f.write(f"# {today} 日記\n")
        f.write("今天學了檔案 I/O。\n")
    print(f"已建立 {diary}")
except FileExistsError:
    # 如果同一天已經建立過，就保留原內容，不做覆蓋。
    print(f"{diary} 今天已寫過，保留原內容不覆蓋")

# ── 任務二：統計某資料夾裡 .py 檔的行數 ────────────────
# 走訪目錄 → 逐檔逐行讀 → 累計三個數字
def count_py(folder: Path):
    # total：總行數
    # nonblank：非空白行數
    # defs：以 def 開頭的函式定義行數
    total, nonblank, defs = 0, 0, 0

    # rglob("*.py") 會遞迴搜尋 folder 底下所有副檔名為 .py 的檔案。
    # 這裡回傳的是 Path 物件，方便後續直接丟進 open()。
    for p in folder.rglob("*.py"):
        # errors="replace" 表示遇到無法解碼的位元組時，以替代字元接住，
        # 避免整個統計流程因單一壞字元而中斷。
        with open(p, "rt", encoding="utf-8", errors="replace") as f:
            # 檔案逐行讀取，能避免一次把大檔全部載入記憶體。
            for line in f:
                total += 1
                # strip() 先去掉前後空白，方便判斷是不是空白行，
                # 也讓我們能用 startswith("def ") 檢查函式定義。
                s = line.strip()
                if s:
                    nonblank += 1
                if s.startswith("def "):
                    defs += 1
    return total, nonblank, defs

target = Path("..") / ".." / "week-04" / "in-class"
if target.exists():
    # 先確認目錄存在再統計，避免找不到路徑時直接出錯。
    total, nonblank, defs = count_py(target)
    print(f"{target}")
    print(f"  總行數       : {total}")
    print(f"  非空白行     : {nonblank}")
    print(f"  def 起頭行數 : {defs}")
else:
    # 示範環境可能沒有這個資料夾，因此先提示而不是硬跑。
    print(f"示範目錄不存在：{target}")

# ── 課堂延伸挑戰（自行嘗試） ───────────────────────────
# 下面三題不是程式必要部分，而是留給你練習如何把相同技巧再延伸。
# 1) 把日記工具改成「附加」模式 'a'：同一天可多次追寫一行時間戳。
# 2) count_py 再多算一個「註解行（以 # 開頭）」的數字。
# 3) 把統計結果用 print(..., sep='\t', file=f) 寫到 stats.tsv。
