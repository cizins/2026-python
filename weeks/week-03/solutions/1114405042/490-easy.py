# UVA 490: Rotating Sentences
# 簡單版 - 更容易記憶的寫法 (-easy)

def solve_easy(input_text):
    """
    用極簡短、更容易記憶的方式解決 UVA 490 句子旋轉問題。
    """
    # 按照換行符號將輸入切分成列表
    lines = input_text.splitlines()
    if not lines:
        return ""
        
    # 取得最長句子的長度，決定外層迴圈次數 (輸出的行數)
    max_len = max(len(x) for x in lines)
    res = []
    
    # i 是直行的索引 (0 到 max_len - 1)
    for i in range(max_len):
        row = ""
        # 反向走訪每一句話 (從最後一行到第一行)
        for line in reversed(lines):
            # 如果這句話夠長，就把字元加進來，否則補上空白
            if i < len(line):
                row += line[i]
            else:
                row += " "
        res.append(row)
        
    return "\n".join(res)

if __name__ == '__main__':
    import sys
    data = sys.stdin.read()
    if data:
        print(solve_easy(data))
