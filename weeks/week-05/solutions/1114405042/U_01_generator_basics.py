# Understand（理解）- 生成器概念
# 生成器 (Generator) 是一種特殊的迭代器，透過 yield 關鍵字來回傳值
# 它會記住當前執行的狀態，並在下次呼叫時從中斷處繼續執行，非常節省記憶體空間

# 1. 基本的浮點數範圍生成器
def frange(start, stop, step):
    """這是一個可以產生浮點數序列的生成器，類似內建的 range() 但支援浮點數 step"""
    x = start
    while x < stop:
        yield x       # 產生當前的值，並暫停執行，將控制權交還給呼叫者
        x += step     # 下次呼叫 next() 時，會從這裡繼續執行

# 使用 list() 將生成器產生的所有值一次性取出並轉成列表
result = list(frange(0, 2, 0.5))
print(f"frange(0, 2, 0.5): {result}")


# 2. 觀察生成器的執行流程
def countdown(n):
    print(f"Starting countdown from {n}") # 這行只有在第一次呼叫 next() 時才會執行
    while n > 0:
        yield n  # 每次呼叫 next() 時回傳 n，並暫停
        n -= 1   # 下次呼叫 next() 從這裡繼續
    print("Done!") # 當沒有更多 yield 可執行時，會擲出 StopIteration，同時印出此行


print("\n--- 建立生成器 ---")
# 呼叫生成器函式並不會馬上執行裡面的程式碼，而是回傳一個生成器物件 (generator object)
c = countdown(3)
print(f"生成器物件: {c}")

print("\n--- 逐步迭代 ---")
# 每次呼叫 next() 會推進到下一個 yield 的位置並回傳其值
print(f"next(c): {next(c)}") # 執行到第一個 yield，印出 "Starting..." 並回傳 3
print(f"next(c): {next(c)}") # 從上一次暫停的地方繼續執行 n-=1，然後遇到 yield 回傳 2
print(f"next(c): {next(c)}") # 繼續執行 n-=1，遇到 yield 回傳 1

# 當生成器函式執行完畢 (沒有 yield 可以執行時)
try:
    next(c) # 嘗試獲取下一個值，會執行 print("Done!") 並擲出 StopIteration
except StopIteration:
    print("StopIteration!")


# 3. 無窮生成器 (Infinite Generator)
def fibonacci():
    """產生費式數列的無窮生成器。由於是生成器，不會因為無限迴圈而耗盡記憶體"""
    a, b = 0, 1
    while True: # 無窮迴圈
        yield a
        a, b = b, a + b # 每次計算下一個費式數列的值


print("\n--- Fibonacci 生成器 ---")
fib = fibonacci()
# 只取前 10 個值，然後停止迭代
for i in range(10):
    print(next(fib), end=" ")
print()


# 4. yield from 的用法
def chain_iter(*iterables):
    """
    接收多個可迭代物件，並將它們串接在一起。
    yield from <iterable> 等同於:
        for x in <iterable>:
            yield x
    它是用來委派生成器的簡潔語法。
    """
    for it in iterables:
        yield from it # 把內部可迭代物件的元素一個一個 yield 出去


print("\n--- yield from 用法 ---")
result = list(chain_iter([1, 2], [3, 4], [5, 6]))
print(f"chain_iter: {result}")


# 5. 使用 yield from 進行遞迴處理：樹結構遍歷
class Node:
    """一個簡單的樹節點類別"""
    def __init__(self, value):
        self.value = value
        self.children = [] # 儲存子節點的列表

    def add_child(self, node):
        self.children.append(node)

    def __iter__(self):
        # 讓 Node 物件可以被迭代，預設迭代其子節點
        return iter(self.children)

    def depth_first(self):
        """深度優先遍歷 (Depth-First Search) 的生成器"""
        yield self # 先回傳當前節點本身
        for child in self: # 迭代所有子節點
            # 遞迴地從每個子節點中產出它的深度優先遍歷結果
            yield from child.depth_first()


print("\n--- 樹的深度優先遍歷 ---")
# 建立一個簡單的樹結構:
#     0
#    / \
#   1   2
#  / \
# 3   4
root = Node(0)
root.add_child(Node(1))
root.add_child(Node(2))
root.children[0].add_child(Node(3))
root.children[0].add_child(Node(4))

# 使用深度優先生成器遍歷樹
for node in root.depth_first():
    print(node.value, end=" ")
print()


# 6. 使用 yield from 進行遞迴處理：攤平巢狀列表
def flatten(items):
    """將任意深度的巢狀可迭代物件攤平為單層結構"""
    for x in items:
        # 檢查 x 是否為可迭代物件 (有 __iter__ 方法)，但排除字串 (避免字串被拆解成單一字元)
        if hasattr(x, "__iter__") and not isinstance(x, str):
            # 如果是嵌套的可迭代物件，遞迴呼叫 flatten 並將產生的元素 yield 出去
            yield from flatten(x)
        else:
            # 如果是單一元素，直接 yield
            yield x


print("\n--- 巢狀序列攤平 ---")
nested = [1, [2, [3, 4]], 5]
# 透過遞迴與 yield from，輕鬆將多層嵌套的列表攤平為 [1, 2, 3, 4, 5]
print(f"展開: {list(flatten(nested))}")