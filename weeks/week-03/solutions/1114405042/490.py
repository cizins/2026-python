# UVA 490: Rotating Sentences
# 標準解法 - 模組化與型別提示

def solve_rotating_sentences(input_text: str) -> str:
    """
    處理 UVA 490 句子旋轉問題的核心函式。
    
    將多行文字順時針旋轉 90 度：
    - 最後輸入的行將變成輸出的最左邊一列
    - 最先輸入的行將變成輸出的最右邊一列
    - 若該行長度不足，對應位置需以空白字元填補
    
    參數:
        input_text (str): 包含所有輸入的完整字串。
        
    回傳:
        str: 旋轉 90 度後的所有文字，以換行符號相接。
    """
    # 處理輸入，使用 splitlines() 而不是 split()，
    # 這樣可以保留句子中的空白字元，只在換行處進行切割。
    lines = input_text.splitlines()
    if not lines:
        return ""
        
    # 找出所有句子中最長的那一句的長度，這將決定輸出文字會有幾行 (高度)
    max_length = max(len(line) for line in lines)
    
    results = []
    
    # 針對旋轉後的每一行 (即原本每一句的第 i 個字元) 進行迭代
    for i in range(max_length):
        current_row_chars = []
        
        # 為了順時針旋轉 90 度，必須從「最後輸入的句子」開始往回讀取
        # 這樣最後一句就會在最左邊，第一句在最右邊
        for line in reversed(lines):
            if i < len(line):
                # 如果該句子的長度足夠長，有第 i 個字元，就取出該字元
                current_row_chars.append(line[i])
            else:
                # 若該句子長度不夠，則在該位置補上空白以維持矩形陣列結構
                current_row_chars.append(" ")
                
        # 將該列所有的字元組合成字串，並加入結果中
        results.append("".join(current_row_chars))
        
    return "\n".join(results)

if __name__ == '__main__':
    import sys
    # 從標準輸入讀取全部資料
    input_data = sys.stdin.read()
    if input_data:
        # 輸出旋轉後的結果
        print(solve_rotating_sentences(input_data))
