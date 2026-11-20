import unittest
from statistics import calculate_statistics


class StatisticsTestCase(unittest.TestCase):
    def test_normal_numbers(self):
        result = calculate_statistics([10, 20, 30])
        self.assertEqual(result["min"], 10)
        self.assertEqual(result["max"], 30)
        self.assertEqual(result["average"], 20)

    def test_negative_numbers(self):
        result = calculate_statistics([-5, -2, -10])
        self.assertEqual(result["min"], -10)
        self.assertEqual(result["max"], -2)
        self.assertEqual(result["average"], -17 / 3)

    def test_single_number(self):
        result = calculate_statistics([7])
        self.assertEqual(result["min"], 7)
        self.assertEqual(result["max"], 7)
        self.assertEqual(result["average"], 7)

    def test_same_numbers(self):
        result = calculate_statistics([4, 4, 4])
        self.assertEqual(result["min"], 4)
        self.assertEqual(result["max"], 4)
        self.assertEqual(result["average"], 4)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_statistics([])
