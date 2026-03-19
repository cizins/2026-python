# UVA 272: TEX Quotes
# 標準解法 - 模組化與型別提示

def solve_tex_quotes(text: str) -> str:
    """
    處理 UVA 272 TEX Quotes 的核心函式。
    
    將輸入文字中的雙引號 (") 替換為 TeX 格式的引號：
    - 第一個遇到的雙引號替換為 `` (兩個左單引號，backquote)
    - 第二個遇到的雙引號替換為 '' (兩個右單引號，apostrophe)
    - 依此類推交替進行
    
    參數:
        text (str): 包含所有輸入測資的完整字串。
        
    回傳:
        str: 替換完雙引號後的字串。
    """
    result = []
    
    # 布林標記，用來記錄目前是否處於等待「開頭引號」的狀態
    # True 代表下一個遇到的 " 是引言的開始，要換成 ``
    # False 代表下一個遇到的 " 是引言的結束，要換成 ''
    open_quote = True
    
    # 逐字元檢查輸入字串
    for char in text:
        if char == '"':
            if open_quote:
                # 是開頭引號，替換並切換狀態
                result.append("``")
            else:
                # 是結尾引號，替換並切換狀態
                result.append("''")
            
            # 狀態反轉，讓下一個引號做不同的替換
            open_quote = not open_quote
        else:
            # 如果不是雙引號，就原封不動加入結果陣列中
            result.append(char)
            
    # 將結果陣列合併成一個完整的字串回傳
    return "".join(result)

if __name__ == '__main__':
    import sys
    # 從標準輸入讀取全部資料 (包含換行與空白)，傳入函式處理後直接輸出
    input_data = sys.stdin.read()
    if input_data:
        # 使用 end="" 避免 print 自動在結尾多加一個換行，
        # 確保輸出格式完全跟輸入匹配
        print(solve_tex_quotes(input_data), end="")
