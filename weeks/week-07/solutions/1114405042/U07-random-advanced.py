# U07. 隨機種子與安全亂數（3.11）
# 說明：本程式碼示範 Python 中隨機數產生的兩個重要觀念與工具：
# 1. `random` 模組：產生的是「偽隨機數」(Pseudo-random numbers)。
#    給定相同的種子 (seed)，就會產生完全一樣的隨機數序列。適合用在遊戲、模擬測試等需要「可重現性」的場合。
#    ⚠️ 絕對不能用在密碼學、資安相關的功能上！
# 2. `secrets` 模組：產生的是「密碼學安全」的真隨機數 (Cryptographically strong random numbers)。
#    它是不可預測的，且不能設定種子。適合用來產生密碼、Token、Session Key 等安全相關資料。

import random
import secrets

# ── random 模組：相同種子 → 相同序列（可重現） ───────────
# 設定全局亂數種子為 42
random.seed(42)
# 產生 5 個 1 到 100 之間的隨機整數
seq1 = [random.randint(1, 100) for _ in range(5)]

# 再次設定相同的全局亂數種子 42
random.seed(42)
# 再次產生 5 個 1 到 100 之間的隨機整數
seq2 = [random.randint(1, 100) for _ in range(5)]

# 陷阱與特性：因為種子相同，所以兩次產生的隨機數序列會「完全一模一樣」
print(seq1 == seq2)  # 輸出: True


# ── 不同 Random 實例各自獨立 ─────────────────────────────
# 如果不想干擾全局的 random 狀態，可以建立獨立的 Random 物件 (實例)
# 每個實例都有自己獨立的內部狀態與種子，彼此產生的亂數流不會互相影響
rng1 = random.Random(1)
rng2 = random.Random(2)

print(rng1.random(), rng2.random())  # 輸出兩個不同的隨機小數


# ── secrets 模組：密碼學安全亂數 ─────────────────────────
# 這是 Python 3.6 加入的模組，專門用來處理資安敏感的隨機需求。
# 底層會去呼叫作業系統提供的安全隨機數生成器 (例如 Linux 的 /dev/urandom 或 Windows 的 CryptGenRandom)。
# 它「不能」設定種子，因此每次執行結果都絕對無法預測。

# 產生一個 0 到 99 之間的安全隨機整數 (不包含 100)
print(secrets.randbelow(100))  

# 產生一個長度為 16 bytes 的安全隨機十六進位字串 (hex string)
# 這種格式非常適合用來當作 API Token、密碼重置連結的 token 等
print(secrets.token_hex(16))  

# 產生 16 bytes 的安全隨機位元組 (bytes)
# 通常用在需要二進位資料的加密演算法 (如 AES 的 IV 或 Key)
print(secrets.token_bytes(16))  

# ⚠️ 再次強調：
# random 模組不適合用於密碼、token、session key 等安全場景！
# 這些場景請務必改用 secrets 模組。
# random 只適合遊戲、數值模擬、單元測試等非安全用途。