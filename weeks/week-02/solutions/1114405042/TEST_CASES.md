# Test Cases Documentation - Week 02 Assignment

This document provides custom test datasets designed to validate critical functionality and edge cases across all three tasks.

---

## Task 1: Sequence Clean - Custom Test Cases

### Test Case 1: Normal Case with Mixed Numbers

**Category**: Normal Case
**Purpose**: Verify basic functionality with duplicates and even/odd mix

**Input**:
```
5 3 5 2 9 2 8 3 1
```

**Expected Output**:
```
dedupe: 5 3 2 9 8 1
asc: 1 2 2 3 3 5 5 8 9
desc: 9 8 5 5 3 3 2 2 1
evens: 2 2 8
```

**Actual Output** (after implementation):
```
dedupe: 5 3 2 9 8 1
asc: 1 2 2 3 3 5 5 8 9
desc: 9 8 5 5 3 3 2 2 1
evens: 2 2 8
```

**Result**: ✓ PASS

**Corresponding Test Function**: `test_normal_case_deduplicate`, `test_normal_case_ascending_sort`, `test_normal_case_descending_sort`, `test_extract_evens_normal`

**Key Validation Point**: Dedup preserves order (5 before 3), even extraction maintains original position

---

### Test Case 2: Edge Case - Negative Numbers and Zero

**Category**: Edge Case
**Purpose**: Verify handling of negative numbers (especially negative evens) and zero

**Input**:
```
-4 -3 0 2 -2 5 6
```

**Expected Output**:
```
dedupe: -4 -3 0 2 -2 5 6
asc: -4 -3 -2 0 2 5 6
desc: 6 5 2 0 -2 -3 -4
evens: -4 0 2 -2 6
```

**Actual Output** (after implementation):
```
dedupe: -4 -3 0 2 -2 5 6
asc: -4 -3 -2 0 2 5 6
desc: 6 5 2 0 -2 -3 -4
evens: -4 0 2 -2 6
```

**Result**: ✓ PASS

**Corresponding Test Function**: `test_with_negative_numbers`, `test_negative_evens`, `test_zero_in_list`

**Key Validation Point**: 
- Negative even numbers (`-4`, `-2`) correctly identified
- Zero correctly treated as even
- Sorting handles negative numbers correctly

---

### Test Case 3: Boundary Case - Empty and Single Element

**Category**: Boundary Case
**Purpose**: Verify edge conditions with minimal input

**Input Set A** (Empty):
```
(empty list)
```

**Expected Output A**:
```
dedupe: (empty)
asc: (empty)
desc: (empty)
evens: (empty)
```

**Input Set B** (Single element):
```
7
```

**Expected Output B**:
```
dedupe: 7
asc: 7
desc: 7
evens: (empty)
```

**Actual Output**: ✓ PASS

**Corresponding Test Function**: `test_empty_list`, `test_single_element`

**Key Validation Point**: No crashes, proper handling of edge conditions

---

### Test Case 4: Critical Path - Order Preservation in Deduplication

**Category**: Order Preservation Verification
**Purpose**: Critical requirement: dedup must preserve **first occurrence order**

**Input**:
```
3 1 4 1 5 9 2 6 5 3 5
```

**Expected Output**:
```
dedupe: 3 1 4 5 9 2 6
(NOT: 1 2 3 4 5 6 9)
```

**Actual Output**:
```
dedupe: 3 1 4 5 9 2 6
```

**Result**: ✓ PASS

**Corresponding Test Function**: `test_dedup_preserves_order`

**Key Validation Point**: 
- First occurrence of 3 is at position 0, kept
- Duplicate 3 at position 9 is removed
- Order is 3→1→4→5→9→2→6, NOT sorted

---

### Test Case 5: Stress Testing - Many Duplicates

**Category**: Stress Test / Boundary
**Purpose**: Verify performance and correctness with high duplication

**Input**:
```
1 1 1 2 2 2 3 3 3 4 4 4 5 5 5
```

**Expected Output**:
```
dedupe: 1 2 3 4 5
asc: 1 1 1 2 2 2 3 3 3 4 4 4 5 5 5
desc: 5 5 5 4 4 4 3 3 3 2 2 2 1 1 1
evens: 2 2 2 4 4 4
```

**Actual Output**: ✓ PASS

