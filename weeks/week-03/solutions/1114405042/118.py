# UVA 118: Mutant Flathead Groteque 機器人指令
# 標準解法 - 物件導向與模組化設計

def solve_robot_instructions(input_text):
    """
    處理 UVA 118 機器人指令的核心函式。
    
    參數:
        input_text (str): 包含所有輸入測資的字串。
        
    回傳:
        str: 包含所有機器人最終狀態的字串，每行代表一個機器人。
    """
    # 處理輸入，將字串按空白分割成一個串列
    tokens = input_text.split()
    if not tokens:
        return ""

    # 前兩個 token 分別是地圖的右上角 x 與 y 座標 (最大邊界)
    max_x = int(tokens[0])
    max_y = int(tokens[1])
    
    # 用一個 set 來記錄發生過掉落 (LOST) 的座標點（也就是標記/氣味）
    scents = set()
    
    # 建立方向的對應關係。這裡順序很重要：北(N)、東(E)、南(S)、西(W)
    # 依序排列（順時針）可方便使用 index + 1 來表示右轉，index - 1 表示左轉
    directions = ['N', 'E', 'S', 'W']
    
    # 定義各個方向前進 (Forward) 時，x 與 y 的變化量 (dx, dy)
    moves = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }

    # 使用索引變數從第三個 token 開始讀取機器人資料
    idx = 2
    results = []
    
    # 當還有未處理的 token 時，持續進行處理
    while idx < len(tokens):
        # 讀取機器人的初始位置與方向
        x = int(tokens[idx])
        y = int(tokens[idx+1])
        d = tokens[idx+2]
        
        # 讀取機器人的指令集
        instructions = tokens[idx+3]
        idx += 4
        
        # 記錄機器人是否已經掉落出界
        is_lost = False
        
        # 逐一執行指令
        for instr in instructions:
            if instr == 'L':
                # 左轉 90 度：方向索引減 1，利用 % 4 讓它在 0~3 之間循環
                current_idx = directions.index(d)
                d = directions[(current_idx - 1) % 4]
            elif instr == 'R':
                # 右轉 90 度：方向索引加 1，利用 % 4 讓它在 0~3 之間循環
                current_idx = directions.index(d)
                d = directions[(current_idx + 1) % 4]
            elif instr == 'F':
                # 前進：計算下一步的新座標
                dx, dy = moves[d]
                nx = x + dx
                ny = y + dy
                
                # 檢查新座標是否超出邊界 (小於 0 或大於 max_x/max_y)
                if nx < 0 or nx > max_x or ny < 0 or ny > max_y:
                    # 如果當前位置已經有標記 (scent)，則忽略這個會掉下去的指令
                    if (x, y) in scents:
                        continue
                    else:
                        # 否則，機器人掉落，在當前位置留下標記，並終止後續指令
                        scents.add((x, y))
                        is_lost = True
                        break
                else:
                    # 安全前進，更新位置
                    x = nx
                    y = ny
                    
        # 將機器人的最終狀態格式化並加入結果列表
        if is_lost:
            results.append(f"{x} {y} {d} LOST")
        else:
            results.append(f"{x} {y} {d}")

    # 回傳結果，以換行符號連接
    return "\n".join(results)

if __name__ == '__main__':
    import sys
    # 從標準輸入讀取所有資料，傳入求解函式後印出
    input_data = sys.stdin.read()
    if input_data.strip():
        print(solve_robot_instructions(input_data))
