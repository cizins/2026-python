# R08. 日期範圍與字串轉換（3.14–3.15）
#
# 本範例涵蓋兩個常見需求：
# 1) 取得某個月份的日期範圍，並做日期迭代
# 2) 日期字串與 datetime 之間的雙向轉換
#
# 關鍵概念：
# - 日期區間常用「半開區間」[start, stop)，可避免邊界重複
# - strptime/strftime 是格式化標準工具，手動解析在固定格式時可更快

from datetime import datetime, date, timedelta
from calendar import monthrange


# ── 3.14 當月日期範圍 ─────────────────────────────────
def get_month_range(start: date | None = None) -> tuple[date, date]:
    # 未傳入日期時，使用「今天所在月份的第一天」
    if start is None:
        start = date.today().replace(day=1)

    # monthrange(year, month) -> (該月第一天星期幾, 該月總天數)
    # 這裡只需要總天數 days
    _, days = monthrange(start.year, start.month)

    # 回傳 (月初, 下個月月初)
    # 注意這是半開區間設計：[start, end)
    return start, start + timedelta(days=days)


first, last = get_month_range(date(2012, 8, 1))
# 顯示時把 end 減一天，就能得到該月最後一天
print(first, "~", last - timedelta(days=1))  # 2012-08-01 ~ 2012-08-31


# 通用日期迭代生成器
# 以固定步長 step，從 start 走到 stop（不含 stop）
def date_range(start: datetime, stop: datetime, step: timedelta):
    # 半開區間迴圈：start < stop
    while start < stop:
        yield start
        start += step


# 範例：每 6 小時列出一天內的時間點
for d in date_range(datetime(2012, 9, 1), datetime(2012, 9, 2), timedelta(hours=6)):
    print(d)
# 2012-09-01 00:00:00 / 06:00 / 12:00 / 18:00

# ── 3.15 字串轉換為日期 ───────────────────────────────
text = "2012-09-20"

# strptime: 依格式把字串解析成 datetime
# %Y: 四位數年份, %m: 月(01-12), %d: 日(01-31)
dt = datetime.strptime(text, "%Y-%m-%d")
print(dt)  # 2012-09-20 00:00:00

# strftime: 把 datetime 轉成指定格式字串
# %A: 星期全名, %B: 月份全名
print(datetime.strftime(dt, "%A %B %d, %Y"))  # 'Thursday September 20, 2012'


# 手動解析（固定格式時通常比 strptime 快）
# 適合格式非常固定、且在意效能的情境。
# 代價是可讀性與彈性較差，格式一變就要改程式。
def parse_ymd(s: str) -> datetime:
    y, m, d = s.split("-")
    return datetime(int(y), int(m), int(d))


print(parse_ymd("2012-09-20"))  # 2012-09-20 00:00:00
