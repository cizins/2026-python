# U05. 日期時間的陷阱（3.12–3.15）
# 說明：本程式碼示範 Python 處理日期與時間時常見的兩個陷阱：
# 1. timedelta 不支援「月份」(months) 作為參數，因為每個月的天數不固定。
# 2. datetime.strptime() 在解析大量日期字串時效能非常差。對於固定格式的日期字串，手動解析反而快得多。

import timeit
import calendar
from datetime import datetime, timedelta

# ── timedelta 不支援月份（3.12）──────────────────────
dt = datetime(2012, 9, 23)

try:
    # 陷阱：我們直覺上可能會想用 timedelta(months=1) 來加一個月
    # 但是 timedelta 只支援 weeks, days, hours, minutes, seconds, milliseconds, microseconds
    # 因為「一個月」到底有幾天是未知的（28、29、30 或 31 天），所以官方不支援這種寫法。
    dt + timedelta(months=1)  # type: ignore[call-arg]
except TypeError as e:
    # 這裡會拋出 TypeError: 'months' is an invalid keyword argument for __new__()
    print(f"TypeError: {e}")


# 解法：如果真的需要進行月份的加減，可以自訂函數。
# 需要使用 calendar 模組取得目標月份的總天數，並將日期 "clamp" (限制) 到該月的最後一天。
# 例如：1月31日加一個月，如果目標是平年2月，就必須限制在2月28日。
def add_one_month(dt: datetime) -> datetime:
    # 計算目標的年與月
    year = dt.year
    month = dt.month + 1
    
    # 如果月份超過 12，代表跨年了，年份加一，月份變回 1 月
    if month == 13:
        year += 1
        month = 1

    # 利用 calendar.monthrange(year, month) 取得該月的第一天是星期幾(丟棄不用) 以及 該月的總天數
    _, days_in_target_month = calendar.monthrange(year, month)
    
    # 取原本的日期 (dt.day) 與目標月份總天數的最小值。
    # 這樣就可以確保 1/31 加一個月會變成 2/28 (或閏年 2/29)
    day = min(dt.day, days_in_target_month)

    # 用 .replace() 產生一個新的 datetime 物件回傳
    return dt.replace(year=year, month=month, day=day)


print(add_one_month(datetime(2012, 1, 31)))  # 輸出: 2012-02-29 (2012年是閏年)
print(add_one_month(datetime(2012, 9, 23)))  # 輸出: 2012-10-23


# ── strptime 效能問題（3.15）─────────────────────────
# 準備一份用來測試的大量日期字串清單 (2012年的每一天，這裡簡單取 1~28 號確保每個月份都有效)
dates = [f"2012-{m:02d}-{d:02d}" for m in range(1, 13) for d in range(1, 29)]


# 陷阱：strptime 雖然方便，但它是用純 Python 實作的，而且需要處理各種複雜的格式字串，
# 這導致它在面對大量資料時，解析速度非常慢。
def use_strptime(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%d")


# 解法：如果日期字串的格式是固定且已知的（例如 YYYY-MM-DD），
# 直接用字串的 split() 拆分，然後轉成 int 餵給 datetime() 建構子，速度會快非常多！
def use_manual(s: str) -> datetime:
    y, m, d = s.split("-")
    return datetime(int(y), int(m), int(d))


# 確認兩種方法解析出來的結果是一模一樣的
assert use_strptime("2012-09-20") == use_manual("2012-09-20")

# 使用 timeit 測量兩種方法解析 100 次 dates 列表的時間差異
t1 = timeit.timeit(lambda: [use_strptime(d) for d in dates], number=100)
t2 = timeit.timeit(lambda: [use_manual(d) for d in dates], number=100)
print(f"strptime (內建): {t1:.3f}s  手動解析: {t2:.3f}s（快 {t1 / t2:.1f} 倍）")