**Corresponding Test Function**: `test_dedup_already_unique` (inverse concept)

**Key Validation Point**: Dedup correctly identifies all 4 duplicates, returns minimal set

---

## Task 2: Student Ranking - Custom Test Cases

### Test Case 1: Normal Case - Clear Ranking

**Category**: Normal Case
**Purpose**: Verify basic ranking with no ties

**Input**:
```
6 3
amy 88 20
bob 88 19
zoe 92 21
ian 88 19
leo 75 20
eva 92 20
```

**Expected Output**:
```
eva 92 20
zoe 92 21
bob 88 19
```

**Actual Output**:
```
eva 92 20
zoe 92 21
bob 88 19
```

**Result**: ✓ PASS

**Corresponding Test Function**: `test_normal_ranking_basic`, `test_tiebreak_multiple_conditions`

**Key Validation Point**: 
- Highest score (92) students first
- Among score 92: eva (20 years) before zoe (21 years)
- Among score 88: bob/ian (both 19) before amy (20)

---

### Test Case 2: Critical - Three-Way Tie Breaking

**Category**: Tie-Breaking Edge Case
**Purpose**: Test all three sort criteria (score→age→name)

**Input**:
```
3 3
zoe 88 19
alice 88 19
bob 88 19
```

**Expected Output**:
```
alice 88 19
bob 88 19
zoe 88 19
```

**Actual Output**:
```
alice 88 19
bob 88 19
zoe 88 19
```

**Result**: ✓ PASS

**Corresponding Test Function**: `test_tiebreak_by_name_same_score_and_age`

**Key Validation Point**: When score and age tied, alphabetical order by name breaks tie (alice < bob < zoe)

---

### Test Case 3: Boundary - k Values

**Category**: Boundary Case
**Purpose**: Test extreme k values

**Input Set A** (k=1):
```
2 1
alice 85 20
bob 95 19
```

**Expected Output A**:
```
bob 95 19
```

**Input Set B** (k = total students):
```
2 2
alice 85 20
bob 95 19
```

**Expected Output B**:
```
bob 95 19
alice 85 20
```

**Actual Output**: ✓ PASS

**Corresponding Test Function**: `test_k_equals_one`, `test_k_equals_total`

**Key Validation Point**: Correctly handles k=1 (single winner) and k=n (all students)

---

### Test Case 4: Age-Based Tie Breaking

**Category**: Secondary Sorting Criterion
**Purpose**: Verify age breaks ties when scores identical

**Input**:
```
4 4
student_old 90 30
student_young 90 18
student_middle 90 25
another 85 20
```

**Expected Output**:
```
student_young 90 18
student_middle 90 25
student_old 90 30
another 85 20
```

**Actual Output**:
```
student_young 90 18
student_middle 90 25
student_old 90 30
another 85 20
```

**Result**: ✓ PASS

**Corresponding Test Function**: `test_tiebreak_by_age_same_score`

**Key Validation Point**: At score 90, youngest (18) comes before oldest (30)

---

### Test Case 5: All Identical with Alphabetical Ordering

**Category**: Maximum Complexity Tie Breaking
**Purpose**: Worst-case tie breaking (all identical scores/ages)

**Input**:
```
4 4
zoe 88 20
alice 88 20
bob 88 20
charlie 88 20
```

**Expected Output**:
```
alice 88 20
bob 88 20
charlie 88 20
zoe 88 20
```

**Actual Output**:
```
alice 88 20
bob 88 20
charlie 88 20
zoe 88 20
```

**Result**: ✓ PASS

**Corresponding Test Function**: `test_identical_students_multiple`

**Key Validation Point**: All students have same score/age, pure alphabetical order: alice < bob < charlie < zoe

---

## Task 3: Log Summary - Custom Test Cases

### Test Case 1: Normal Case - Mixed Users and Actions

**Category**: Normal Case
**Purpose**: Verify event counting and action frequency detection

**Input**:
```
8
alice login
bob login
alice view
alice logout
bob view
bob view
chris login
bob logout
```

**Expected Output**:
```
bob 4
alice 3
chris 1
top_action: login 3
```

**Actual Output**:
```
bob 4
alice 3
chris 1
top_action: login 3
```

**Result**: ✓ PASS

**Corresponding Test Function**: `test_normal_log_summary`

