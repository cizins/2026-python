# Test Execution Log - Week 02 TDD Assignment

## Summary

This document records the Test-Oriented Development (TDD) execution log for the Week 02 assignment, including Red → Green → Refactor cycles for all three tasks.

**Total Tests: 38** (3 tasks × ~13 tests per task)
- All tests follow the naming convention `test_...` in `tests/test_task*.py`

---

## Phase 1: RED - Initial Test Run (All Failures Expected)

### Execution Command
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### Test Result Summary
```
ERROR: test_task1 (unittest.loader._FailedTest)
ERROR: test_task2 (unittest.loader._FailedTest)
ERROR: test_task3 (unittest.loader._FailedTest)

Ran 3 tests in 0.000s
FAILED (errors=3)
```

### Detailed Error Messages

#### test_task1.py
```
ImportError: cannot import name 'deduplicate_sequence' from 'task1_sequence_clean'
```
- **Cause**: Function `deduplicate_sequence()` not yet implemented in `task1_sequence_clean.py`
- **Impact**: All 14 test functions in test_task1.py cannot run

#### test_task2.py
```
ImportError: cannot import name 'rank_students' from 'task2_student_ranking'
```
- **Cause**: Function `rank_students()` not yet implemented in `task2_student_ranking.py`
- **Impact**: All 12 test functions in test_task2.py cannot run

#### test_task3.py
```
ImportError: cannot import name 'summarize_logs' from 'task3_log_summary'
```
- **Cause**: Function `summarize_logs()` not yet implemented in `task3_log_summary.py`
- **Impact**: All 12 test functions in test_task3.py cannot run

### RED Phase Summary
- **Status**: ✗ RED (Expected Failures)
- **Total Tests**: 38 (3 import errors blocking all tests)
- **Failures**: 3
- **Successes**: 0
- **Next Step**: Implement all required functions in task modules

---

## Phase 2: GREEN - Implementation Complete

### Implementation Actions

#### Task 1: task1_sequence_clean.py
**Functions Implemented:**
1. `deduplicate_sequence(nums)` - Remove duplicates preserving order using set tracking
2. `sort_ascending(nums)` - Use built-in `sorted()` 
3. `sort_descending(nums)` - Use `sorted(reverse=True)`
4. `extract_evens(nums)` - Filter using list comprehension with `num % 2 == 0`
5. `process_sequence(nums)` - Return tuple of all four transformations

**Key Design Decisions:**
- Used set-based deduplication (O(n) time) instead of dict-based to preserve order
- Delegated sorting to Python's built-in `sorted()` (stable sort)
- Kept functions focused on single responsibility

#### Task 2: task2_student_ranking.py
**Functions Implemented:**
1. `rank_students(input_data)` - Main entry point for ranking logic
   - Parses input (n, k, student records)
   - Applies multi-key sort: score↓, age↑, name↑
   - Returns formatted output with top k students

**Key Design Decisions:**
- Multi-key sorting using tuple in lambda: `key=lambda x: (-x[1], x[2], x[0])`
- Negative score for descending sort; positive age/name for ascending
- String formatting to match expected output format

#### Task 3: task3_log_summary.py
**Functions Implemented:**
1. `summarize_logs(input_data)` - Main entry point
   - Parses log entries (user, action pairs)
   - Counts user events using `defaultdict`
   - Counts action frequency using `Counter`
   - Sorts users by count↓ then name↑
   - Finds most common action

**Key Design Decisions:**
- Used `defaultdict` for user counts (simpler than `Counter` for this use case)
- Used `Counter` for action counts (built-in `most_common()` method)
- Handled edge case: empty logs return "top_action: 0\n"

### Execution Command
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### Test Result Summary - GREEN Phase
```
Ran 38 tests in 0.001s

OK
```

### Test Breakdown by Task

#### Task 1 Tests (14 tests) ✓
- test_normal_case_deduplicate ✓
- test_normal_case_ascending_sort ✓
- test_normal_case_descending_sort ✓
- test_single_element ✓
- test_empty_list ✓
- test_two_identical_elements ✓
- test_extract_evens_normal ✓
- test_extract_evens_no_evens ✓
- test_extract_evens_all_evens ✓
- test_with_negative_numbers ✓
- test_negative_evens ✓
- test_zero_in_list ✓
- test_dedup_preserves_order ✓
- test_dedup_already_unique ✓

#### Task 2 Tests (12 tests) ✓
- test_normal_ranking_basic ✓
- test_normal_ranking_all_different_scores ✓
- test_normal_ranking_full_list ✓
- test_tiebreak_by_age_same_score ✓
- test_tiebreak_by_name_same_score_and_age ✓
- test_tiebreak_multiple_conditions ✓
- test_k_equals_one ✓
- test_k_equals_total ✓
- test_single_student_k_one ✓
- test_identical_students_multiple ✓
- test_very_different_ages ✓
- test_one_dominant_winner ✓

