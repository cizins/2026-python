# Week 03 - Python 基礎解題 (UVA 118, 272, 299, 490)

本目錄包含 Week 03 的解題作業，主要涵蓋四道 UVA 經典題目的 Python 實作與單元測試。

## 包含的檔案
- `118.py` / `118-easy.py`：UVA 118 (Mutant Flathead Groteque) 機器人指令處理。
- `272.py` / `272-easy.py`：UVA 272 (TEX Quotes) 雙引號轉換。
- `299.py` / `299-easy.py`：UVA 299 (Train Swapping) 氣泡排序/逆序對計算。
- `490.py` / `490-easy.py`：UVA 490 (Rotating Sentences) 字串二維陣列旋轉。
- `tests/`：包含針對上述四道題目的所有 `unittest` 單元測試檔。
- `AI_USAGE.md`：AI 輔助開發紀錄。
- `TEST_CASES.md`：各題目的單元測試案例設計。
- `TEST_LOG.md`：各題目的測試執行日誌。

## 執行測試
請於目錄下執行以下指令以執行所有單元測試：
```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```

## 解題特色
* 提供 `標準版`：包含型別提示 (Type Hints)、完整的模組化設計。
* 提供 `-easy版`：簡化了繁雜的狀態邏輯，保留最精華的解題思路，便於上機考試背誦及快速實作。