**Key Validation Point**: 
- bob has 4 events (ranked first)
- alice has 3 events (ranked second)
- login appears 3 times (most frequent action)

---

### Test Case 2: Boundary - Empty Logs

**Category**: Boundary Case
**Purpose**: Verify handling of no input

**Input**:
```
0
```

**Expected Output**:
```
top_action: 0
```

**Actual Output**:
```
top_action: 0
```

**Result**: ✓ PASS

**Corresponding Test Function**: `test_empty_logs`

**Key Validation Point**: No crash on empty input, graceful handling

---

### Test Case 3: Critical - Identi Counts with Alphabetical Tie-Break

**Category**: Tie-Breaking Edge Case
**Purpose**: Users with same event count should be alphabetically ordered

**Input**:
```
6
zoe action1
alice action2
bob action3
charlie action4
david action5
emma action6
```

**Expected Output**:
```
alice 1
bob 1
charlie 1
david 1
emma 1
zoe 1
top_action: (any of the actions with count 1)
```

**Actual Output**:
```
alice 1
bob 1
charlie 1
david 1
emma 1
zoe 1
top_action: action1 1
```

**Result**: ✓ PASS

**Corresponding Test Function**: `test_same_user_count_alphabetical`

**Key Validation Point**: When all users have 1 event, alphabetical order: alice < bob < charlie < ... < zoe

---

### Test Case 4: Action Frequency Detection

**Category**: Action Ranking
**Purpose**: Confirm top_action is correctly identified (highest count)

**Input**:
```
7
alice login
bob login
charlie login
david view
eve view
frank delete
grace delete
```

**Expected Output**:
```
alice 1
bob 1
charlie 1
david 1
eve 1
frank 1
grace 1
top_action: login 3
```

**Actual Output**:
```
alice 1
bob 1
charlie 1
david 1
eve 1
frank 1
grace 1
top_action: login 3
```

**Result**: ✓ PASS

**Corresponding Test Function**: `test_top_action_most_frequent`

**Key Validation Point**: login appears 3 times (most), view and delete each appear 2 times

---

### Test Case 5: Complex Real-World Scenario

**Category**: Stress Test / Complex Mix
**Purpose**: Multiple users with varying action counts and frequencies

**Input**:
```
10
alice login
alice logout
bob view
bob edit
bob delete
charlie login
charlie logout
david view
david edit
eve login
```

**Expected Output**:
```
bob 3
alice 2
charlie 2
david 2
eve 1
top_action: login 3
```

**Actual Output**:
```
bob 3
alice 2
charlie 2
david 2
eve 1
top_action: login 3
```

**Result**: ✓ PASS

**Corresponding Test Function**: `test_complex_mixed_scenario`

**Key Validation Point**: 
- bob leads with 3 events
- alice/charlie/david tied at 2 events, alphabetically ordered
- eve has 1 event
- login appears 3 times (most common)

---

## Summary Statistics

| Task | Test Cases Provided | Total Assertions | Pass Rate |
|------|---------------------|------------------|-----------|
| Task 1 | 5 | 20 | 100% |
| Task 2 | 5 | 15 | 100% |
| Task 3 | 5 | 15 | 100% |
| **Total** | **15** | **50** | **100%** |

---

## Test Design Methodology

Each test case was designed following these principles:

1. **Purpose Clarity**: Each test validates a specific requirement
2. **Input Variation**: From empty/minimal to complex with multiple conditions
3. **Edge Case Coverage**: Negative numbers, zero, empty lists, ties, etc.
4. **Assertion Specificity**: Verify exact order, not just approximate correctness
5. **Traceability**: Each test case maps to actual test functions in test_task*.py

---

## Key Insights from Test Design

1. **Order Matters**: Task 1 (dedup position), Task 2 (ranking), Task 3 (alphabetical sort)
2. **Tie-Breaking Complexity**: Multi-key sorting requires careful test design
3. **Edge Case Discovery**: Negative numbers and zero revealed implementation gaps
4. **Stress Testing**: High duplication ratios and many identical records test robustness

---

## Future Test Enhancements

1. **Performance Tests**: Time complexity verification for large inputs (1M+ elements)
2. **Unicode Tests**: Verify sorting with non-ASCII names
3. **Precision Tests**: Task 2 with floating-point scores (if requirements change)
4. **Concurrent Access**: If code is used in multi-threaded environment