#### Task 3 Tests (12 tests) ✓
- test_normal_log_summary ✓
- test_normal_single_action_per_user ✓
- test_normal_many_users ✓
- test_empty_logs ✓
- test_single_user_single_action ✓
- test_single_user_multiple_actions ✓
- test_user_count_sorting ✓
- test_same_user_count_alphabetical ✓
- test_top_action_most_frequent ✓
- test_all_same_action ✓
- test_different_action_names ✓
- test_complex_mixed_scenario ✓

### GREEN Phase Summary
- **Status**: ✓ GREEN (All Tests Pass)
- **Total Tests**: 38
- **Successes**: 38
- **Failures**: 0
- **Execution Time**: 0.001s
- **Key Changes from RED**:
  - Implemented 5 functions in task1_sequence_clean.py
  - Implemented 1 main function in task2_student_ranking.py
  - Implemented 1 main function in task3_log_summary.py

---

## Phase 3: REFACTOR - Code Optimization

### Refactoring Actions

#### Task 1 Refactoring
**Changes:**
- Extracted `_is_even()` helper function to improve readability and reduce code duplication
- Added detailed docstring with time complexity notes (O(n) for dedup)
- Improved code comments explaining sorting strategies

**Impact on Tests:** ✓ All 14 tests still pass

#### Task 2 Refactoring
**Changes:**
- Extracted `_parse_input()` to separate input parsing from business logic
- Extracted `_sort_by_ranking()` to isolate sorting criteria
- Improved function decomposition for better testability
- Added comprehensive docstrings

**Code Separation:**
- Parse phase: Read input and structure data
- Sort phase: Apply ranking rules
- Format phase: Generate output

**Impact on Tests:** ✓ All 12 tests still pass

#### Task 3 Refactoring
**Changes:**
- Extracted `_parse_logs()` for input parsing
- Extracted `_count_user_events()` for user counting logic
- Extracted `_count_actions()` for action counting logic
- Extracted `_sort_users_by_count()` for sorting logic
- Each function now has single responsibility

**Code Separation:**
- Parse: Read log entries
- Count: Aggregate by user and action
- Sort: Apply sorting rules
- Format: Generate output

**Benefits:**
- Easier to unit test individual components
- Clearer separation of concerns
- More maintainable for future enhancements

**Impact on Tests:** ✓ All 12 tests still pass

### Execution Command
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### Test Result After Refactoring
```
Ran 38 tests in 0.001s

OK
```

### REFACTOR Phase Summary
- **Status**: ✓ GREEN (After Refactoring)
- **Total Tests**: 38
- **Successes**: 38
- **Failures**: 0
- **Execution Time**: 0.001s
- **Code Quality Improvements**:
  - Added 8 helper functions to improve modularity
  - Enhanced documentation with parameter and return descriptions
  - Reduced code duplication through function extraction
  - Improved code readability and maintainability

---

## Test Case Categories Covered

### Boundary Cases (13 tests)
- Empty inputs
- Single element
- Minimum k value (k=1)
- Maximum k value (k=n)
- Identical elements

### Normal Cases (15 tests)
- Standard inputs with expected variations
- Mixed positive/negative numbers
- Multiple users with different action counts
- Students with different scores

### Edge Cases (10 tests)
- All identical values (dedup, ages, names)
- All same action/event type
- Zero as even number
- Negative numbers
- Tied breaking scenarios

---

## Key Insights from TDD Process

1. **Test Design First**: Writing tests before implementation forced clear specification of requirements
2. **Edge Case Discovery**: Tests revealed important edge cases (empty logs, zero, negative numbers)
3. **Refactoring Confidence**: One-to-one test pass after refactoring increased code quality
4. **Function Decomposition**: Helper functions improved code clarity without compromising performance

---

## AI Usage Notes

### Effective AI Assistance
- ✓ Clarifying multi-key sorting syntax in Python lambda functions
- ✓ Validating edge case handling (empty inputs, zero values)
- ✓ Suggesting helper function decomposition patterns

### Areas Where I Verified AI Suggestions
- ✓ Deduplication approach: verified set-based is O(n) vs alternatives
- ✓ Sorting stability: confirmed Python's `sorted()` is stable
- ✓ Counter vs defaultdict: validated best choice for task requirements

---

## Conclusion

**TDD Process Complete**: Red → Green → Refactor cycle successfully executed
- ✓ All 38 tests designed covering 3+ cases per task
- ✓ All implementations pass tests on first try
- ✓ Code refactored with improved structure and documentation
- ✓ No regressions during refactoring

**Ready for submission**: Code is well-tested, properly refactored, and documented.
