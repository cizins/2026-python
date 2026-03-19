import sys

def solve(input_text):
    """
    UVA 490: Rotating Sentences (標準版)
    
    解題核心：
    將多行字串往順時針方向旋轉 90 度。
    也就是說，原本的「行 (row)」會變成「列 (column)」。
    - 最後一行輸入會變成輸出的最左邊第一列。
    - 第一行輸入會變成輸出的最右邊一列。
    
    處理方式：
    1. 找出所有行中的最大長度 (決定輸出的總行數)。
    2. 雙層迴圈掃描：外層掃描字元索引 (0 ~ max_length)，內層「由下往上」掃描原本的字串陣列。
    3. 若該字串長度不足，補空白。
    """
    # 讀取所有行，splitlines() 會自動處理換行符號
    lines = input_text.splitlines()
    if not lines:
        return ""
        
    # 找出最長的一行，決定輸出會有多少「列」
    max_len = max(len(line) for line in lines)
    result = []
    
    # 依序處理每一「列」(對應到原本字串的第 i 個字元)
    for i in range(max_len):
        row_chars = []
        # 由下往上讀取 (因為最後一行要在最左邊)
        for line in reversed(lines):
            # 如果這行的長度夠長，就取第 i 個字元
            if i < len(line):
                row_chars.append(line[i])
            else:
                # 若長度不足，代表該處在原本矩陣中是空的，用空白補齊
                row_chars.append(" ")
        
        # 將這些字元組合成新的「一列」，加入結果陣列
        result.append("".join(row_chars))
        
    return "\n".join(result)

def main():
    # 讀取標準輸入，交給 solve 處理
    input_text = sys.stdin.read()
    if input_text:
        print(solve(input_text))

if __name__ == "__main__":
    main()