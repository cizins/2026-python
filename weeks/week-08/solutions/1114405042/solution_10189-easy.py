import sys

def solve_easy(input_data: str) -> str:
    """
    解題思路 (簡單、容易記憶版)：
    1. 這個版本使用「周圍加邊框」 (Padding) 的技巧，這在競程中非常常見。
    2. 由於原本的地圖是 n * m，我們將其擴展成 (n+2) * (m+2)，並在最外層填滿空白 '.'。
    3. 如此一來，任何一個原本的地圖點，其 8 個方向都會在合法範圍內 (不會超出 index 範圍)。
    4. 這樣就能省去所有繁瑣的 `0 <= r < n` 的邊界判斷，讓程式碼更簡潔易懂。
    5. 使用 sum() 結合 Generator Expression 也能讓計數更加優雅。
    """
    lines = input_data.strip().split('\n')
    idx = 0
    field_num = 1
    results = []
    
    while idx < len(lines):
        # 讀取 n 和 m
        line = lines[idx].strip()
        if not line:
            idx += 1
            continue
            
        parts = line.split()
        if len(parts) < 2:
            idx += 1
            continue
            
        n, m = map(int, parts)
        if n == 0 and m == 0:
            break
            
        idx += 1
        
        # 製作帶有邊框 (Padding) 的地圖
        padded_grid = []
        padded_grid.append('.' * (m + 2))  # 上方邊框
        for _ in range(n):
            # 每行的左、右兩邊各加上 '.'
            padded_grid.append('.' + lines[idx].strip() + '.')
            idx += 1
        padded_grid.append('.' * (m + 2))  # 下方邊框
        
        # 設定輸出格式
        if field_num > 1:
            results.append("")
        results.append(f"Field #{field_num}:")
        
        # 因為加了邊框，所以我們只檢查 [1, n] 行和 [1, m] 列的元素
        for r in range(1, n + 1):
            row_res = []
            for c in range(1, m + 1):
                if padded_grid[r][c] == '*':
                    row_res.append('*')
                else:
                    # 計算九宮格內 (包含自己) 地雷的數量
                    # 註：因為中心不是 '*' 所以包含自己一起計算也無妨 (只會加到 '*')
                    count = sum(
                        padded_grid[r + dr][c + dc] == '*'
                        for dr in [-1, 0, 1]
                        for dc in [-1, 0, 1]
                    )
                    row_res.append(str(count))
            # 合併字串
            results.append("".join(row_res))
            
        field_num += 1
        
    return "\n".join(results)

if __name__ == "__main__":
    # 若被直接執行，則由 sys.stdin 讀取測資
    input_text = sys.stdin.read()
    if input_text.strip():
        print(solve_easy(input_text))
