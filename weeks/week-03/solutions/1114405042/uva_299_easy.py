import sys

def solve_easy(input_text):
    """
    UVA 299: Train Swapping (簡單好記版 - easy)
    
    這個版本非常適合初學者！
    既然題目問「只交換相鄰的車廂，要把數字從小排到大，總共要換幾次？」
    這完完全全就是「泡沫排序法 (Bubble Sort)」的定義呀！
    
    所以我們最直觀的解法，就是直接寫一個泡沫排序法，
    然後只要發生交換，就把次數 +1，這樣就一定不會錯了！
    """
    # 步驟 1: 把所有輸入內容根據空白或換行切成一個個字詞 (Token)
    # 這樣就不用擔心有些數字擠在同一行、有些被斷行的問題
    tokens = input_text.split()
    
    # 準備一個清單，用來收集所有要輸出的答案
    output_answers = []
    
    # 如果輸入是空的，直接結束
    if not tokens:
        return ""
        
    # 第一個數字是測試資料的總數量
    num_test_cases = int(tokens[0])
    
    # token_idx 用來記住我們目前讀到了第幾個字
    token_idx = 1
    
    # 步驟 2: 跑迴圈，處理每一筆測試資料
    for _ in range(num_test_cases):
        
        # 每筆測資的第一個數字，是火車的總長度
        train_length = int(tokens[token_idx])
        token_idx += 1
        
        # 建立一個清單，依序把目前的車廂號碼讀進來
        train_cars = []
        for _ in range(train_length):
            train_cars.append(int(tokens[token_idx]))
            token_idx += 1
            
        # 步驟 3: 實作泡沫排序法 (Bubble Sort) 並計算交換次數
        # swap_count 用來累計我們到底交換了幾次
        swap_count = 0
        
        # 外層迴圈：代表要執行幾次「把最大數字推到最後面」的過程
        for i in range(train_length):
            
            # 內層迴圈：負責尋找相鄰的兩個數字
            # 注意範圍是到 train_length - 1 - i，因為後面的 i 個數字已經排好，不用再檢查了
            for j in range(train_length - 1 - i):
                
                # 如果前面的車廂號碼大於後面的車廂號碼，就必須交換它們
                if train_cars[j] > train_cars[j+1]:
                    # 進行相鄰車廂交換 (Swap)
                    temp = train_cars[j]             # 先把前面的車廂放到暫存區 temp
                    train_cars[j] = train_cars[j+1]  # 把後面的車廂移到前面
                    train_cars[j+1] = temp           # 把暫存區裡的車廂放回後面
                    
                    # 交換完成，交換次數 +1
                    swap_count += 1
                    
        # 步驟 4: 記錄這筆測資的結果
        output_answers.append(f"Optimal train swapping takes {swap_count} swaps.")
        
    # 最後，把所有的答案用換行符號(\n)連接起來，變成一個大字串並回傳
    return "\n".join(output_answers)

def main():
    # 處理終端機的標準輸入，方便系統測資批改
    input_text = sys.stdin.read()
    if input_text.strip():
        print(solve_easy(input_text))

if __name__ == "__main__":
    main()