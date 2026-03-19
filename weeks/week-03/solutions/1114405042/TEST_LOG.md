# 測試日誌 (TEST_LOG) - Week 03 作業

## 執行紀錄：UVA 118
- 執行指令：`python3 test_118.py -v`
- 執行結果：
  ```
  test_easy_solution (__main__.TestUVA118) ... ok
  test_empty_input (__main__.TestUVA118) ... ok
  test_standard_solution (__main__.TestUVA118) ... ok
  ----------------------------------------------------------------------
  Ran 3 tests in 0.000s
  OK
  ```
- 結論：標準版與簡單版 (`-easy`) 皆正確處理機器人轉向、移動與氣味 (Scent) 掉落機制。

---

## 執行紀錄：UVA 272
- 執行指令：`python3 test_272.py -v`
- 執行結果：
  ```
  test_easy_solution (__main__.TestUVA272) ... ok
  test_empty_input (__main__.TestUVA272) ... ok
  test_multiple_nested_quotes (__main__.TestUVA272) ... ok
  test_no_quotes (__main__.TestUVA272) ... ok
  test_standard_solution (__main__.TestUVA272) ... ok
  ----------------------------------------------------------------------
  Ran 5 tests in 0.000s
  OK
  ```
- 結論：文字與雙引號替換成功，交替使用 ` `` ` 與 ` '' ` 邏輯完美通過，邊界條件（沒有引號或多重引號）也順利通過。

---

## 執行紀錄：UVA 299
- 執行指令：`python3 test_299.py -v`
- 執行結果：
  ```
  test_already_sorted (__main__.TestUVA299) ... ok
  test_easy_solution (__main__.TestUVA299) ... ok
  test_empty_input (__main__.TestUVA299) ... ok
  test_standard_solution (__main__.TestUVA299) ... ok
  test_zero_trains (__main__.TestUVA299) ... ok
  ----------------------------------------------------------------------
  Ran 5 tests in 0.000s
  OK
  ```
- 結論：利用計算「逆序對 (Inversions)」的方法成功取得最佳交換次數，0 個車廂或已排好序的極端測資皆輸出 0 swaps，符合預期。

---

## 執行紀錄：UVA 490
- 執行指令：`python3 test_490.py -v`
- 執行結果：
  ```
  test_different_lengths_with_middle_short (__main__.TestUVA490) ... ok
  test_easy_solution (__main__.TestUVA490) ... ok
  test_empty_input (__main__.TestUVA490) ... ok
  test_standard_solution (__main__.TestUVA490) ... ok
  ----------------------------------------------------------------------
  Ran 4 tests in 0.000s
  OK
  ```
- 結論：無論句子長短，皆能以順時針 90 度旋轉並正確補上空白字元。

---

## 執行紀錄：UVA 100
- 執行指令：`python3 -m unittest discover -s tests -p "test_100.py" -v`
- 執行結果：
  ```
  test_easy_solution (test_100.TestUVA100) ... ok
  test_empty_input (test_100.TestUVA100) ... ok
  test_reversed_order (test_100.TestUVA100) ... ok
  test_standard_solution (test_100.TestUVA100) ... ok
  ----------------------------------------------------------------------
  Ran 4 tests in 0.001s
  OK
  ```
- 結論：加入全域字典做 memoization 成功加快遞迴速度，對於輸入為 `i > j` 的情況也能安全轉換並以原順序輸出答案。
