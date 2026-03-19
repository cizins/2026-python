# 測試案例 (Test Cases) - Week 03 作業

這份文件記錄了本週四道 UVA 題目的單元測試案例設計，包含正常情況與邊界情況。所有測試皆已透過 Python `unittest` 實作。

## 1. UVA 118 - Mutant Flatworld Explorers (`test_118.py`)

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

### 1.2 邊界測資 (Edge Case) - 空白輸入
* **目的**：驗證當傳入空字串時，程式不會崩潰，且能回傳空字串。
* **輸入**：`""`
* **預期輸出**：`""`

---

## 2. UVA 272 - TEX Quotes (`test_272.py`)

### 2.1 範例測資 (Sample Input)
* **目的**：測試多行文字、且含有多組成對引號時，是否能正確替換為 ` `` ` 與 ` '' `。
* **輸入**：題目提供的範例測資 (多行字串)
* **預期輸出**：所有的首引號轉為 ` `` `，尾引號轉為 ` '' `。

### 2.2 邊界測資 (Edge Case)
* **沒有雙引號的文字**：測試 `Hello, world! This is a simple test without any quotes.`，預期輸出與輸入一模一樣。
* **多層嵌套與連續引號**：測試 `"""Hello"""`，預期輸出為 ```''``Hello''``''`，驗證狀態機切換邏輯。
* **空輸入**：輸入為空字串，預期輸出為空。

---

## 3. UVA 299 - Train Swapping (`test_299.py`)

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

### 3.2 邊界測資 (Edge Case) 
* **長度為 0 (沒有車廂)**：輸入 `1\n0\n`，預期不需要交換，輸出為 `0 swaps`。
* **已經排好序的情況**：輸入 `1\n5\n1 2 3 4 5\n`，預期不需要交換，輸出為 `0 swaps`。

---

## 4. UVA 490 - Rotating Sentences (`test_490.py`)

### 4.1 範例測資 (Sample Input)
* **目的**：測試基本的 90 度旋轉，將橫向句子轉為垂直。
* **輸入**：
  ```
  Rene Decartes once said,
  "I think, therefore I am."
  ```
* **預期輸出**：旋轉 90 度的結果。

### 4.2 邊界測資 (Edge Case) - 長短不一的句子
* **目的**：測試當中間的句子特別短時，程式是否能正確在不足的部分補上空白字元。
* **輸入**：
  ```
  abc
  d
  efgh
  ```
* **預期輸出**：
  ```
  eda
  f b
  g c
  h  
  ```
  （驗證空白補齊功能正常運作）
