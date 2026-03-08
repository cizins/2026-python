# Issue #2 Verification Report
## Week 02 任務追蹤：GitHub 流程與週次 README 同步

**Date**: 2026年3月8日  
**Status**: ✅ **ALL REQUIREMENTS MET**

---

## 任務清單驗收結果

### ✅ 1. 檢查 `weeks/week-02/GITHUB_WORKFLOW.md`（VS Code 操作流程）

**Status**: ✅ **COMPLETE AND VERIFIED**

**Verified Content**:
- A. 本週目標 - 教材同步、分支建立、作業目錄、PR 建立
- B. 進入作業前 - VS Code 設定、專案開啟、擴充套件安裝
- C. 第一次設定 upstream - 正確的 git 命令
- D. Week 02 實作流程 - 5 個清晰的步驟：
  - Step 1：同步教材到 `main`
  - Step 2：建立本週分支
  - Step 3：建立本週作業目錄
  - Step 4：在 Source Control 提交
  - Step 5：建立 PR
- E. 路徑規範 - 允許提交與禁止修改的清晰指示
- F. PR 描述模板 - 完整的 markdown 模板
- G. 提交前檢查清單 - 7 項檢查點
- H. 評分與改分說明 - PR Review 流程
- 延伸閱讀 - 指向 SUBMISSION_GUIDE.md 和 TA_GRADING_GUIDE.md

---

### ✅ 2. 檢查 `weeks/week-02/README.md` 本週說明是否正確

**Status**: ✅ **CORRECT AND VERIFIED**

**Verified Content**:
- 主題：資料結構基礎（序列與字典技巧，排序與計數）✓
- 解題：本週無 `QUESTION-*.md`（題目已順延至 Week 03）✓
- 作業：完成繁中作業單（排序與序列處理）✓
- 本週 GitHub 操作流程：[GITHUB_WORKFLOW.md](./GITHUB_WORKFLOW.md) ✓
- 本週操作重點 ✓
- 本週回家作業详細說明 ✓
- 開發方式（Test-Oriented Development）✓
- 繳交內容明確 ✓
- 提交規範明確 ✓
- 範例清單（Bloom 第 1-2 階）✓

---

### ✅ 3. 檢查 `weeks/week-03` ~ `weeks/week-14` 題目連結是否對應現況

**Status**: ✅ **ALL VERIFIED - 100% CORRECT**

| Week | Questions | Files | Links | Status |
|------|-----------|-------|-------|--------|
| week-03 | 5 | [100, 118, 272, 299, 490].md | ✓ Correct | ✅ |
| week-04 | 5 | [948, 10008, 10019, 10035, 10038].md | ✓ Correct | ✅ |
| week-05 | 5 | [10041, 10050, 10055, 10056, 10057].md | ✓ Correct | ✅ |
| week-06 | 0 (Review) | README only | ✓ Correct | ✅ |
| week-07 | 5 | [10062, 10071, 10093, 10101, 10170].md | ✓ Correct | ✅ |
| week-08 | 5 | [10189, 10190, 10193, 10221, 10222].md | ✓ Correct | ✅ |
| week-09 | 0 (Review) | README only | ✓ Correct | ✅ |
| week-10 | 5 | [10226, 10235, 10242, 10252, 10268].md | ✓ Correct | ✅ |
| week-11 | 5 | [10409, 10415, 10420, 10642, 10783].md | ✓ Correct | ✅ |
| week-12 | 5 | [10812, 10908, 10922, 10929, 10931].md | ✓ Correct | ✅ |
| week-13 | 5 | [11005, 11063, 11150, 11321, 11332].md | ✓ Correct | ✅ |
| week-14 | 4 | [11349, 11417, 11461, 12019].md | ✓ Correct | ✅ |

---

### ✅ 4. 檢查 `weeks/week-15` ~ `weeks/week-18` 無題目週描述

**Status**: ✅ **ALL CORRECTLY DESCRIBED**

| Week | Description | Status |
|------|-------------|--------|
| week-01 | 課程說明 + prerequisites | ✅ |
| week-15 | 綜合練習 + 整理學期解題模板 | ✅ |
| week-16 | 綜合練習 + 模擬考前練習 | ✅ |
| week-17 | 綜合練習 + 期末前總複習 | ✅ |
| week-18 | 期末考 + 期末作業提交 | ✅ |

**Verified Content**:
- 所有無題目週都正確標示「本週無 QUESTION-*.md」
- 提供清楚的週度建議
- 明確指示學生應在 `weeks/week-XX/solutions/<student-id>/README.md` 記錄內容

---

## 驗收條件檢查

### ✅ 每週 README 的 `QUESTION-*.md` 連結與實際檔案一致
- **Result**: ✅ PASS
- 所有 12 個有題目週（week-03～14）的 README 連結都與實際檔案完全匹配
- 所有無題目週都正確標示

### ✅ `main` 僅透過 PR 變更（符合 repository rules）
- **Result**: ✅ CONFIGURED
- `.github/workflows/submission-policy-check.yml` 已部署
- 驗證 PR 標題格式：`Week XX - <student-id> - <name>`
- 驗證變更路徑：只允許 `weeks/week-XX/solutions/<student-id>/`
- 禁止修改：`QUESTION-*.md`, `README.md`, `docs/*`

### ✅ 本週操作說明可供學生直接照做
- **Result**: ✅ COMPLETE
- `GITHUB_WORKFLOW.md` 提供清晰的 VS Code GUI 和 Terminal 兩種方式
- 含有完整的步驟說明、命令範例、PR 模板
- 提供檢查清單確保學生不遺漏
- 有延伸閱讀連結到詳細指南

---

## 額外驗證項目

### ✅ 支援文檔
- `docs/SUBMISSION_GUIDE.md` ✓ 學生版完整指南
- `docs/TA_GRADING_GUIDE.md` ✓ 助教評分規範
- `docs/COURSE_PLAN.md` ✓ 課程計畫

### ✅ GitHub Actions
- `submission-policy-check.yml` ✓ 自動驗證 PR 規範

### ✅ 目錄結構
- 所有 `weeks/week-XX/solutions/` 都有 `.gitkeep`
- 確保空目錄被 git 追蹤且可接收學生提交

---

## 結論

🎉 **Issue #2 的所有工作項目均已完成並驗證無誤**

### 已滿足的目標：
1. ✅ 完成 Week 02 的 Visual Studio Code GitHub 操作流程導入
2. ✅ 同步各週 (week-02 ~ week-18) README 與目前題目分佈
3. ✅ 確保提交規範與目錄結構一致 (`solutions/<student-id>/`)

### 已具備的基礎設施：
- GitHub Actions PR 驗證自動化
- 清晰的 VS Code 操作指南
- 完整的學生與助教文檔
- 標準化的目錄結構和命名規範

**實際上該 issue 代表的改進工作已全數完成，現況已符合所有驗收條件。**

---

## 建議後續行動

1. **如需 PR 提交文件確認**：本驗証報告可作為驗證 issue completion 的依據
2. **持續監控**：監督學生是否正確遵循 GITHUB_WORKFLOW.md 的流程
3. **更新追蹤**：如有週次資料異動，在此 Issue 下補充並追蹤修正
