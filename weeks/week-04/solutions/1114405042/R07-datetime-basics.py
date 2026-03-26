# R07. 日期時間基本運算（3.12–3.13）
#
# 這份範例示範兩個很實用的日期時間技巧：
# 1) 使用 timedelta 做日期與時間的加減
# 2) 使用 weekday() 計算「上一個指定星期幾」
#
# 常見應用：報表區間、排程回推、週期性任務日期計算。

from datetime import datetime, timedelta

# ── 3.12 timedelta 基本運算 ───────────────────────────
# timedelta 可同時表示天、秒、微秒等時間差
# 這裡建立 2 天 6 小時
a = timedelta(days=2, hours=6)
# 4.5 小時（可接受浮點）
b = timedelta(hours=4.5)
c = a + b

# days 屬性是「整天數」部分
print(c.days)  # 2

# total_seconds() 取得完整秒數（包含天數），再換算成小時
print(c.total_seconds() / 3600)  # 58.5

# datetime + timedelta 可直接得到新日期時間
dt = datetime(2012, 9, 23)
print(dt + timedelta(days=10))  # 2012-10-03 00:00:00

# 兩個 datetime 相減會得到 timedelta
d1, d2 = datetime(2012, 9, 23), datetime(2012, 12, 21)
print((d2 - d1).days)  # 89

# 閏年會由 datetime 自動處理，不需手動判斷
# 2012 是閏年，2/28 到 3/1 會跨兩天（含 2/29）
print((datetime(2012, 3, 1) - datetime(2012, 2, 28)).days)  # 2（閏年）
# 2013 非閏年，2/28 到 3/1 只跨一天
print((datetime(2013, 3, 1) - datetime(2013, 2, 28)).days)  # 1（平年）

# ── 3.13 計算指定星期日期 ─────────────────────────────
WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def get_previous_byday(dayname: str, start: datetime | None = None) -> datetime:
    # 未提供起始時間時，預設使用現在時間
    if start is None:
        start = datetime.today()

    # weekday(): Monday=0, ..., Sunday=6
    day_num = start.weekday()

    # 目標星期的索引值（同樣以 Monday=0）
    target = WEEKDAYS.index(dayname)

    # 計算要往前退幾天：
    # (7 + 今日 - 目標) % 7 可以得到「差值（0~6）」
    # 若結果為 0，代表今天就是目標星期；題目要「previous」，
    # 因此用 or 7 讓它回到前一週同星期。
    days_ago = (7 + day_num - target) % 7 or 7

    # 回傳往前 days_ago 天的日期
    return start - timedelta(days=days_ago)


base = datetime(2012, 8, 28)  # 週二
# 從週二回推最近的週一、週五
print(get_previous_byday("Monday", base))  # 2012-08-27
print(get_previous_byday("Friday", base))  # 2012-08-24
