import sys

def solve_easy(input_text):
    """
    UVA 118 簡單解題版本 (-easy版)
    利用字典(dictionary)來對應方向和移動，直觀好讀，非常適合初學者記憶和理解。
    """
    # 步驟 1: 處理輸入資料
    # 將輸入字串依據換行符號切開，取得每一行的資料
    lines = input_text.strip().split('\n')
    if not lines: return ""
    
    # 步驟 2: 解析地圖邊界
    # 第一行包含右上角座標，分別為最大的 x 與 y 值
    top_right = lines[0].split()
    max_x = int(top_right[0])
    max_y = int(top_right[1])
    
    # 步驟 3: 準備變數
    # 用 set (集合) 來記錄所有掉下去的機器人留下的「氣味」(座標點)
    # 使用 set 是因為尋找元素的速度極快 (O(1))
    scents = set()
    # output 陣列用來儲存每個機器人的最終結果字串
    output = []
    
    # 步驟 4: 定義方向規則 (核心好記法)
    # 定義每一個方向前進時，x 和 y 會如何變化 (x位移, y位移)
    # N: 北方 y+1, E: 東方 x+1, S: 南方 y-1, W: 西方 x-1
    moves = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }
    
    # 定義向左轉(L)的結果，利用字典一對一映射，非常直覺
    turn_left = {
        'N': 'W', # 面向北向左轉會變西
        'W': 'S', # 面向西向左轉會變南
        'S': 'E', # 面向南向左轉會變東
        'E': 'N'  # 面向東向左轉會變北
    }
    
    # 定義向右轉(R)的結果
    turn_right = {
        'N': 'E', # 面向北向右轉會變東
        'E': 'S', # 面向東向右轉會變南
        'S': 'W', # 面向南向右轉會變西
        'W': 'N'  # 面向西向右轉會變北
    }
    
    # 步驟 5: 逐一處理每個機器人
    # 因為每個機器人的資料佔 2 行 (第一行初始狀態，第二行指令集)，所以迴圈一次跳 2 步
    for i in range(1, len(lines), 2):
        # 防呆檢查：確保不超出範圍或讀到空行
        if i >= len(lines) or not lines[i].strip():
            continue
            
        # 讀取機器人的初始狀態
        init_state = lines[i].split()
        if len(init_state) < 3: 
            continue
            
        x = int(init_state[0])     # 初始 X 座標
        y = int(init_state[1])     # 初始 Y 座標
        facing = init_state[2]     # 初始面向方向 (N, S, E, W)
        
        # 讀取緊接著下一行的指令集 (L, R, F 組合字串)
        commands = lines[i+1].strip()
        
        # 標記機器人是否已經掉下去的布林變數
        is_lost = False
        
        # 步驟 6: 執行機器人指令
        for cmd in commands:
            if cmd == 'L':
                # 利用左轉字典，直接更新當前面向的方向
                facing = turn_left[facing]
                
            elif cmd == 'R':
                # 利用右轉字典，直接更新當前面向的方向
                facing = turn_right[facing]
                
            elif cmd == 'F':
                # 取出當前方向對應的位移量
                dx, dy = moves[facing]
                
                # 計算如果前進一步後的新座標
                next_x = x + dx
                next_y = y + dy
                
                # 檢查這個新座標是否已經超出了地圖邊界
                if next_x < 0 or next_x > max_x or next_y < 0 or next_y > max_y:
                    
                    # 判斷當前所在格子是否已經有「氣味」
                    if (x, y) in scents:
                        # 有氣味代表之前有機器人從這裡掉下去過
                        # 所以我們「忽略」這個致命的往前走指令，繼續執行下一個指令
                        continue
                    else:
                        # 當前格子沒有氣味，機器人會掉下去！
                        # 把這個掉落的邊緣座標加入氣味集合中
                        scents.add((x, y))
                        
                        # 標記機器人遺失，並且「停止」執行後續所有指令
                        is_lost = True
                        break
                        
                else:
                    # 在邊界內，安全前進！更新現在的座標到新位置
                    x = next_x
                    y = next_y
                    
        # 步驟 7: 紀錄最終結果
        if is_lost:
            # 如果掉下去，要多輸出一個 'LOST'，並保留最後一次安全的座標
            output.append(f"{x} {y} {facing} LOST")
        else:
            # 安全結束所有指令，直接輸出座標和方向
            output.append(f"{x} {y} {facing}")
            
    # 最後把所有機器人的結果，用換行符號連接起來成為最終字串回傳
    return '\n'.join(output)

def main():
    # 處理終端機的標準輸入，方便系統測資批改
    input_text = sys.stdin.read()
    print(solve_easy(input_text))

if __name__ == "__main__":
    main()