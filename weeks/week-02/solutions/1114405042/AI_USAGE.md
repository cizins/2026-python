# AI 輔助使用紀錄 - Week 02 TDD 作業

本文件記錄了在測試驅動開發 (TDD) 過程中，如何使用 AI 輔助，重點在於透明度與學習成果。

---

## 向 AI 提出的問題

### 主題 1: Python 中的多鍵值排序 (Multi-Key Sorting)

**問題 1.1**: "如何在 Python 中使用 `sorted()` 函式，根據多個條件對學生進行排序？"

**AI 建議**:
> 使用 `sorted()` 搭配 lambda 函式，回傳一個包含排序鍵值的 Tuple。Tuple 內的元素會逐一進行比較。
```python
sorted(students, key=lambda x: (score, age, name))
```

**我的評估**: ✓ **採用 (ADOPTED)**
- 驗證了這對於升序排列有效。
- 對於降序的分數：使用負號：`key=lambda x: (-score, age, name)`。
- 在 Task 2 的同分打破僵局情境下進行了測試。
- 使用這個方法，12 個測試全數通過。

**為何信任此建議**: Lambda tuple 排序是標準的 Python 寫法，在官方文件中也有詳細記載。

---

**問題 1.2**: "Python 的 `sorted()` 函式是穩定的 (stable) 嗎？這對我的排名演算法有何意義？"

**AI 建議**:
> 是的，Python 的 `sorted()` 使用 Timsort，這是一種穩定的排序演算法。這意味著相等的元素會保持它們在原始列表中的相對順序。

**我的評估**: ✓ **採用並驗證 (ADOPTED & VERIFIED)**
- 透過測試確認：`test_identical_students_multiple` 成功通過了字母順序的測試。
- 穩定性對 Task 3 (動作頻率計數) 非常重要。
- 未觀察到退化 (regressions)。

**影響**: 穩定的排序讓我可以放心地串聯多個操作。

---

### 主題 2: 基於 Set 的去重 (Deduplication)

**問題 2.1**: "如何從列表中移除重複項，同時保留原始順序？"

**AI 建議** (多種方法):

**選項 A**: 基於 Set (推薦)
```python
seen = set()
result = []
for item in items:
    if item not in seen:
        seen.add(item)
        result.append(item)
```

**選項 B**: Dict.fromkeys()
```python
list(dict.fromkeys(items))
```

**選項 C**: 使用列表尋找的自訂去重 (效率低)
```python
result = [x for i, x in enumerate(items) if x not in items[:i]]
```

**我的評估**: ✓ **採用選項 A，拒絕選項 B & C**

**理由**:
- **選項 A (採納)**: O(n) 時間複雜度，明確表達了使用 set 進行追蹤，具備教育意義。
- **選項 B (拒絕)**: 雖然可行，但保留順序的原因不夠直覺，較不明確。
- **選項 C (拒絕)**: O(n²) 時間複雜度，對於較大的列表不可接受。

**驗證**: Task 1 的 `test_dedup_preserves_order` 測試通過，確認了順序被保留。

**主要學習**: 當存在多種解決方案時，選擇對未來閱讀者來說既高效又清晰的那一個。

---

**問題 2.2**: "負數適用於基於 set 的去重嗎？"

**AI 回覆**: 
> 是的，Python 中的 set 可以包含任何可雜湊 (hashable) 的型別，包含負整數。`in` 運算子對負數的作用完全相同。

**我的評估**: ✓ **透過測試驗證 (VERIFIED THROUGH TESTING)**
- 測試案例 `test_negative_evens` 確認了：`-4, -2` 被正確地追蹤。
- 不需要特殊處理。

---

### 主題 3: 使用 Collections 進行事件計數

**問題 3.1**: "我應該使用 `defaultdict`, `Counter`, 還是普通的 `dict` 來計算事件？"

**AI 比較**:
| 方法 | 概念 | 最適用於 |
|----------|---------|----------|
| `defaultdict(int)` | 預設值工廠 | 簡單的計數，隱式初始化為 0 |
| `Counter` | 特化的 dict 子類別 | 頻率計數 + `most_common()` |
| `dict` 搭配 `.get()` | 手動處理預設值 | 細粒度控制 |

**我的評估**: ✓ **採用混合方法 (ADOPTED Hybrid Approach)**
- 使用 `defaultdict(int)` 計算使用者事件 (Task 3)。
- 使用 `Counter` 計算動作頻率 (Task 3)。
- 讓每個工具發揮其專長。

**驗證**: Task 3 的測試在此混合方法下全數通過。

**理由**:
```python
user_counts = defaultdict(int)  # 簡單、乾淨地進行基本計數
action_counts = Counter()        # 具備內建的 most_common() 方法
```

---

**問題 3.2**: "使用 `defaultdict` 時，如何找到出現頻率最高的元素？"

