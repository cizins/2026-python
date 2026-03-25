def solve(n, arr):
    """
    計算 UVA 10057: Mid-Summer Night's Dream 的三個答案。
    1. 能使距離總和最小的最小可能的 A (中位數)。
    2. 在原本輸入的陣列中，有多少個數字等於任何一個最佳的 A。
    3. 總共有幾種可能的 A 值。
    """
    arr.sort()
    
    # 計算最佳的 A 的範圍 (中位數區間)
    if n % 2 == 1:
        # 如果是奇數，中位數只有一個
        min_a = arr[n // 2]
        max_a = arr[n // 2]
    else:
        # 如果是偶數，中位數是中間兩個數字及其之間的任何整數
        min_a = arr[n // 2 - 1]
        max_a = arr[n // 2]
        
    # 計算陣列中有多少個元素落在 [min_a, max_a] 區間內
    # 這些元素就是「符合最佳 A 條件的原本輸入數字」
    count = 0
    for x in arr:
        if min_a <= x <= max_a:
            count += 1
            
    # 計算有幾種可能的 A 值
    # 也就是區間 [min_a, max_a] 內包含的整數數量
    possible_a_count = max_a - min_a + 1
    
    return min_a, count, possible_a_count

import sys

def main():
    # 讀取標準輸入
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx])
        idx += 1
        
        arr = []
        for _ in range(n):
            arr.append(int(input_data[idx]))
            idx += 1
            
        ans1, ans2, ans3 = solve(n, arr)
        print(f"{ans1} {ans2} {ans3}")

if __name__ == '__main__':
    main()
