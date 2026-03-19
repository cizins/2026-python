import sys

def solve_easy(input_text):
    """
    UVA 272 簡單解題版本 (-easy版)
    這是一個利用 Python 內建的 split() 函數所寫的「奇招」，對於初學者非常好記！
    
    邏輯解析：
    如果我們把字串用雙引號 (") 切開 (split)，例如 `"A" B "C"` 會變成：
    [空白, 'A', ' B ', 'C', 空白]
    
    你會發現：
    第 0, 2, 4... (偶數索引) 都是雙引號「外面」的文字，不需要改動。
    第 1, 3, 5... (奇數索引) 都是被雙引號「包起來」的文字。
    
    所以只要把切開後的陣列重新接起來：
    遇到偶數索引時 -> 就是原本的文字
    遇到奇數索引前 -> 代表原本有個左引號 `"`，改成接上 ` `` `
    遇到奇數索引後 -> 代表原本有個右引號 `"`，改成接上 ` '' `
    
    （其實最簡單的方式，是直接用一個變數切換「左」「右」來逐個替換字串的元件）
    這邊我們用最直觀、易讀的布林開關(Boolean switch) 寫法。
    """
    
    # 建立一個清單來裝處理完的文字
    result = []
    
    # 宣告一個「開關」，用來記錄我們現在「是否要換成左邊的引號」
    # 第一個遇到的引號一定是左邊，所以初始值設為 True
    is_left = True
    
    # 我們「一個字元、一個字元」的讀取整個輸入
    for char in input_text:
        # 如果這個字元是雙引號 (")
        if char == '"':
            # 判斷現在開關的狀態，看看該給左引號還是右引號
            if is_left == True:
                # 第一個遇到的雙引號，把它換成兩個左單引號 (反引號)
                result.append("``")
                # 用過左引號了，把開關切換為 False，下次遇到就會用右引號
                is_left = False
            else:
                # 再次遇到雙引號，因為開關是 False，把它換成兩個右單引號
                result.append("''")
                # 右引號也用過了，把開關切換為 True，準備下一次遇到雙引號又可以變成左邊
                is_left = True
                
        # 如果不是雙引號，那就什麼都不用改，直接裝進結果裡
        else:
            result.append(char)
            
    # 最後把裝著單一字元的清單，全部連起來變回一整串文字
    return ''.join(result)

def main():
    # 處理終端機的標準輸入，方便系統測資批改
    input_text = sys.stdin.read()
    # 輸出最終轉換好的字串
    if input_text:
        sys.stdout.write(solve_easy(input_text))

if __name__ == "__main__":
    main()