# U01. 計時裝飾器實作與資料格式速度比較（6.1 / 6.2 / 6.3）
# 從「重複的計時程式碼」出發，引入裝飾器，再做格式實驗

"""
示範：使用裝飾器統一計時邏輯，並比較不同資料格式（CSV/JSON/XML）
重點：
- 將計時（benchmark）邏輯抽成裝飾器，避免在每個函式內重複計時程式碼。
- 示範 functools.wraps 的用途：保留原函式的 metadata（例如 __name__ 和 __doc__），
    使除錯與程式碼說明更友善。
- 比較三種常見序列化格式的解析速度差異（以 Python 內建/常用實作為基準）。

所有註解與說明皆以繁體中文（zh-TW）撰寫，方便教學與程式碼閱讀。
"""

import csv
import json
import time
import io
import xml.etree.ElementTree as ET
import functools

# ═══════════════════════════════════════════════════════════
# Part 1｜問題：每個函式都要手動計時 → 大量重複
# ═══════════════════════════════════════════════════════════

def read_csv_raw(data: str) -> list:
    """將 CSV 字串解析為字典列表。

    說明：使用 csv.DictReader 會把每一列解析成 dict，欄位名稱來自標頭。
    備註：回傳的每個欄位值皆為字串，必要時 caller 必須自行轉型（例如 int）。
    """
    return list(csv.DictReader(io.StringIO(data)))

def read_json_raw(data: str) -> list:
    """將 JSON 字串解析為 Python 結構（通常為 list/dict）。

    說明：json.loads 使用的是 C 實作的解析器（在 CPython 中），速度通常較快。
    """
    return json.loads(data)

def read_xml_raw(data: str) -> list:
    """將簡單 XML 字串解析為屬性字典的列表。

    說明：此處假設每個記錄為 <row .../>，且我們只取 attribute 而不處理內部文字節點。
    XML 解析通常較慢，且需要額外的字串轉型（例如屬性都是字串）。
    """
    root = ET.fromstring(data)
    return [r.attrib for r in root.findall("row")]

# 沒有裝飾器：每次都要複製貼上計時程式碼 ↓
# start = time.perf_counter()
# result = read_csv_raw(data)
# print(f"read_csv_raw 耗時 {time.perf_counter() - start:.6f}s")
#
# start = time.perf_counter()
# result = read_json_raw(data)
# print(f"read_json_raw 耗時 {time.perf_counter() - start:.6f}s")
# ... 每加一個函式就多寫三行，且容易忘記移除

# ═══════════════════════════════════════════════════════════
# Part 2｜解法：裝飾器把計時邏輯包起來，一次定義，到處復用
# ═══════════════════════════════════════════════════════════

def timeit(func):
    """裝飾器（簡易版）：在呼叫前後計時並印出耗時。

    使用說明：
    - 將此裝飾器套在任何函式上，呼叫時會在標準輸出印出該次呼叫耗時。
    - 該實作未保留原函式的 metadata，呼叫 help() 或 inspect 時會看到 wrapper 的資訊。
    """
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")
        return result
    return wrapper

# 問題：wrapper 蓋掉了原函式的 __name__ / __doc__
def demo():
    """這是 demo 的說明文字"""
    pass

wrapped = timeit(demo)
print("未加 wraps 前：", wrapped.__name__)   # wrapper（錯誤！）

# ── Part 3｜functools.wraps：保留原函式的 metadata ──────────

def timeit(func):
    @functools.wraps(func)          # 使用 functools.wraps 保留原函式的 __name__、__doc__ 等屬性
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")
        return result
    return wrapper

wrapped = timeit(demo)
print("加 wraps 後：  ", wrapped.__name__)   # demo（正確）
print()

# ═══════════════════════════════════════════════════════════
# Part 4｜實驗：相同資料，CSV vs JSON vs XML 速度比較
# ═══════════════════════════════════════════════════════════

# ── 產生測試資料（1000 筆學生記錄）────────────────────────
N = 1000

# CSV 格式
csv_buf = io.StringIO()
writer = csv.DictWriter(csv_buf, fieldnames=["id", "name", "score"])
writer.writeheader()
for i in range(N):
    writer.writerow({"id": i, "name": f"Student{i:04d}", "score": 60 + i % 40})
CSV_DATA = csv_buf.getvalue()

# JSON 格式
JSON_DATA = json.dumps([
    {"id": i, "name": f"Student{i:04d}", "score": 60 + i % 40}
    for i in range(N)
])

# XML 格式
xml_rows = "".join(
    f'<row id="{i}" name="Student{i:04d}" score="{60 + i % 40}"/>'
    for i in range(N)
)
XML_DATA = f"<data>{xml_rows}</data>"

# ── 帶回傳耗時的計時包裝 ─────────────────────────────────

def timeit_silent(func):
    """計時裝飾器（無輸出版本）：回傳 (原始結果, 耗時)

    說明：
    - 有些情境我們不想直接印出耗時，而是要以資料方式收集、計算平均或做進一步分析，
      這時使用這個 decorator 會比較方便。
    - 同樣使用 functools.wraps 保留原始函式 metadata。
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        return result, time.perf_counter() - start
    return wrapper

_csv  = timeit_silent(read_csv_raw)
_json = timeit_silent(read_json_raw)
_xml  = timeit_silent(read_xml_raw)

# ── 執行比較（重複 5 次取平均，排除冷啟動影響）────────────

RUNS = 5
times = {"CSV": 0.0, "JSON": 0.0, "XML": 0.0}

for _ in range(RUNS):
    _, t = _csv(CSV_DATA);   times["CSV"]  += t
    _, t = _json(JSON_DATA); times["JSON"] += t
    _, t = _xml(XML_DATA);   times["XML"]  += t

print(f"=== 讀取 {N} 筆資料，重複 {RUNS} 次平均 ===\n")
print(f"{'格式':<6} {'平均耗時':>12}  {'相對 JSON':>10}")
base = times["JSON"] / RUNS
for fmt, total in times.items():
    avg = total / RUNS
    print(f"  {fmt:<6} {avg:.6f}s   {avg/base:>8.2f}x")

# ═══════════════════════════════════════════════════════════
# 觀察重點（詳細說明）
# ═══════════════════════════════════════════════════════════
# 1. JSON 通常最快：
#    - 在 CPython 中，json 模組的部分解析器用 C 實作（或有高度優化），因此解析速度通常較快。
#    - 備註：如果使用第三方快速 JSON 庫（如 orjson），速度會更好，但此範例以標準庫為主。
# 2. XML 通常最慢：
#    - XML 解析需要處理標記、層級與屬性字串，且常需要更多字串操作與結構建立，開銷較大。
#    - 若處理複雜 XML，建議使用分流/串流解析（例如 iterparse）以減少記憶體與解析峰值。
# 3. CSV 介於中間：
#    - CSV 格式簡單，但 csv.DictReader 會把欄位都視為字串，若需數值運算需額外轉型，轉型成本可能影響整體效能。
#
# 裝飾器帶來的好處（為何要用 decorator）：
# - 封裝：將計時邏輯從業務函式中移出，讓函式專注於處理資料。
# - 可重用：一次實作，可套用於多個函式，不會重複貼上相同程式碼。
# - 可切換：需要開啟/關閉計時時，只需改變裝飾器或移除 @timeit，函式本身不變。
# - 可保留 metadata：搭配 functools.wraps 後，除錯或使用 help() 時可以看到原始函式名稱與 docstring，
#   有助於測試與日後維護。
