import unittest
from src.StudentAnalyzer import filter_gioi, average_score

class TestStudentUtils(unittest.TestCase):

    def test_filter_gioi_mixed_valid_invalid(self):
        result = filter_gioi([9, 7, 8, 12, -1])
        self.assertEqual(result, [9, 8])
        print("test_filter_gioi_mixed_valid_invalid passed:", result)

    def test_filter_gioi_all_valid(self):
        result = filter_gioi([10, 9, 8.5])
        self.assertEqual(result, [10, 9, 8.5])
        print("test_filter_gioi_all_valid passed:", result)

    def test_filter_gioi_empty_list(self):
        result = filter_gioi([])
        self.assertEqual(result, [])
        print("test_filter_gioi_empty_list passed:", result)

    def test_filter_gioi_only_boundary_values(self):
        result = filter_gioi([0, 10])
        self.assertEqual(result, [10])
        print("test_filter_gioi_only_boundary_values passed:", result)

    def test_filter_gioi_all_invalid_scores(self):
        result = filter_gioi([-2, 11, 15])
        self.assertEqual(result, [])
        print("test_filter_gioi_all_invalid_scores passed:", result)

    def test_average_score_mixed_valid_invalid(self):
        result = average_score([5, 7, -1, 10, 11])
        expected = (5 + 7 + 10) / 3
        self.assertAlmostEqual(result, expected)
        print(f"test_average_score_mixed_valid_invalid passed: {result:.2f}")

    def test_average_score_all_valid(self):
        result = average_score([8, 9, 10])
        self.assertAlmostEqual(result, 9.0)
        print(f"test_average_score_all_valid passed: {result:.2f}")

    def test_average_score_empty_list(self):
        result = average_score([])
        self.assertEqual(result, 0)
        print("test_average_score_empty_list passed:", result)

    def test_average_score_only_boundary_values(self):
        result = average_score([0, 10])
        self.assertEqual(result, 5.0)
        print("test_average_score_only_boundary_values passed:", result)

    def test_average_score_all_invalid_scores(self):
        result = average_score([-5, 20])
        self.assertEqual(result, 0)
        print("test_average_score_all_invalid_scores passed:", result)

if __name__ == '__main__':
    unittest.main()
