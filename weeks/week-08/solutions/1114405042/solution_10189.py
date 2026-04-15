import sys

def solve(input_data: str) -> str:
    """
    解題思路 (標準版)：
    1. 讀取所有輸入，按行分割。
    2. 解析 n 和 m，若為 0 0 則結束。
    3. 建立 2D 陣列 (Grid) 儲存地雷和空白。
    4. 遍歷每個格子，若是空白 '.'，則檢查其周圍 8 個方向 (需要做邊界檢查防止 IndexError)。
    5. 計算周圍的 '*' 數量並轉換成字串。
    6. 依照題目要求的格式輸出 (注意 Field 之間的空行)。
    """
    lines = input_data.strip().split('\n')
    idx = 0
    field_num = 1
    results = []
    
    while idx < len(lines):
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
        grid = []
        # 讀取地圖資料
        for _ in range(n):
            grid.append(list(lines[idx].strip()))
            idx += 1
            
        # 兩筆測資之間需要空行，但第一筆前面不用
        if field_num > 1:
            results.append("")
            
        results.append(f"Field #{field_num}:")
        
        # 遍歷網格計算地雷數
        for r in range(n):
            row_res = []
            for c in range(m):
                if grid[r][c] == '*':
                    row_res.append('*')
                else:
                    count = 0
                    # 檢查周圍 8 個方向
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if dr == 0 and dc == 0:
                                continue
                            nr, nc = r + dr, c + dc
                            # 邊界檢查：確保新的座標在網格範圍內
                            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '*':
                                count += 1
                    row_res.append(str(count))
            # 將整行結果合併後加入 results
            results.append("".join(row_res))
            
        field_num += 1
        
    return "\n".join(results)

if __name__ == "__main__":
    # 支援從標準輸入讀取資料 (給 OJ 平台測試用)
    input_text = sys.stdin.read()
    if input_text.strip():
        print(solve(input_text))
