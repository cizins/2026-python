# R02. 路徑操作與目錄列舉（5.11 / 5.12 / 5.13）
# Bloom: Remember — 會用 pathlib 組路徑、檢查存在、列出檔案

import os
from pathlib import Path

# 本檔案重點：
# 1) pathlib.Path 是現代 Python 推薦的路徑操作方式
# 2) 理解 / 運算子、stem / suffix / name / parent 的用途
# 3) exists() / is_file() / is_dir() 用於檔案系統檢查
# 4) glob 與 rglob 用於檔案搜尋（單層 vs 遞迴）
# 5) 為何要用 pathlib 而非老舊的 os.path

# ── 5.11 組路徑：pathlib 是現代寫法 ────────────────────
# Path("weeks") 建立路徑物件，可用 / 運算子拼接，
# 自動適應作業系統（Linux /，Windows \）。
# 舊寫法 os.path.join 容易出錯，不建議新程式使用。
base = Path("weeks") / "week-09"
print(base)              # weeks/week-09（Windows 會自動變成反斜線）
# .name 是「最後一個零件」的名稱。
print(base.name)         # week-09
# .parent 取上一層路徑。
print(base.parent)       # weeks
# .suffix 是副檔名（含點），資料夾無副檔名，回傳空字串。
print(base.suffix)       # ''（無副檔名）

f = Path("hello.txt")
# .stem 是檔名去掉副檔名，.suffix 是副檔名（含點）。
print(f.stem, f.suffix)  # hello .txt

# 相容舊寫法：os.path.join（較舊，但仍可用，不過 Path 更直觀）
print(os.path.join("weeks", "week-09", "README.md"))

# ── 5.12 存在判斷 ──────────────────────────────────────
# 這些檢查方法在「讀檔前先驗證」、「防禦式程式設計」時很重要。
p = Path("hello.txt")
# .exists() 回傳 True/False，檔案或資料夾都會回傳 True。
print(p.exists())    # 是否存在
# .is_file() 只在「是檔案」時回傳 True。
print(p.is_file())   # 是否是檔案
# .is_dir() 只在「是資料夾」時回傳 True。
print(p.is_dir())    # 是否是資料夾

missing = Path("no_such_file.txt")
# 常見模式：先檢查再讀，避免 FileNotFoundError。
if not missing.exists():
    print(f"{missing} 不存在，略過讀取")

# ── 5.13 列出資料夾內容 ────────────────────────────────
# 三種遍歷方式各有用途：listdir（無框架）、glob（單層+模式）、rglob（遞迴+模式）。
here = Path(".")

# 方法 1：os.listdir() 列出當層所有項目（檔案與資料夾）
# 回傳字串清單，不包括隱藏檔（通常）。
for name in os.listdir(here):
    print("listdir:", name)

# 方法 2：Path.glob() 用模式搜尋當層（不遞迴）。
# *.py 代表「任意名稱 + .py 副檔名」，只看當層。
# 回傳 Path 物件，更好處理。
for p in here.glob("*.py"):
    print("glob:", p)

# 方法 3：Path.rglob() 遞迴搜尋所有子資料夾（recursive glob）。
# 威力強大但可能遍歷龐大目錄樹，要注意效能。
for p in Path("...").rglob("*.py"):
    print("rglob:", p)
    break  # 示範用，只印第一個（完整執行會列出很多檔案）
