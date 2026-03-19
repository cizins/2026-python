# UVA 272: TEX Quotes
# 簡單版 - 更容易記憶的寫法 (-easy)

def solve_easy(text):
    """
    用極簡短、更容易記憶的方式解決 UVA 272 雙引號替換問題。
    """
    res = ""
    # 用一個變數記錄是否為左引號 (開頭引號)
    is_left = True
    
    # 遍歷所有的字元
    for c in text:
        if c == '"':
            # 如果是雙引號，根據 is_left 的狀態選擇要替換的字串
            # 使用 Python 的條件運算式 (三元運算子) 讓程式碼更簡潔
            res += "``" if is_left else "''"
            
            # 替換後，反轉 is_left 的狀態 (True變False，False變True)
            is_left = not is_left
        else:
            # 不是雙引號的話，直接把字元加上去
            res += c
            
    return res

if __name__ == '__main__':
    import sys
    # 讀取所有的標準輸入資料並處理
    data = sys.stdin.read()
    if data:
        # sys.stdout.write 不會像 print 一樣自動幫你加換行
        # 這樣能保證輸出完全等於轉換後的結果
        sys.stdout.write(solve_easy(data))
