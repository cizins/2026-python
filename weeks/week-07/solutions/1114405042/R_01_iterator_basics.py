# Remember（記憶）- 迭代器基礎概念
# 說明：本程式碼示範了 Python 中非常核心的「迭代器 (Iterator)」與「可迭代物件 (Iterable)」觀念。
# 涵蓋了 __iter__() 與 __next__() 的實作、常見的可迭代物件、如何自訂可迭代物件，以及手動觸發與處理 StopIteration。

# 1. 迭代器協議的核心方法
items = [1, 2, 3]

# 呼叫內建的 iter() 函數，實際上是去呼叫物件本身的 __iter__() 魔術方法
# 這個方法會建立並回傳一個對應的「迭代器 (Iterator)」物件
it = iter(items)
print(f"迭代器: {it}")

# 呼叫內建的 next() 函數，實際上是去呼叫迭代器的 __next__() 魔術方法
# 每次呼叫，迭代器就會吐出序列中的下一個元素
print(f"第一個: {next(it)}")  # 輸出 1
print(f"第二個: {next(it)}")  # 輸出 2
print(f"第三個: {next(it)}")  # 輸出 3

# 當迭代器裡面已經沒有更多元素可以吐出來時，它會「主動拋出 StopIteration 例外」
# 這就是 Python 內部 for 迴圈知道什麼時候該停下來的依據
try:
    next(it)
except StopIteration:
    print("迭代結束!")

# 2. 常見可迭代物件
# 只要能被 iter() 成功轉換出迭代器的，就是「可迭代物件 (Iterable)」
print("\n--- 常見可迭代物件 ---")

# 列表 (List) 是一般最常用的可迭代物件
print(f"列表 iter: {iter([1, 2, 3])}")

# 字串 (String) 也是可迭代物件，迭代出來的是一個個字元
print(f"字串 iter: {iter('abc')}")

# 字典 (Dictionary) 也是可迭代物件，預設迭代出來的是字典的 keys (鍵)
print(f"字典 iter: {iter({'a': 1, 'b': 2})}")

# 檔案物件 (File object) 同樣是可迭代物件，每次迭代會讀取出一行文字 (包含換行符號)
import io
f = io.StringIO("line1\nline2\nline3")
print(f"檔案 iter: {iter(f)}")


# 3. 自訂可迭代物件與自訂迭代器
# 要自訂可迭代物件，需要實作 __iter__() 方法，並在裡面回傳一個迭代器
class CountDown:
    def __init__(self, start):
        self.start = start

    # 實作 __iter__：代表這個類別的實例是「可被迭代的」
    def __iter__(self):
        # 這裡回傳一個專門用來處理倒數計時狀態的「迭代器」
        return CountDownIterator(self.start)

# 要自訂迭代器，需要實作 __next__() 方法
class CountDownIterator:
    def __init__(self, start):
        # 迭代器內部會保存當前的進度或狀態
        self.current = start

    # 實作 __next__：定義每次呼叫 next() 時要吐出什麼值
    def __next__(self):
        # 如果已經倒數到 0 或更小，就拋出 StopIteration 結束迭代
        if self.current <= 0:
            raise StopIteration
        
        # 否則，將狀態減 1，並回傳當下的值
        self.current -= 1
        return self.current + 1


print("\n--- 自訂迭代器 ---")
# 因為 CountDown 實作了 __iter__，所以可以直接放在 for 迴圈中
for i in CountDown(3):
    print(i, end=" ")  # 輸出 3 2 1 


# 4. 迭代器 vs 可迭代物件 的觀念釐清
print("\n\n--- 迭代器 vs 可迭代物件 ---")

# 列表是「可迭代物件 (Iterable)」，但它本身並「不是迭代器 (Iterator)」
# 因為 list 有 __iter__() 方法，但沒有 __next__() 方法（不能對 list 直接 call next()）
my_list = [1, 2, 3]
print(f"列表: 可迭代物件 ✓, 迭代器 ✗")

# 當對 list 呼叫 iter() 後，回傳的那個新物件，才是「迭代器」
my_iter = iter(my_list)
print(f"iter(列表): 可迭代物件 ✗, 迭代器 ✓")

# 實際上，設計良好的「迭代器」本身也會實作 __iter__() 並回傳自己（return self）
# 因此迭代器本身通常也是可迭代物件。
print(f"迭代器: 可迭代物件 ✓ (有__iter__), 迭代器 ✓ (有__next__)")


# 5. 處理 StopIteration 例外
print("\n--- StopIteration 用法 ---")

# 手動遍歷的標準寫法（這就是 for 迴圈在底層做的事情）
def manual_iter(items):
    # 先取得迭代器
    it = iter(items)
    while True:
        try:
            # 不斷嘗試取出下一個元素
            item = next(it)
            print(f"取得: {item}")
        except StopIteration:
            # 遇到 StopIteration 代表東西拿完了，主動跳出無窮迴圈
            break

manual_iter(["a", "b", "c"])


# 另一種更簡潔的手動遍歷：利用 next() 的第二個參數 (預設值)
def manual_iter_default(items):
    it = iter(items)
    while True:
        # 當拿不到東西時，不再拋出 StopIteration，而是回傳指定的預設值（這裡是 None）
        item = next(it, None)  
        
        # 檢查是否拿到預設值，是的話就代表結束了
        if item is None:
            break
        print(f"取得: {item}")

print("\n使用預設值:")
manual_iter_default(["a", "b", "c"])
