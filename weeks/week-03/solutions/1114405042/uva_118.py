import sys

def solve(input_text):
    """
    UVA 118 核心解題邏輯 (標準版)
    利用陣列與索引來處理方向轉換，執行效率稍高但需要稍微理解索引的對應關係。
    """
    lines = input_text.strip().split('\n')
    if not lines or not lines[0]: return ""
    
    # 讀取地圖邊界 (右上角座標)
    parts = lines[0].strip().split()
    max_x, max_y = int(parts[0]), int(parts[1])
    
    scents = set() # 記錄有掉落氣味的座標點
    result = []
    
    # 使用陣列儲存方向，依照順時針排列：北、東、南、西
    directions = ['N', 'E', 'S', 'W']
    # 對應的 x, y 軸位移量
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    idx = 1
    while idx < len(lines):
        line = lines[idx].strip()
        if not line:
            idx += 1
            continue
        
        # 讀取機器人初始位置與方向
        parts = line.split()
        if len(parts) < 3:
            idx += 1
            continue
            
        x, y, d = int(parts[0]), int(parts[1]), parts[2]
        idx += 1
        
        if idx >= len(lines):
            break
            
        # 讀取指令集
        commands = lines[idx].strip()
        idx += 1
        
        # 找出當前方向在陣列中的索引
        d_idx = directions.index(d)
        lost = False
        
        # 依序執行指令
        for cmd in commands:
            if cmd == 'L':
                # 向左轉：索引減 1 (加上 4 避免負數取餘數的問題，但在 Python 中負數取餘數仍是正確的)
                d_idx = (d_idx - 1) % 4
            elif cmd == 'R':
                # 向右轉：索引加 1
                d_idx = (d_idx + 1) % 4
            elif cmd == 'F':
                # 模擬往前走一步
                nx = x + dx[d_idx]
                ny = y + dy[d_idx]
                
                # 檢查是否超出邊界
                if nx < 0 or nx > max_x or ny < 0 or ny > max_y:
                    # 若此處已有標記(氣味)，則忽略這個會掉落的指令
                    if (x, y) in scents:
                        continue
                    else:
                        # 掉落邊界，留下標記並跳出迴圈
                        scents.add((x, y))
                        lost = True
                        break
                else:
                    # 未掉落，更新當前位置
                    x, y = nx, ny
                    
        # 紀錄執行結果
        if lost:
            result.append(f"{x} {y} {directions[d_idx]} LOST")
        else:
            result.append(f"{x} {y} {directions[d_idx]}")
            
    return "\n".join(result)

def main():
    # 讀取所有的標準輸入
    input_text = sys.stdin.read()
    print(solve(input_text))

if __name__ == "__main__":
    main()