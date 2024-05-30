from django.test import TestCase
import unittest
from application.utils import normalize_term, normalize_date


class NormalizeTermTests(unittest.TestCase):
    def test_years(self):
        self.assertEqual(normalize_term("2 года"), "2_0_0_0")

    def test_months(self):
        self.assertEqual(normalize_term("3 месяца"), "0_3_0_0")

    def test_weeks(self):
        self.assertEqual(normalize_term("1 неделя"), "0_0_1_0")

    def test_days(self):
        self.assertEqual(normalize_term("10 дней"), "0_0_0_10")

    def test_combined(self):
        self.assertEqual(normalize_term("2 года 3 месяца 1 неделю 10 дней"), "2_3_1_10")

    def test_partial(self):
        self.assertEqual(normalize_term("5 месяцев 2 недели"), "0_5_2_0")

    def test_invalid(self):
        self.assertEqual(normalize_term("полгода"), "0_0_0_0")

    def test_artifacts(self):
        self.assertEqual(normalize_term(" 2   года  3 месяца "), "2_3_0_0")


class NormalizeDateTests(unittest.TestCase):
    def test_dd_mm_yyyy(self):
        self.assertEqual(normalize_date("01.02.2022"), "01.02.2022")

    def test_dd_month_yyyy(self):
        self.assertEqual(normalize_date("1 февраля 2022"), "01.02.2022")

    def test_dd_month_yyyy_with_year(self):
        self.assertEqual(normalize_date("5 ноября 2022 года"), "05.11.2022")

    def test_with_artifacts(self):
        self.assertEqual(normalize_date(" 1 февраля  2022 года "), "01.02.2022")