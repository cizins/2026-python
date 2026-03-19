# 測試案例 (Test Cases) - Week 03 作業

這份文件記錄了本週四道 UVA 題目的單元測試案例設計，包含正常情況與邊界情況。所有測試皆已透過 Python `unittest` 實作。

## 1. UVA 118 - Mutant Flatworld Explorers

### 1.1 範例測資 (Sample Input)
* **目的**：確認基本前進、轉向以及第一次掉落產生氣味 (scent) 的邏輯是否正確。
* **輸入**：
  ```
  5 3
  1 1 E
  RFRFRFRF
  3 2 N
  FRRFLLFFRRFLL
  0 3 W
  LLFFFLFLFL
  ```
* **預期輸出**：
  ```
  1 1 E
  3 3 N LOST
  2 3 S
  ```

### 1.2 邊界測資 (Edge Case) - 氣味保護機制
* **目的**：驗證當有多個機器人在同一個地點往下掉時，第一個掉落的機器人留下的氣味是否能成功保護後續的機器人免於掉落。
* **輸入**：
  ```
  2 2
  0 0 S
  F
  0 0 W
  F
  0 0 S
  F
  ```
* **預期輸出**：
  ```
  0 0 S LOST
  0 0 W
  0 0 S
  ```
  （第一個機器人往南掉落並留下氣味；第二個機器人往西掉落留下另一個氣味；第三個機器人再次往南掉，但因為有氣味保護，故忽略該指令並留在原地。）

---

## 2. UVA 272 - TEX Quotes

### 2.1 範例測資 (Sample Input)
* **目的**：測試多行文字、且含有多組成對引號時，是否能正確替換為 ` `` ` 與 ` '' `。
* **輸入**：
  ```
  "To be or not to be," quoth the Bard, "that
  is the question".
  ```
* **預期輸出**：
  ```
  ``To be or not to be,'' quoth the Bard, ``that
  is the question''.
  ```

### 2.2 邊界測資 (Edge Case) - 連續與空引號
* **目的**：測試單行中出現連續引號 `""` 或多層次引號的情境。
* **輸入**：
  ```
  He said "What?" and then "" followed by "Nothing".
  ```
* **預期輸出**：
  ```
  He said ``What?'' and then ````'' followed by ``Nothing''.
  ```

---

## 3. UVA 299 - Train Swapping

### 3.1 範例測資 (Sample Input)
* **目的**：測試泡沫排序/逆序數對計算的基本正確性。
* **輸入**：
  ```
  3
  3
  1 3 2
  4
  4 3 2 1
  2
  2 1
  ```
* **預期輸出**：
  ```
  Optimal train swapping takes 1 swaps.
  Optimal train swapping takes 6 swaps.
  Optimal train swapping takes 1 swaps.
  ```

### 3.2 邊界測資 (Edge Case) - 長度為 0 及 已排序好的狀況
* **目的**：確保當陣列為空，或是陣列完全不需要交換時，程式不會崩潰，且能正確輸出 0 次交換。
* **輸入**：
  ```
  3
  0
  
  5
  1 2 3 4 5
  3
  3 1 2
  ```
* **預期輸出**：
  ```
  Optimal train swapping takes 0 swaps.
  Optimal train swapping takes 0 swaps.
  Optimal train swapping takes 2 swaps.
  ```

---

## 4. UVA 490 - Rotating Sentences

### 4.1 範例測資 (Sample Input)
* **目的**：測試基本的 90 度旋轉，將橫向句子轉為垂直。
* **輸入**：
  ```
  Rene Dekart
  Blaise Pascal
  ```
* **預期輸出**：
  ```
  BR
  le
  an
  ie
  s 
  eD
   e
  Pk
  aa
  sr
  ct
  a 
  l 
  ```

### 4.2 邊界測資 (Edge Case) - 長短不一的句子
* **目的**：測試當句子長度落差極大時，程式是否能正確在不足的部分補上空白字元。
* **輸入**：
  ```
  123
  12345
  12
  ```
* **預期輸出**：
  ```
  111
  222
   33
   4 
   5 
  ```
  （注意最後兩行最左邊的空白是為了補齊 `12` 的不足長度。）