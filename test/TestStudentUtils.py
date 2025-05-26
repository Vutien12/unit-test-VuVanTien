import unittest
from src.StudentAnalyzer import filter_gioi, average_score

class TestStudentAnalyzer(unittest.TestCase):

    # --- Tests for filter_gioi ---
    def test_filter_gioi_mixed_valid_invalid(self):
        self.assertEqual(filter_gioi([9, 7, 8, 12, -1]), [9, 8])

    def test_filter_gioi_all_valid(self):
        self.assertEqual(filter_gioi([10, 9, 8.5]), [10, 9, 8.5])

    def test_filter_gioi_empty_list(self):
        self.assertEqual(filter_gioi([]), [])

    def test_filter_gioi_none(self):
        self.assertEqual(filter_gioi(None), [])

    def test_filter_gioi_only_boundary_values(self):
        self.assertEqual(filter_gioi([0, 10]), [10])

    def test_filter_gioi_all_invalid_scores(self):
        self.assertEqual(filter_gioi([-2, 11, 15]), [])

    # --- Tests for average_score ---
    def test_average_score_mixed_valid_invalid(self):
        self.assertAlmostEqual(average_score([5, 7, -1, 10, 11]), (5 + 7 + 10) / 3)

    def test_average_score_all_valid(self):
        self.assertAlmostEqual(average_score([8, 9, 10]), 9.0)

    def test_average_score_empty_list(self):
        self.assertEqual(average_score([]), 0)

    def test_average_score_none(self):
        self.assertEqual(average_score(None), 0)

    def test_average_score_only_boundary_values(self):
        self.assertEqual(average_score([0, 10]), 5.0)

    def test_average_score_all_invalid_scores(self):
        self.assertEqual(average_score([-5, 20]), 0)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()         # pragma: no cover
