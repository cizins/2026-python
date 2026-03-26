# R09. 時區操作（3.16）
#
# 本範例示範 Python 3.9+ 的 zoneinfo 標準時區做法：
# 1) 建立帶時區的 datetime（aware datetime）
# 2) 在不同時區之間安全轉換
# 3) 以 UTC 作為內部儲存與計算基準
#
# 與舊做法相比，zoneinfo 已是標準庫，通常不再需要 pytz。

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo, available_timezones

# 常用時區物件（IANA 時區名稱）
utc = ZoneInfo("UTC")
central = ZoneInfo("America/Chicago")
taipei = ZoneInfo("Asia/Taipei")

# 建立帶時區的 datetime（tzinfo 不為 None）
# 這種帶時區資訊的時間稱為 aware datetime，能安全做跨時區轉換
d = datetime(2012, 12, 21, 9, 30, 0, tzinfo=central)
print(d)  # 2012-12-21 09:30:00-06:00

# astimezone() 會保留「同一個絕對時間點」，只改變顯示時區
print(d.astimezone(ZoneInfo("Asia/Kolkata")))  # 2012-12-21 21:00:00+05:30
print(d.astimezone(taipei))  # 2012-12-21 23:30:00+08:00

# 取得目前 UTC 時間（建議伺服器內部使用 UTC）
now_utc = datetime.now(tz=utc)
print(now_utc)

# 最佳實踐：內部存 UTC，輸出給使用者時再轉在地時區
# 這可降低夏令時間（DST）切換造成的歧義與錯誤
utc_dt = datetime(2013, 3, 10, 7, 45, 0, tzinfo=utc)
print(utc_dt.astimezone(central))  # 2013-03-10 01:45:00-06:00

# 查詢可用時區（此處示範篩選含 Taipei 的名稱）
# available_timezones() 會回傳大量 IANA 時區字串

tw_zones = [z for z in available_timezones() if "Taipei" in z]
print(tw_zones)  # ['Asia/Taipei']
