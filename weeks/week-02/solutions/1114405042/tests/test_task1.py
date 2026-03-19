"""
Test cases for Task 1: Sequence Clean
Tests cover normal cases, boundary cases, and edge cases.
"""
import unittest
import sys
from pathlib import Path

# Add parent directory to path to import task1_sequence_clean
sys.path.insert(0, str(Path(__file__).parent.parent))

from task1_sequence_clean import (
    deduplicate_sequence,
    sort_ascending,
    sort_descending,
    extract_evens,
    process_sequence
)


class TestSequenceClean(unittest.TestCase):
    """Test suite for sequence clean operations"""

    # === Test Group 1: Normal Cases ===
    
    def test_normal_case_deduplicate(self):
        """Test normal case: deduplicate preserves first occurrence order"""
        nums = [5, 3, 5, 2, 9, 2, 8, 3, 1]
        expected = [5, 3, 2, 9, 8, 1]
        result = deduplicate_sequence(nums)
        self.assertEqual(result, expected)

    def test_normal_case_ascending_sort(self):
        """Test normal case: sort ascending with duplicates"""
        nums = [5, 3, 5, 2, 9, 2, 8, 3, 1]
        expected = [1, 2, 2, 3, 3, 5, 5, 8, 9]
        result = sort_ascending(nums)
        self.assertEqual(result, expected)

    def test_normal_case_descending_sort(self):
        """Test normal case: sort descending with duplicates"""
        nums = [5, 3, 5, 2, 9, 2, 8, 3, 1]
        expected = [9, 8, 5, 5, 3, 3, 2, 2, 1]
        result = sort_descending(nums)
        self.assertEqual(result, expected)

    # === Test Group 2: Boundary Cases ===

    def test_single_element(self):
        """Test boundary: single element"""
        nums = [5]
        self.assertEqual(deduplicate_sequence(nums), [5])
        self.assertEqual(sort_ascending(nums), [5])
        self.assertEqual(sort_descending(nums), [5])

    def test_empty_list(self):
        """Test boundary: empty list"""
        nums = []
        self.assertEqual(deduplicate_sequence(nums), [])
        self.assertEqual(sort_ascending(nums), [])
        self.assertEqual(sort_descending(nums), [])

    def test_two_identical_elements(self):
        """Test boundary: only two identical elements"""
        nums = [3, 3]
        self.assertEqual(deduplicate_sequence(nums), [3])
        self.assertEqual(sort_ascending(nums), [3, 3])
        self.assertEqual(sort_descending(nums), [3, 3])

    # === Test Group 3: Evens Extraction ===

    def test_extract_evens_normal(self):
        """Test extract evens: normal case with mixed numbers"""
        nums = [5, 3, 5, 2, 9, 2, 8, 3, 1]
        expected = [2, 2, 8]
        result = extract_evens(nums)
        self.assertEqual(result, expected)

    def test_extract_evens_no_evens(self):
        """Test extract evens: no even numbers"""
        nums = [1, 3, 5, 7, 9]
        expected = []
        result = extract_evens(nums)
        self.assertEqual(result, expected)

    def test_extract_evens_all_evens(self):
        """Test extract evens: all even numbers"""
        nums = [2, 4, 6, 8, 10]
        expected = [2, 4, 6, 8, 10]
        result = extract_evens(nums)
        self.assertEqual(result, expected)

    # === Test Group 4: Edge Cases & Negative Numbers ===

    def test_with_negative_numbers(self):
        """Test with negative numbers"""
        nums = [-5, 3, -2, 5, -2, 8]
        dedup = deduplicate_sequence(nums)
        asc = sort_ascending(nums)
        self.assertEqual(sort_ascending(dedup), [-5, -2, 3, 5, 8])
        self.assertIn(-2, asc)
        self.assertIn(-5, asc)

    def test_negative_evens(self):
        """Test extract evens with negative numbers"""
        nums = [-4, -3, 2, -2, 5, 6]
        expected = [-4, 2, -2, 6]
        result = extract_evens(nums)
        self.assertEqual(result, expected)

    def test_zero_in_list(self):
        """Test with zero (which is even)"""
        nums = [0, 1, 2, 3, 0]
        evens = extract_evens(nums)
        self.assertEqual(evens, [0, 2, 0])
        self.assertEqual(deduplicate_sequence(nums), [0, 1, 2, 3])

    # === Test Group 5: Deduplication Order Preservation ===

    def test_dedup_preserves_order(self):
        """Test that deduplication preserves first occurrence order"""
        nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        expected = [3, 1, 4, 5, 9, 2, 6]
        result = deduplicate_sequence(nums)
        self.assertEqual(result, expected)

    def test_dedup_already_unique(self):
        """Test dedup when all elements are unique"""
        nums = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        result = deduplicate_sequence(nums)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
