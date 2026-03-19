import sys

def solve(input_text):
    """
    UVA 272: TEX Quotes 核心解題邏輯 (標準版)
    利用一個布林變數 (boolean) 紀錄目前遇到的是「左引號」還是「右引號」。
    """
    result = []
    # is_left_quote 用來追蹤現在遇到雙引號 (") 時，應該要替換成左引號還是右引號
    # 初始為 True，表示遇到的第一個雙引號要換成左引號 (``)
    is_left_quote = True
    
    # 逐字元掃描整個輸入字串
    for char in input_text:
        if char == '"':
            if is_left_quote:
                # 遇到左引號，替換為兩個反引號 (backquote)
                result.append("``")
            else:
                # 遇到右引號，替換為兩個單引號 (apostrophe)
                result.append("''")
            
            # 切換狀態：下一次遇到的雙引號就會變成相反的替換字元
            is_left_quote = not is_left_quote
        else:
            # 不是雙引號的字元，直接原封不動加入結果陣列
            result.append(char)
            
    # 將結果陣列組合成字串並回傳
    return "".join(result)

def main():
    # 讀取標準輸入 (sys.stdin.read() 會讀取直到 EOF 結束，包含所有換行)
    input_text = sys.stdin.read()
    if input_text:
        # sys.stdout.write 不會額外加上換行，保持與原始測資的空行行為一致
        sys.stdout.write(solve(input_text))

if __name__ == "__main__":
    main()