**AI 建議**:
> 如果使用 `defaultdict`，你需要手動尋找最大值：
```python
max(counter.items(), key=lambda x: x[1])
```
> 但如果切換到 `Counter`，請使用 `Counter.most_common(1)[0]`。

**我的評估**: ✓ **採用 (ADOPTED)**
- 特別使用 `Counter` 來利用 `most_common()` 方法。
- 程式碼比手動尋找最大值更乾淨。
- 測試 `test_top_action_most_frequent` 確認了正確性。

---

### 主題 4: 邊界情況處理 (Edge Case Handling)

**問題 4.1**: "我應該如何在函式中處理空的輸入列表？"

**AI 建議**:
- 回傳空列表 (針對序列)
- 回傳空的 dict/counter (針對聚合)
- 特殊情況輸出 (針對摘要)

**我的評估**: ✓ **部分採用 (PARTIALLY ADOPTED)**

**實作**:
- Task 1: `deduplicate_sequence([])` 回傳 `[]` ✓
- Task 2: 不適用 (k 必須 ≥1)
- Task 3: 回傳 "top_action: 0\n" 作為優雅降級 (graceful degradation)

**測試覆蓋率**: `test_empty_list`, `test_empty_logs` 均通過。

---

**問題 4.2**: "在 Python 中，零 (0) 算作偶數嗎？"

**AI 回覆**:
> 是的，`0 % 2 == 0`，所以根據數學定義，零是偶數。

**我的評估**: ✓ **驗證並實作 (VERIFIED & IMPLEMENTED)**
- 新增了測試案例 `test_zero_in_list`。
- 確認：`extract_evens([0, 1, 2, 3])` 回傳 `[0, 2]`。
- 實作正確地處理了零。

---

### 主題 5: 程式碼重構最佳實踐

**問題 5.1**: "我應該如何抽出輔助函式而不改變測試結果？"

**AI 建議**:
1. 保持主函式的簽名 (signatures) 不變。
2. 抽出新的 `_private_functions` (帶有前導底線)。
3. 在每次抽出後執行測試，確認沒有發生退化。
4. 專注於減少重複，而不是增加程式碼。

**我的評估**: ✓ **採用並驗證 (ADOPTED & VERIFIED)**

**應用於**:
- Task 1: 抽出 `_is_even()` 輔助函式
  - 減少了 `extract_evens()` 與附近邏輯中的重複程式碼。
  - 重構後 14 個測試依然通過。

- Task 2: 抽出 `_parse_input()` 與 `_sort_by_ranking()`
  - 關注點分離：解析、排序、格式化。
  - 重構後 12 個測試依然通過。

- Task 3: 抽出 4 個輔助函式：`_parse_logs()`, `_count_user_events()`, `_count_actions()`, `_sort_users_by_count()`
  - 每個函式都具有單一職責。
  - 重構後 12 個測試依然通過。

**主要學習**: 在測試通過的安全網下進行重構，是強大的 TDD 實踐。

---

**問題 5.2**: "在測試通過後加上 docstrings 和型別提示 (type hints) 可以嗎？"

**AI 回覆**:
> 是的，文件化是重構的一種形式。它不會改變行為，只會提高清晰度。請在重構 (REFACTOR) 階段加入。

**我的評估**: ✓ **採用 (ADOPTED)**
- 擴充了所有 docstrings，包含 Args, Returns, Examples。
- 在相關處加上了複雜度註解。
- 文件變更沒有導致任何測試失敗。

---

## 我拒絕的 AI 建議與原因

### 拒絕 1: 使用 `list.sort()` 代替 `sorted()`

**AI 建議**: "你也可以使用 `list.sort()` 進行就地排序 (in-place sorting)，這稍微高效一點。"

**我的回應**: ✗ **拒絕 (REJECTED)**
- 原因：不需要就地排序；`sorted()` 回傳新列表，對於函數式風格更清晰。
- Task 2 需要不會修改輸入的排序。
- `sorted()` 允許串聯，更適合可讀的一行程式碼 (one-liners)。
- 偏好不可變性 (Immutability) 原則。

---

### 拒絕 2: 使用 `@dataclass` 建立學生紀錄

**AI 建議**: "考慮使用 `@dataclass` 或具名元組 (named tuples) 來建構學生紀錄，而不是普通的 tuples。"

**我的回應**: ✗ **拒絕 (REJECTED)**
- 原因：對於這個問題的範圍來說過度設計 (Over-engineering)。
- 使用索引存取的 tuples `[0]=name, [1]=score, [2]=age` 就足夠了。
- Dataclass 會增加複雜度，且對測試沒有幫助。
- Tuple 方法自然地契合了問題的輸入格式。

---

### 拒絕 3: 使用 `functools.reduce()` 進行計數

**AI 建議**: "你可以使用 `functools.reduce()` 以函數式風格來聚合日誌。"

