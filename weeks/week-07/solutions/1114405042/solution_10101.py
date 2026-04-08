# 題目 10101 (火柴棒方程式)
#
# 題意：
# 給定一個由數字、加號(+)、減號(-)與等號(=)組成的字串，字尾以 '#' 結束。
# 我們只能移動「組成數字的其中一根火柴棒」，且不能動運算符號。
# 改變後，所有的數字仍然必須是合法的七段顯示器數字 (0-9)。
# 若能讓等式成立，輸出改變後的等式 (同樣以 '#' 結尾)；否則輸出 'No'。
#
# 解法 (枚舉所有可能的火柴棒移動)：
# 1. 整理出單一數字「內部移動一根火柴棒」可能變成的數字。
# 2. 整理出數字「減少一根火柴棒」可能變成的數字，以及「增加一根火柴棒」可能變成的數字。
# 3. 由於字串長度最多 1000，但數字長度不超過 7 位數，我們可以使用 eval() 或自訂函數快速計算等式是否成立。
# 4. 我們可以窮舉：
#    - 情境 A：在字串某個位置的數字進行內部移動。
#    - 情境 B：在字串某個位置的數字減少一根，並在另一個位置的數字增加一根。
# 5. 只要改動後等式兩邊的值相等，即代表找到答案。

import re

# 定義七段顯示器數字的火柴棒轉換規則
# 內部移動一根火柴棒可以變成的數字
INTERNAL_MOVES = {
    '0': ['6', '9'],
    '2': ['3'],
    '3': ['2', '5'],
    '5': ['3'],
    '6': ['0', '9'],
    '9': ['0', '6']
}

# 減少一根火柴棒可以變成的數字
REMOVE_STICK = {
    '6': ['5'],
    '7': ['1'],
    '8': ['0', '6', '9'],
    '9': ['3', '5'],
    '0': [], '1': [], '2': [], '3': [], '4': [], '5': []
}

# 增加一根火柴棒可以變成的數字
ADD_STICK = {
    '0': ['8'],
    '1': ['7'],
    '3': ['9'],
    '5': ['6', '9'],
    '6': ['8'],
    '9': ['8'],
    '2': [], '4': [], '7': [], '8': []
}


def evaluate_equation(eq_str: str) -> bool:
    """判斷等式是否成立"""
    try:
        left, right = eq_str.split('=')
        # 使用 eval 計算左右兩邊，注意要處理前導 0 的問題
        # Python eval 不允許 '01' 這種前導零，因此需要自訂求值或去除前導零。
        # 由於題目說可能有前導 0，我們自己寫一個簡單的求值器比較安全
        
        def calc(expr):
            # 用正則表達式切分出所有的數字與符號
            tokens = re.findall(r'[+-]?\d+', expr)
            return sum(int(t) for t in tokens)
            
        return calc(left) == calc(right)
    except:
        return False


def solve(equation: str) -> str:
    """
    尋找移動一根火柴棒後能讓等式成立的字串。
    """
    if not equation or '#' not in equation:
        return "No"
        
    # 擷取到 '#' 為止的字串
    eq = equation[:equation.index('#')]
    chars = list(eq)
    
    # 找出所有數字的索引位置
    digit_indices = [i for i, c in enumerate(chars) if c.isdigit()]
    
    # 情境 A: 內部移動一根火柴棒
    for idx in digit_indices:
        orig_char = chars[idx]
        if orig_char in INTERNAL_MOVES:
            for new_char in INTERNAL_MOVES[orig_char]:
                chars[idx] = new_char
                new_eq = "".join(chars)
                if evaluate_equation(new_eq):
                    return new_eq + '#'
            # 復原
            chars[idx] = orig_char

    # 情境 B: 跨數字移動一根火柴棒 (一個減少，另一個增加)
    for remove_idx in digit_indices:
        orig_remove_char = chars[remove_idx]
        if not REMOVE_STICK.get(orig_remove_char):
            continue
            
        for new_remove_char in REMOVE_STICK[orig_remove_char]:
            chars[remove_idx] = new_remove_char
            
            # 尋找可以增加一根火柴棒的數字
            for add_idx in digit_indices:
                if add_idx == remove_idx:
                    continue
                    
                orig_add_char = chars[add_idx]
                if not ADD_STICK.get(orig_add_char):
                    continue
                    
                for new_add_char in ADD_STICK[orig_add_char]:
                    chars[add_idx] = new_add_char
                    new_eq = "".join(chars)
                    if evaluate_equation(new_eq):
                        return new_eq + '#'
                        
                # 復原增加的字元
                chars[add_idx] = orig_add_char
                
            # 復原減少的字元
            chars[remove_idx] = orig_remove_char
            
    return "No"
