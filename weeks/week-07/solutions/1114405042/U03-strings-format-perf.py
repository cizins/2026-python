# U03. 字串格式化效能與陷阱（2.14–2.20）
# 說明：本程式碼示範 Python 中字串處理的效能差異與幾個進階的格式化技巧：
# 1. 字串串接效能比較：大量字串串接時，使用 "".join() 遠比使用 + 號快。
# 2. format_map 處理缺失鍵：在使用字串的 format 功能時，如果字典中缺少某些鍵值，可以透過自訂字典來避免報錯。
# 3. bytes (位元組) 與 string (字串) 的索引差異：說明 bytes 物件在索引取值時的行為差異。

import timeit

# ── join 效能優於 + （2.14）──────────────────────────
# 先準備一個包含 1000 個字串的陣列 (list)，用來做串接測試
parts = [f"item{i}" for i in range(1000)]


def bad_concat():
    s = ""
    for p in parts:
        # 陷阱：每次使用 += 串接字串時，Python 都必須在記憶體中建立一個全新的字串物件，
        # 將舊的內容和新的內容拷貝進去。隨著字串越來越長，拷貝的成本也越來越高。
        # 因此這樣做在大量資料時效能極差，時間複雜度為 O(n²)。
        s += p  
    return s


def good_join():
    # 正確寫法：使用 .join() 方法。
    # Python 內部會先計算出串接後的總長度，然後只向作業系統申請一次足夠的記憶體空間，
    # 接著一次把所有字串填進去。這種做法效能極佳，時間複雜度為 O(n)。
    return "".join(parts)  


# 使用 timeit 來測量兩種方式執行 500 次所花費的時間
# 測試結果會發現 good_join() 遠比 bad_concat() 快得多
t1 = timeit.timeit(bad_concat, number=500)
t2 = timeit.timeit(good_join, number=500)
print(f"+串接 (bad_concat): {t1:.3f}s  join (good_join): {t2:.3f}s")


# ── format_map 處理缺失鍵（2.15）─────────────────────
# 預設情況下，如果使用 s.format(**dict) 或 s.format_map(dict)，
# 只要字典裡少了一個鍵 (key)，就會拋出 KeyError。
# 這裡我們自訂一個繼承自內建 dict 的類別 `SafeSub`。
class SafeSub(dict):
    # 當向字典請求一個不存在的鍵時，會自動觸發 __missing__ 方法
    def __missing__(self, key: str) -> str:
        # 在這裡我們不拋出錯誤，而是原封不動地把該佔位符回傳（例如 "{n}"）
        # 這樣格式化時，缺失的變數就會維持原本的 {key} 樣子，不會讓程式當掉
        return "{" + key + "}"  


name = "Guido"
s = "{name} has {n} messages."

# vars() 會回傳目前區域範圍內的變數所組成的字典，此時字典裡有 'name'，但沒有 'n'
# 透過 format_map() 並傳入我們自訂的 SafeSub 字典
# 因為 n 不存在，會觸發 SafeSub.__missing__，回傳 "{n}"
print(s.format_map(SafeSub(vars())))  
# 輸出: 'Guido has {n} messages.'（n 不存在也不會報錯）


# ── bytes 索引回傳整數（2.20）────────────────────────
# 字串 (string) 物件
a = "Hello"
# 位元組 (bytes) 物件，注意字串前面的 b
b = b"Hello"

# 對普通字串做索引取值，會拿到對應位置的「字元」
print(a[0])  # 輸出: 'H'（字元字串）

# 陷阱：對 bytes 物件做索引取值時，回傳的「不是字元字節」，而是對應的 ASCII/Unicode 數值！
# 'H' 的 ASCII 碼是 72
print(b[0])  # 輸出: 72（整數 = ord('H')）

# 陷阱：bytes 物件不能直接呼叫 .format() 方法進行格式化
# 正確做法是先對普通字串做格式化，完成後再 encode 轉換成 bytes
# '{:10s}' 代表佔 10 個字元的字串，'{:5d}' 代表佔 5 個字元的整數
print("{:10s} {:5d}".format("ACME", 100).encode("ascii"))
# 輸出: b'ACME       100'
