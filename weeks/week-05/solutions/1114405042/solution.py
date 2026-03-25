import sys

def solve(relatives):
    """
    計算 Vito 到所有親戚家的最小總距離。
    這是一個經典的數學問題：在一維座標上，到所有點距離總和最小的點就是這些點的「中位數」。
    """
    if not relatives:
        return 0
        
    # 步驟 1：將所有親戚的門牌號碼由小到大排序
    sorted_relatives = sorted(relatives)
    n = len(sorted_relatives)
    
    # 步驟 2：找出中位數
    # 如果數量是奇數，中位數就是最中間的數
    # 如果數量是偶數，中間有兩個數，取其中任何一個當基準點，總距離都是一樣的（這裡取 n // 2）
    median = sorted_relatives[n // 2]
    
    # 步驟 3：計算所有親戚家到該中位數位置的距離總和
    total_distance = sum(abs(x - median) for x in sorted_relatives)
    
    return total_distance

def main():
    # 一次性讀取所有輸入資料，並以空白或換行符號分割成字串列表
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    # 第一個輸入值代表有幾組測試資料
    num_test_cases = int(input_data[0])
    idx = 1
    
    # 迴圈處理每一組測試資料
    for _ in range(num_test_cases):
        if idx >= len(input_data):
            break
            
        # 讀取這組測試資料的親戚數量 r
        r = int(input_data[idx])
        idx += 1
        
        # 根據數量 r，讀取對應數量的親戚門牌號碼
        relatives = [int(input_data[i]) for i in range(idx, idx + r)]
        idx += r
            
        # 計算並輸出這組資料的最小總距離
        print(solve(relatives))

if __name__ == '__main__':
    main()
