import sys

# 這是針對 UVA 10057 (Mid-Summer Night's Dream) 題目的簡易好記版！
#
# 【解題核心概念】：
# 1. 這題一樣是找「中位數」，因為要讓所有點的絕對值距離和最小，最佳點一定在中位數上。
# 2. 但是題目要求輸出三個數字：
#    - 第一個：最小的可能中位數 (min_A)
#    - 第二個：輸入資料裡面，有幾個數字「剛好是」這些可能的中位數
#    - 第三個：總共有「幾種」可能的中位數
#
# 3. 怎麼算呢？
#    先排序 (sort)！
#    如果是奇數個：中位數只有正中間那個！ (min_A = max_A = arr[n//2])
#    如果是偶數個：中間有兩個數，從左邊到右邊的範圍內所有整數都可以是中位數！
#               (min_A = arr[n//2 - 1], max_A = arr[n//2])
#
#    那麼：
#    第一個答案 = min_A
#    第二個答案 = 原本陣列中，數值在 min_A 到 max_A 之間的數字有幾個
#    第三個答案 = max_A - min_A + 1 (區間內的整數個數)

def main():
    # 一次性讀取所有資料，以空白分割
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
        
    idx = 0
    while idx < len(data):
        # 讀取這組測資有幾個數字
        n = data[idx]
        
        # 取出這 n 個數字，並且直接進行「排序」
        arr = sorted(data[idx + 1 : idx + 1 + n])
        
        # 找中位數的邊界 (min_A 和 max_A)
        # 奇數的情況：例如 3 個數字，中間是第 1 個 (n//2)。左邊界 = 右邊界
        # 偶數的情況：例如 4 個數字，中間是第 1 個和第 2 個 (n//2 - 1 和 n//2)。
        if n % 2 == 1:
            min_a = arr[n // 2]
            max_a = arr[n // 2]
        else:
            min_a = arr[n // 2 - 1]
            max_a = arr[n // 2]
            
        # 答案 1：最小的可能 A (也就是左邊界)
        ans1 = min_a
        
        # 答案 2：輸入數字中，有幾個落在 [min_a, max_a] 之間
        # 只要用生成式配合 sum 就可以輕鬆算出個數
        ans2 = sum(1 for x in arr if min_a <= x <= max_a)
        
        # 答案 3：有幾種可能的中位數整數
        ans3 = max_a - min_a + 1
        
        # 輸出三個答案
        print(f"{ans1} {ans2} {ans3}")
        
        # 指標往後推 (1個數量 N + N 個數字)
        idx += 1 + n

if __name__ == '__main__':
    main()
