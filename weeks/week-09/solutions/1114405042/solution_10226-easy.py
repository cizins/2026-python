# 解決 10226 (DFS 排列組合問題) - 手打簡易版
# 題意：給定 N 個人，找出符合條件（沒有人排在不想要的位置）的所有排列，
# 並且輸出時，與上一個排列相同的前綴不輸出。

def solve_10226_easy():
    import sys
    
    # 讀取所有輸入資料
    lines = sys.stdin.read().split()
    if not lines:
        return
        
    idx = 0
    while idx < len(lines):
        n = int(lines[idx])
        idx += 1
        
        # 建立不喜歡的位置的集合陣列 (0-indexed)
        dislikes = [set() for _ in range(n)]
        for i in range(n):
            while idx < len(lines):
                val = int(lines[idx])
                idx += 1
                if val == 0:
                    break
                dislikes[i].add(val - 1)
                
        # prev_arr 用來記錄上一次輸出的完整排列
        prev_arr = []
        # used 陣列用來記錄某個人是否已經排進去
        used = [False] * n
        # curr_arr 記錄目前的排列
        curr_arr = []
        
        def dfs(depth):
            nonlocal prev_arr
            # 如果深度等於 n，代表找到一組完整的排列
            if depth == n:
                # 找出與上一次排列不同的起始位置
                diff_idx = 0
                while diff_idx < n and prev_arr and prev_arr[diff_idx] == curr_arr[diff_idx]:
                    diff_idx += 1
                
                # 印出不同的部分
                for i in range(diff_idx, n):
                    # 將 0~25 轉換成 A~Z
                    print(chr(curr_arr[i] + 65), end='')
                print()
                
                # 更新 prev_arr
                prev_arr = list(curr_arr)
                return
                
            # 嘗試將每個人放到目前的 depth 位置
            for i in range(n):
                if not used[i] and depth not in dislikes[i]:
                    used[i] = True
                    curr_arr.append(i)
                    dfs(depth + 1)
                    # 回溯 (Backtracking)
                    curr_arr.pop()
                    used[i] = False
                    
        dfs(0)
        print() # 測資之間可能需要空白行，視題意調整

if __name__ == '__main__':
    solve_10226_easy()
