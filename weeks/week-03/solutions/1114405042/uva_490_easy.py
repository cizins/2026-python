import sys

def solve_easy(input_text):
    """
    UVA 490: Rotating Sentences (簡單好記版 - easy)
    
    這個版本特別適合初學者！我們把這個看似複雜的「選轉」問題，拆解成幾個無腦的簡單步驟。
    既然題目怕有些行太短導致轉過來有缺角，我們乾脆一開始「就把所有行都補上空白，讓大家都一樣長」。
    這樣旋轉的時候就像是在轉一個完美的長方形，完全不用寫 if 去判斷有沒有缺字！
    """
    # 步驟 1: 把輸入的整坨文字，按照「換行」切開，變成一行一行的清單
    lines = input_text.splitlines()
    if not lines:
        return ""
        
    # 步驟 2: 找出這群文字裡面，最長的那一行到底有幾個字？
    max_length = 0
    for line in lines:
        if len(line) > max_length:
            max_length = len(line)
            
    # 步驟 3: 把每一行都用「空白」補齊到相同的長度
    # 舉例：原本是 "123"，如果最長是 5，就會變成 "123  "
    # Python 有一個超好用的內建功能叫 ljust(長度)，它會幫你在右邊補空白！
    padded_lines = []
    for line in lines:
        padded_lines.append(line.ljust(max_length))
        
    # 準備一個清單，用來裝旋轉過後的結果
    result = []
    
    # 步驟 4: 開始「順時針 90 度」旋轉
    # 原本的「直行(column)」現在要變成新的「橫列(row)」
    for col in range(max_length):
        
        # 準備組合新的一行
        new_row = ""
        
        # 為什麼要「由下往上」讀呢？
        # 因為順時針旋轉 90 度後，原本在最下面(最後一行)的文字，會跑到最左邊！
        # range(起點, 終點(不包含), 步長) -> 這樣寫可以從最後一個索引一路倒退到 0
        for row in range(len(padded_lines) - 1, -1, -1):
            
            # 把字元一個一個黏起來
            new_row += padded_lines[row][col]
            
        # 黏好的一整行，就把它收進結果清單裡
        result.append(new_row)
        
    # 最後，把這些新的橫列，用「換行符號」接起來，印出最終答案
    return "\n".join(result)

def main():
    # 處理終端機的標準輸入
    input_text = sys.stdin.read()
    if input_text:
        print(solve_easy(input_text))

if __name__ == "__main__":
    main()