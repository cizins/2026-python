# U02. 正則表達式進階技巧（2.4–2.6）
# 說明：本程式碼示範 Python 中正規表達式的幾個進階應用：
# 1. 預編譯效能比較：多次使用的正則表達式，預先編譯 (re.compile) 可以提升效能。
# 2. re.sub 搭配回呼函數 (callback)：不只可以替換固定字串，還可以把匹配結果丟給一個函數動態產生替換內容。
# 3. 保持大小寫一致的替換：在進行忽略大小寫替換時，能根據原本匹配到的大小寫格式，將替換字串轉換成對應的格式。

import re
import timeit
from calendar import month_abbr

# ── 預編譯效能（2.4）──────────────────────────────────
text = "Today is 11/27/2012. PyCon starts 3/13/2013."

# 預先將正規表達式編譯成 Pattern 物件
# 當同一個正規表達式在程式碼中會被重複執行多次（例如在迴圈中）時，
# 預先編譯可以省下每次呼叫模組層級的 re.findall() 或 re.sub() 時內部重複編譯的開銷。
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")


def using_module():
    # 直接使用 re 模組的 findall 方法，內部會先編譯一次正規表達式，然後再執行匹配，並且會快取結果
    return re.findall(r"(\d+)/(\d+)/(\d+)", text)


def using_compiled():
    # 使用已經預先編譯好的 Pattern 物件直接尋找，省去了編譯與查詢快取的開銷
    return datepat.findall(text)


# 使用 timeit 來測量兩種方式執行 5 萬次所花費的時間
# 在多次重複執行的情況下，預編譯通常會有一定的效能優勢
t1 = timeit.timeit(using_module, number=50_000)
t2 = timeit.timeit(using_compiled, number=50_000)
print(f"直接呼叫 (using_module): {t1:.3f}s  預編譯 (using_compiled): {t2:.3f}s")


# ── sub 回呼函數（2.5）────────────────────────────────
# 定義一個回呼函數 (callback function)
# 這個函數接收一個 re.Match 物件作為參數，並回傳要替換成的字串
def change_date(m: re.Match) -> str:
    # m.group(1) 抓出月份 (例如 '11' 或 '3')，將其轉為數字後，
    # 透過 month_abbr 從數字取得月份的英文縮寫 (例如 11 -> 'Nov')
    mon_name = month_abbr[int(m.group(1))]
    # 重新組合為: '日 月份縮寫 年' 的格式
    return f"{m.group(2)} {mon_name} {m.group(3)}"


# re.sub(替換內容, 目標字串)
# 這裡將 `change_date` 函數當作「替換內容」傳入。
# sub 會自動找到所有符合 datepat (月/日/年) 的地方，把每一次的 Match 物件丟給 change_date，
# 然後用 change_date 回傳的字串替換掉原本的內容。
print(datepat.sub(change_date, text))
# 輸出: 'Today is 27 Nov 2012. PyCon starts 13 Mar 2013.'


# ── 保持大小寫一致的替換（2.6）───────────────────────
# 這是一個高階函數 (Higher-Order Function) 或稱為閉包 (Closure)
# 接收我們要替換的目標詞彙 `word`，然後回傳一個可以用於 `re.sub` 的替換函數。
def matchcase(word: str):
    # 這個 replace 函數才是真正會被傳給 re.sub 執行的回呼函數
    def replace(m: re.Match) -> str:
        # 取出被匹配到的原本文字
        t = m.group()
        
        # 檢查原文字的大小寫狀態，並讓要替換的 word 模仿該狀態：
        if t.isupper():
            return word.upper()       # 如果原文字是全大寫 (例如 PYTHON)，替換字也變全大寫 (SNAKE)
        if t.islower():
            return word.lower()       # 如果原文字是全小寫 (例如 python)，替換字也變全小寫 (snake)
        if t[0].isupper():
            return word.capitalize()  # 如果原文字是首字母大寫 (例如 Python)，替換字也變首字母大寫 (Snake)
        
        # 如果都不是，就直接回傳原本指定的 word
        return word

    return replace


s = "UPPER PYTHON, lower python, Mixed Python"

# 在 re.sub 裡面使用 flags=re.IGNORECASE 進行「忽略大小寫」的匹配。
# 所以 "python" 可以配到 PYTHON、python 和 Python。
# 每次匹配到，就會丟給 matchcase("snake") 所產生的 replace 函數去判斷並決定回傳的大、小寫格式。
print(re.sub("python", matchcase("snake"), s, flags=re.IGNORECASE))
# 輸出: 'UPPER SNAKE, lower snake, Mixed Snake'
