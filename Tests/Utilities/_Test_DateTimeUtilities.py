import unittest
from src.MetaKit.Utilities import DateTimeUtilities
from datetime import date, datetime


class MyTestCase(unittest.TestCase):
    def test_convert_str_to_datetime(self):
        result = DateTimeUtilities.convert_str_to_datetime("6/21/2025")
        self.assertEqual(result.date(), date(2025, 6, 21))

    def test_get_end_of_year(self):
        result = DateTimeUtilities.get_end_of_year(date(2025, 6, 21))
        self.assertEqual(result, date(2025, 12, 31))

    def test_get_end_of_year_plus(self):
        result = DateTimeUtilities.get_end_of_year(date(2025, 6, 21), years_to_add=1)
        self.assertEqual(result, date(2026, 12, 31))

    def test_get_end_of_year_minus(self):
        result = DateTimeUtilities.get_end_of_year(date(2025, 6, 21), years_to_add=-1)
        self.assertEqual(result, date(2024, 12, 31))

    def test_get_quarter_0(self):
        result = DateTimeUtilities.get_quarter(selected_date=datetime(2025, 1, 1))
        self.assertEqual(result, 1)

    def test_get_quarter_1(self):
        result = DateTimeUtilities.get_quarter(selected_date=date(2025, 1, 13))
        self.assertEqual(result, 1)

    def test_get_quarter_2(self):
        result = DateTimeUtilities.get_quarter(selected_date=date(2025, 3, 31))
        self.assertEqual(result, 1)

    def test_get_quarter_3(self):
        result = DateTimeUtilities.get_quarter(selected_date=date(2025, 4, 1))
        self.assertEqual(result, 2)

    def test_get_quarter_4(self):
        result = DateTimeUtilities.get_quarter(selected_date=date(2025, 6, 30))
        self.assertEqual(result, 2)

    def test_get_quarter_5(self):
        result = DateTimeUtilities.get_quarter(selected_date=date(2025, 12, 31))
        self.assertEqual(result, 4)

    def test_get_prior_day_0(self):
        result = DateTimeUtilities.get_prior_day(selected_date=date(2025, 6, 2))
        self.assertEqual(result, date(2025, 6, 1))

    def test_get_prior_day_1(self):
        result = DateTimeUtilities.get_prior_day(selected_date=date(2025, 1, 1))
        self.assertEqual(result, date(2024, 12, 31))

    def test_get_end_of_month_0(self):
        result = DateTimeUtilities.get_end_of_month(selected_date=date(2025, 6, 1))
        self.assertEqual(result, date(2025, 6, 30))

    def test_get_end_of_month_1(self):
        result = DateTimeUtilities.get_end_of_month(selected_date=date(2025, 6, 30))
        self.assertEqual(result, date(2025, 6, 30))

    def test_get_end_of_month_2(self):
        result = DateTimeUtilities.get_end_of_month(selected_date=date(2025, 6, 30), months_to_add=1)
        self.assertEqual(result, date(2025, 7, 31))

    def test_get_end_of_month_3(self):
        result = DateTimeUtilities.get_end_of_month(selected_date=date(2025, 6, 30), months_to_add=-1)
        self.assertEqual(result, date(2025, 5, 31))


if __name__ == '__main__':
    unittest.main()

#%%
