# UVA 118: Mutant Flathead Groteque 機器人指令
# 簡單版 - 更容易記憶的寫法 (-easy)

def solve_easy(input_text):
    """
    用更精簡、更容易記憶的方式解決 UVA 118 機器人指令問題。
    """
    tokens = input_text.split()
    if not tokens:
        return ""
        
    max_x, max_y = int(tokens[0]), int(tokens[1])
    scents = set()
    
    # 建立一個方向字串，依順時針排列：北、東、南、西
    dirs = "NESW"
    # 對應的 x, y 變化量，與 dirs 字串的順序完全對應
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    idx = 2
    res = []
    
    while idx < len(tokens):
        x = int(tokens[idx])
        y = int(tokens[idx+1])
        # 使用 find 找到方向的索引 (0~3)
        d_idx = dirs.find(tokens[idx+2])
        instructions = tokens[idx+3]
        idx += 4
        
        lost = False
        for instr in instructions:
            if instr == 'L':
                # 左轉：索引減 1 (用 %4 確保循環)
                d_idx = (d_idx - 1) % 4
            elif instr == 'R':
                # 右轉：索引加 1
                d_idx = (d_idx + 1) % 4
            elif instr == 'F':
                # 前進：根據目前方向索引取得變化量
                dx, dy = moves[d_idx]
                nx, ny = x + dx, y + dy
                
                # 檢查是否掉出邊界
                if not (0 <= nx <= max_x and 0 <= ny <= max_y):
                    # 如果該位置已經有氣味，忽略這個指令
                    if (x, y) in scents:
                        continue
                    else:
                        # 否則掉落，紀錄氣味，標記 LOST
                        scents.add((x, y))
                        lost = True
                        break
                else:
                    # 安全前進
                    x, y = nx, ny
                    
        # 紀錄結果
        final_dir = dirs[d_idx]
        if lost:
            res.append(f"{x} {y} {final_dir} LOST")
        else:
            res.append(f"{x} {y} {final_dir}")
            
    return "\n".join(res)

if __name__ == '__main__':
    import sys
    data = sys.stdin.read()
    if data.strip():
        print(solve_easy(data))
