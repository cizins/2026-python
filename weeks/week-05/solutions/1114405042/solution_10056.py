def solve_probability(n, p, i):
    """
    計算第 i 個玩家在有 n 個玩家參與，單次成功機率為 p 的遊戲中獲勝的機率。
    
    這是一個無限等比級數求和的問題。
    設單次不成功的機率 q = 1 - p。
    
    第 i 個玩家在第 1 輪獲勝的機率是：前 i-1 個人都失敗，然後他成功。
    機率 = q^(i-1) * p
    
    第 i 個玩家在第 2 輪獲勝的機率是：第 1 輪所有人(n個人)都失敗，第 2 輪前 i-1 個人失敗，然後他成功。
    機率 = q^n * q^(i-1) * p
    
    以此類推，這是一個首項 a = q^(i-1) * p，公比 r = q^n 的無限等比級數。
    和 S = a / (1 - r) = [q^(i-1) * p] / [1 - q^n]
    
    參數:
    n (int): 玩家總數
    p (float): 單次投擲成功的機率
    i (int): 指定的玩家順位 (從 1 開始)
    
    回傳:
    float: 第 i 個玩家獲勝的機率 (返回原值，輸出時再四捨五入到小數後四位)
    """
    # 邊界條件：如果單次成功機率為 0，則沒有人會贏，機率為 0
    if p == 0:
        return 0.0

    q = 1.0 - p
    
    # a: 等比級數的首項，也就是在第 1 輪就獲勝的機率
    a = (q ** (i - 1)) * p
    
    # r: 等比級數的公比，也就是每一輪沒有人獲勝的機率 (全部 n 個人都失敗)
    r = q ** n
    
    # 應用無限等比級數求和公式：S = a / (1 - r)
    probability = a / (1.0 - r)
    
    return probability

import sys

def main():
    # 讀取標準輸入，將其全部拆分為字串陣列
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    # 第一個數字為測資數量 S
    num_test_cases = int(input_data[0])
    idx = 1
    
    for _ in range(num_test_cases):
        if idx >= len(input_data):
            break
            
        n = int(input_data[idx])
        p = float(input_data[idx+1])
        i = int(input_data[idx+2])
        idx += 3
        
        # 計算機率
        ans = solve_probability(n, p, i)
        
        # 題目要求輸出至小數點後第四位
        print(f"{ans:.4f}")

if __name__ == '__main__':
    main()
