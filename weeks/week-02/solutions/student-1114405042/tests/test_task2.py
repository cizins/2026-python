"""
Test cases for Task 2: Student Ranking
Tests cover multi-key sorting with different tie-breaking scenarios.
"""
import unittest
import sys
from pathlib import Path
from io import StringIO

# Add parent directory to path to import task2_student_ranking
sys.path.insert(0, str(Path(__file__).parent.parent))

from task2_student_ranking import rank_students


class TestStudentRanking(unittest.TestCase):
    """Test suite for student ranking operations"""

    # === Test Group 1: Normal Sorting Cases ===

    def test_normal_ranking_basic(self):
        """Test basic ranking with clear score differences"""
        input_data = """3 2
alice 85 20
bob 92 19
charlie 88 21"""
        expected_output = "bob 92 19\ncharlie 88 21"
        result = rank_students(input_data)
        self.assertEqual(result.strip(), expected_output)

    def test_normal_ranking_all_different_scores(self):
        """Test ranking where all students have different scores"""
        input_data = """4 3
zoe 95 21
emma 88 20
ian 76 19
amy 92 18"""
        expected_output = "zoe 95 21\namy 92 18\nemma 88 20"
        result = rank_students(input_data)
        self.assertEqual(result.strip(), expected_output)

    def test_normal_ranking_full_list(self):
        """Test ranking returning all students"""
        input_data = """3 3
alpha 80 25
beta 90 20
gamma 85 22"""
        expected_output = "beta 90 20\ngamma 85 22\nalpha 80 25"
        result = rank_students(input_data)
        self.assertEqual(result.strip(), expected_output)

    # === Test Group 2: Tie-Breaking Cases ===

    def test_tiebreak_by_age_same_score(self):
        """Test tie-breaking by age when scores are identical"""
        input_data = """4 3
amy 88 20
bob 88 19
ian 88 19
leo 75 20"""
        # All three have 88: bob and ian both 19 (also need name), amy is 20
        # bob and ian both 19, so sort by name: bob < ian
        expected_output = "bob 88 19\nian 88 19\namy 88 20"
        result = rank_students(input_data)
        self.assertEqual(result.strip(), expected_output)

    def test_tiebreak_by_name_same_score_and_age(self):
        """Test final tie-breaking by name when score and age are identical"""
        input_data = """3 3
zoe 88 19
alice 88 19
bob 88 19"""
        expected_output = "alice 88 19\nbob 88 19\nzoe 88 19"
        result = rank_students(input_data)
        self.assertEqual(result.strip(), expected_output)

    def test_tiebreak_multiple_conditions(self):
        """Test complex tie-breaking with mixed conditions"""
        input_data = """6 6
amy 88 20
bob 88 19
zoe 92 21
ian 88 19
leo 75 20
eva 92 20"""
        # Expected order:
        # eva (92, 20), zoe (92, 21), bob (88, 19), ian (88, 19), amy (88, 20), leo (75, 20)
        expected_output = "eva 92 20\nzoe 92 21\nbob 88 19\nian 88 19\namy 88 20\nleo 75 20"
        result = rank_students(input_data)
        self.assertEqual(result.strip(), expected_output)

    # === Test Group 3: Boundary Cases ===

    def test_k_equals_one(self):
        """Test returning top 1 student"""
        input_data = """3 1
alice 80 25
bob 95 20
charlie 88 22"""
        expected_output = "bob 95 20"
        result = rank_students(input_data)
        self.assertEqual(result.strip(), expected_output)

    def test_k_equals_total(self):
        """Test k equals total number of students"""
        input_data = """2 2
alice 85 20
bob 90 19"""
        expected_output = "bob 90 19\nalice 85 20"
        result = rank_students(input_data)
        self.assertEqual(result.strip(), expected_output)

    def test_single_student_k_one(self):
        """Test with single student and k=1"""
        input_data = """1 1
alice 88 20"""
        expected_output = "alice 88 20"
        result = rank_students(input_data)
        self.assertEqual(result.strip(), expected_output)

    # === Test Group 4: Edge Cases ===

    def test_identical_students_multiple(self):
        """Test with multiple identical student records"""
        input_data = """4 2
alice 88 20
bob 88 20
charlie 88 20
david 88 20"""
        # All identical, sort alphabetically
        expected_output = "alice 88 20\nbob 88 20"
        result = rank_students(input_data)
        self.assertEqual(result.strip(), expected_output)

    def test_very_different_ages(self):
        """Test with very different ages"""
        input_data = """3 3
youngster 85 18
oldster 85 50
middle 90 35"""
        # middle 90, then youngster 18, then oldster 50
        expected_output = "middle 90 35\nyoungster 85 18\noldster 85 50"
        result = rank_students(input_data)
        self.assertEqual(result.strip(), expected_output)

    def test_one_dominant_winner(self):
        """Test where one student clearly dominates"""
        input_data = """5 3
alice 100 20
bob 50 19
charlie 75 25
david 60 21
eve 80 22"""
        expected_output = "alice 100 20\neve 80 22\ncharlie 75 25"
        result = rank_students(input_data)
        self.assertEqual(result.strip(), expected_output)


if __name__ == '__main__':
    unittest.main()
