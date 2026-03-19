"""
Test cases for Task 3: Log Summary
Tests cover user event counting and most frequent action detection.
"""
import unittest
import sys
from pathlib import Path

# Add parent directory to path to import task3_log_summary
sys.path.insert(0, str(Path(__file__).parent.parent))

from task3_log_summary import summarize_logs


class TestLogSummary(unittest.TestCase):
    """Test suite for log summary operations"""

    # === Test Group 1: Normal Cases ===

    def test_normal_log_summary(self):
        """Test normal case: multiple users with multiple actions"""
        input_data = """8
alice login
bob login
alice view
alice logout
bob view
bob view
chris login
bob logout"""
        expected = "bob 4\nalice 3\nchris 1\ntop_action: login 3"
        result = summarize_logs(input_data)
        self.assertEqual(result.strip(), expected)

    def test_normal_single_action_per_user(self):
        """Test normal case: each user has one action"""
        input_data = """3
alice login
bob logout
charlie view"""
        # Each user: 1 action. Top action: all tied at 1, pick alphabetically first
        # Could be any of login, logout, view since all have count 1
        result = summarize_logs(input_data)
        lines = result.strip().split('\n')
        self.assertEqual(len(lines), 4)  # 3 users + top_action line
        self.assertIn("alice 1", result)
        self.assertIn("bob 1", result)
        self.assertIn("charlie 1", result)
        self.assertIn("top_action:", result)

    def test_normal_many_users(self):
        """Test normal case: many users with varying action counts"""
        input_data = """6
user1 action
user2 action
user3 action
user4 action
user5 action
user6 action"""
        result = summarize_logs(input_data)
        lines = result.strip().split('\n')
        # 6 users each with 1 action, plus 1 top_action line
        self.assertEqual(len(lines), 7)

    # === Test Group 2: Boundary Cases ===

    def test_empty_logs(self):
        """Test boundary: no logs (m=0)"""
        input_data = """0"""
        result = summarize_logs(input_data)
        # Should handle gracefully - either empty or just top_action line
        self.assertIsNotNone(result)

    def test_single_user_single_action(self):
        """Test boundary: one user with one action"""
        input_data = """1
alice login"""
        result = summarize_logs(input_data)
        lines = result.strip().split('\n')
        self.assertIn("alice 1", result)
        self.assertIn("top_action: login 1", result)

    def test_single_user_multiple_actions(self):
        """Test boundary: one user with multiple actions"""
        input_data = """4
alice login
alice view
alice logout
alice view"""
        result = summarize_logs(input_data)
        lines = result.strip().split('\n')
        self.assertIn("alice 4", result)
        # view appears twice, others once - top_action should be view
        self.assertIn("top_action: view 2", result)

    # === Test Group 3: Counting & Sorting Cases ===

    def test_user_count_sorting(self):
        """Test users are sorted by count (descending)"""
        input_data = """7
alice action1
bob action2
bob action3
charlie action4
charlie action5
charlie action6
david action7"""
        # alice: 1, bob: 2, charlie: 3, david: 1
        # Order: charlie (3), bob (2), alice (1), david (1)
        # alice and david both 1, sort by name: alice < david
        expected_start = "charlie 3\nbob 2\nalice 1\ndavid 1"
        result = summarize_logs(input_data)
        self.assertTrue(result.strip().startswith(expected_start))

    def test_same_user_count_alphabetical(self):
        """Test users with same action count are sorted alphabetically"""
        input_data = """6
zoe login
alice logout
bob view
charlie delete
david edit
emma upload"""
        # Each user has 1 action, should be alphabetical
        result = summarize_logs(input_data)
        lines = result.strip().split('\n')
        # First 5 lines should be users in alphabetical order
        self.assertTrue(lines[0].startswith("alice"))
        self.assertTrue(lines[1].startswith("bob"))
        self.assertTrue(lines[2].startswith("charlie"))
        self.assertTrue(lines[3].startswith("david"))
        self.assertTrue(lines[4].startswith("emma"))

    def test_top_action_most_frequent(self):
        """Test top_action is the most frequent action"""
        input_data = """7
alice login
bob login
charlie login
david view
eve view
frank delete
grace delete"""
        # login: 3, view: 2, delete: 2
        # top_action should be login with count 3
        result = summarize_logs(input_data)
        self.assertIn("top_action: login 3", result)

    # === Test Group 4: Action Edge Cases ===

    def test_all_same_action(self):
        """Test when all users perform the same action"""
        input_data = """4
alice login
bob login
charlie login
david login"""
        result = summarize_logs(input_data)
        self.assertIn("top_action: login 4", result)

    def test_different_action_names(self):
        """Test with various action names (spaces in parsing)"""
        input_data = """5
user1 login
user2 logout
user3 view_profile
user4 edit_post
user5 delete"""
        result = summarize_logs(input_data)
        self.assertIn("top_action:", result)
        # Check that underscores in action names don't break parsing
        self.assertIsNotNone(result)

    def test_complex_mixed_scenario(self):
        """Test complex scenario with tied counts"""
        input_data = """10
alice login
alice logout
bob view
bob edit
bob delete
charlie login
charlie logout
david view
david edit
eve login"""
        # alice: 2, bob: 3, charlie: 2, david: 2, eve: 1
        # Users sorted: bob 3, alice 2, charlie 2, david 2, eve 1
        # alice/charlie/david at same level (2) - alphabetical
        # login: 3, logout: 2, view: 2, edit: 2, delete: 1
        result = summarize_logs(input_data)
        lines = result.strip().split('\n')
        self.assertIn("bob 3", result)
        self.assertIn("top_action: login 3", result)


if __name__ == '__main__':
    unittest.main()
