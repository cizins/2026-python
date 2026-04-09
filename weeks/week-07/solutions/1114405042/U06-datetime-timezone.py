# U06. 時區操作最佳實踐：UTC 優先（3.16）
# 說明：本程式碼示範處理時間時，尤其涉及時區轉換與夏時制 (Daylight Saving Time, DST) 時，最重要的原則：
# 1. 為什麼要用 UTC？：因為本地時間可能會因為夏令時或時區改變而出現「跳躍」甚至「不存在的時間」。
# 2. 內部時間計算（加減時分秒）應該一律在轉換成 UTC (協調世界時) 後才進行，才不會出錯。
# 3. 最佳實踐模式：使用者輸入時間 -> 轉換並儲存為 UTC -> 進行所有的時間計算 -> 最後要顯示給使用者看時，才轉回他們的本地時間。

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# 準備兩個時區物件：UTC 協調世界時 與 America/Chicago 美國中部時間
utc = ZoneInfo("UTC")
central = ZoneInfo("America/Chicago")

# 陷阱：直接在本地時間（aware datetime）上做加減，遇到夏令時邊界就會出錯！
# 例如：美國在 2013-03-10 凌晨 2:00 時，會將時鐘往前撥一小時，變成 3:00（這是夏令時的開始）。
# 因此，這天凌晨的 2:00 到 2:59 在這個時區是「不存在」的時間。

# 假設現在是凌晨 1:45
local_dt = datetime(2013, 3, 10, 1, 45, tzinfo=central)

# 錯誤示範：直接加 30 分鐘
# 1:45 + 30 分鐘 = 2:15。但是 2:15 在這一天根本不存在！
wrong = local_dt + timedelta(minutes=30)
print(f"錯誤結果：{wrong}")  # 輸出 2:15（但這個時間不符合現實！）


# 正確做法：無論如何，只要牽涉到時間計算，先轉成沒有夏令時干擾的 UTC！
# .astimezone(utc) 會把時間轉成正確的 UTC 對應時間
utc_dt = local_dt.astimezone(utc)

# 在 UTC 的環境下加 30 分鐘，因為 UTC 永遠是線性流逝的，不會有跳躍問題
correct = utc_dt + timedelta(minutes=30)

# 計算完成後，再轉回芝加哥本地時間顯示。
# 這樣系統就會自動處理夏令時的跳躍，正確得出 3:15
print(f"正確結果：{correct.astimezone(central)}")  # 輸出 3:15（成功跳過了不存在的 2:xx）


# ── 時區處理最佳實踐（Best Practice）─────────────────
# 記住這個口訣：輸入 → 轉換為 UTC 儲存/計算 → 輸出時才轉回本地

# 步驟 1：取得使用者輸入（通常是當地時間字串）
user_input = "2012-12-21 09:30:00"

# 步驟 2：解析字串。此時得到的是一個沒有時區資訊的 "naive" datetime
naive = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")

# 步驟 3：為這個 naive 時間掛上來源時區 (replace)，然後立刻轉換成 UTC (astimezone)
# 這樣我們就得到了一個安全的，可以用於各種比較、加減與存入資料庫的 "aware" UTC 時間
aware = naive.replace(tzinfo=central).astimezone(utc)
print(f"存入資料庫或進行計算的 UTC 時間：{aware}")

# 步驟 4：當需要顯示給另一個時區（例如台北）的使用者看時，再從 UTC 轉過去
print(f"顯示在台北使用者的畫面：{aware.astimezone(ZoneInfo('Asia/Taipei'))}")