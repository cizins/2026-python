# 這是更簡單、更容易記憶的寫法 (Easy version)
#
# 解題思路：
# 1. 建立一個對應表 (Dictionary)，將數字間所有「合法轉換」寫好。
#    - `move_inside`: 單純內部火柴棒移動 (0<->6, 0<->9, 2<->3, 5<->3)
#    - `lose_one`: 數字少了一根火柴棒會變成什麼 (例如 8->0, 8->6, 8->9)
#    - `gain_one`: 數字多了一根火柴棒會變成什麼 (剛好是 `lose_one` 的反向)
# 2. 字串可能很長，但我們可以透過取代特定位置的字元來嘗試：
#    - 首先嘗試自己「內部轉變」，看等式成不成立。
#    - 如果不成立，嘗試「某個位置變少一根」，同時「另一個位置變多一根」。
# 3. 判斷等式是否成立，可以簡單用 `replace('=', '==')`，但因為可能有前導 0 (如 '01+02==03')，
#    Python 內建的 `eval()` 會報錯，所以寫一個簡短的 `check` 函式處理，把數字轉成 `int` 就好了。

# 紀錄變化對應表
# 內部交換一根
MOVE_INSIDE = {
    '0': ['6', '9'], '6': ['0', '9'], '9': ['0', '6'],
    '2': ['3'], '3': ['2', '5'], '5': ['3']
}
# 少一根火柴棒
LOSE_ONE = {
    '7': ['1'], '8': ['0', '6', '9'], '9': ['3', '5'], '6': ['5']
}
# 多一根火柴棒 (反轉 LOSE_ONE 的關係)
GAIN_ONE = {
    '1': ['7'], '0': ['8'], '6': ['8'], '9': ['8'], '3': ['9'], '5': ['6', '9']
}


def check(eq_str: str) -> bool:
    """簡便判斷等式是否成立的方法 (支援前導零)"""
    try:
        # 分割左右兩邊
        left_str, right_str = eq_str.split('=')
        
        # 定義小工具，用來解析像是 "01+02-03" 這樣的字串並求和
        # 我們直接在數字前面補 0 以防空字串，然後將加減號作為正負號
        import re
        def calc(s):
            # 找到所有的數值 (含前面的正負號)
            numbers = re.findall(r'[+-]?\d+', s)
            return sum(int(n) for n in numbers)
            
        return calc(left_str) == calc(right_str)
    except:
        return False


def solve_easy(equation: str) -> str:
    """
    計算移動一根火柴棒是否能讓等式成立。
    """
    if '#' not in equation:
        return "No"
        
    eq = equation.replace('#', '')
    chars = list(eq)
    n = len(chars)
    
    # 1. 嘗試「自己內部交換一根火柴棒」
    for i in range(n):
        c = chars[i]
        if c in MOVE_INSIDE:
            for new_c in MOVE_INSIDE[c]:
                chars[i] = new_c
                new_eq = "".join(chars)
                if check(new_eq):
                    return new_eq + '#'
                chars[i] = c  # 記得復原
                
    # 2. 嘗試「一個數字少一根，另一個數字多一根」
    for i in range(n):
        c1 = chars[i]
        if c1 in LOSE_ONE:
            for new_c1 in LOSE_ONE[c1]:
                chars[i] = new_c1  # 讓位置 i 少一根火柴棒
                
                # 尋找另一個位置 j 來接收這根火柴棒
                for j in range(n):
                    if i == j: continue
                    c2 = chars[j]
                    if c2 in GAIN_ONE:
                        for new_c2 in GAIN_ONE[c2]:
                            chars[j] = new_c2  # 讓位置 j 多一根火柴棒
                            new_eq = "".join(chars)
                            if check(new_eq):
                                return new_eq + '#'
                            chars[j] = c2  # 復原位置 j
                            
                chars[i] = c1  # 復原位置 i
                
    return "No"