**我的回應**: ✗ **拒絕 (REJECTED)**
- 原因：for 迴圈方法比 reduce 更具可讀性。
- Reduce 會掩蓋簡單的計數邏輯。
- 團隊的可維護性大於聰明的函數式編程。
- 測試並不要求函數式方法。

---

### 拒絕 4: 使用 NumPy 優化 Task 1

**AI 建議**: "對於大型資料集，考慮使用 NumPy 陣列以獲得更快的效能。"

**我的回應**: ✗ **拒絕 (REJECTED)**
- 原因：作業規範禁止使用外部套件。
- NumPy 不被允許 (只能使用 Python 內建)。
- 純 Python 方法已經足夠滿足需求。
- 測試案例並未顯示有效能瓶頸。

---

## 需要我自行驗證 AI 指導的案例

### 案例 1: 負數的取餘數行為

**AI 聲稱**: "Python 的取餘數對正負數的運作方式相同：`-4 % 2 == 0`"

**我的驗證**:
```python
# 在 Python 中測試：
print(-4 % 2)    # 預期：0 (偶數)
print(-3 % 2)    # 預期：1 (奇數)
print(-2 % 2)    # 預期：0 (偶數)
```

**結果**: ✓ 已確認 (CONFIRMED)
- AI 對於 Python 的地板除法行為是正確的。
- 加入了測試 `test_negative_evens` 來記錄這點。

**學習**: 數學行為在不同語言的版本/實作上可能會有所不同；永遠要測試關鍵假設。

---

### 案例 2: 包含相同 Tuples 的穩定排序

**AI 聲稱**: "穩定的排序會維持相等元素的原始順序。"

**我的驗證**:
```python
# Task 2: 多個具有相同 (分數, 年齡) 的學生
# 輸入: [(alice 88 20), (bob 88 20), (charlie 88 20)]
# 預期輸出維持插入順序
```

**結果**: ✓ 已確認 (CONFIRMED)
- 測試 `test_identical_students_multiple` 驗證了這點。
- 字母排序正確地實作了次要層級。

**學習**: 用實際的測試案例來測試你對語言行為的假設。

---

### 案例 3: Counter.most_common() 在平手時的行為

**AI 聲稱**: "當存在平手時，Counter.most_common() 會以任意順序回傳元素。"

**我的測試**:
```python
# 當多個動作有相同計數時：
action_counts = Counter({'login': 2, 'view': 2, 'delete': 2})
top = action_counts.most_common(1)  # 會是哪一個？
```

**結果**: 透過測試 `test_all_same_action` 驗證
- Counter 會回傳其中之一（這對本作業來說沒差）。
- 測試不要求平手時要有特定的動作。
- 在測試註解中記錄了這個行為。

---

## AI 輔助影響總結

### 有用的貢獻
- 使用 lambda tuples 解釋多鍵值排序。
- Collections 模組指南 (defaultdict vs Counter)。
- 具備測試安全性的重構最佳實踐。
- 邊界情況思考 (空輸入、零、負數)。

### 需要自我驗證的關鍵領域
- Python 中的負數數學。
- 遇到平手時的穩定排序行為。
- 相同頻率下的 Counter 行為。
- 邊界情況的行為假設。

### 整體評估
- **AI 有效性**: 85% - 大多數建議是可靠的；對關鍵假設需要進行驗證。
- **獲得的學習**: 90% - 驗證的過程比 AI 的建議本身教會了我更多。
- **程式碼品質**: 所有被採用的建議都在不妥協正確性的前提下提高了清晰度。

---

## 關鍵教訓：AI 作為思考夥伴，而非權威

本作業強化了一個重要原則：
> 將 AI 作為思考夥伴來探索選項時最為有效，而不是把它當作最終答案的權威。永遠要：
1. 理解 AI 建議背後的原因 (`why`)。
2. 用程式碼測試關鍵假設。
3. 透過實際執行來驗證邊界情況。
4. 信任測試多於解釋。

---

## 未來使用 AI 的建議

1. **對於演算法設計**: 接受建議，但用小型測試案例進行驗證。
2. **對於語法問題**: 信任度較高 (例如 lambda 排序)，但仍需驗證一次。
3. **對於邊界情況**: 與 AI 討論，然後實作防禦性測試。
4. **對於重構**: 使用 AI 提供建議，但要求所有測試依然必須通過。
5. **對於文件化**: AI 可以提升清晰度；需要審查準確性。

---

## 最終反思

TDD 流程讓 AI 的使用變得透明且可咎責 (accountable)：
- 測試作為評估 AI 建議的規格。
- 如果接受 AI 建議後測試通過，那它很可能是正確的。
- 如果測試失敗，必須拒絕或修改建議。
- 這建立了一個客觀的回饋迴圈。

這與不經測試就接受 AI 程式碼有根本上的不同——在這裡，測試才是真相的來源。