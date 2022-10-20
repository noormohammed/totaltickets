from datetime import datetime
from django.test import TestCase
from django.conf import settings
from django.test.utils import override_settings

from samples.sample_function import do_lots_of_things

from django.core.exceptions import ValidationError


# Base class for Test classes
class BaseClassForTestingC(object):

    dt_next_year_str = '2023-10-15 10:00:22'

    dt_this_year_str = '2022-10-15 11:22:33'

    dt_prev_year_str = '2021-10-15 22:33:44'

    dt_obj = datetime.strptime(
        '2023-10-16 10:00:22',
        settings.DATETIME_FORMAT
    )

# Create your tests here.
class DoLotsOfThingsTestCasesForC(BaseClassForTestingC, TestCase):

    @classmethod
    def setUpTestData(cls):
        print("\nRunning tests for validating 'c' ...\n")
        pass

    def test_c_is_valid_datetime_string(self):
        res = do_lots_of_things(2, 'foo', self.dt_next_year_str)
        self.assertEquals(res, 4)

    def test_c_is_valid_datetime_object(self):
        res = do_lots_of_things(2, 'foo', self.dt_obj)
        self.assertEquals(res, 4)

    def test_c_is_valid_and_b_is_bar(self):
        res = do_lots_of_things(2, 'bar', self.dt_next_year_str)
        self.assertEquals(res, 6)

    def test_c_is_valid_and_b_is_foo(self):
        res = do_lots_of_things(10, 'foo', self.dt_next_year_str)
        self.assertEquals(res, 20)

    def test_c_is_empty_string(self):
        with self.assertRaisesMessage(ValidationError, 'c is invalid'):
            do_lots_of_things(2, 'foo', '')

    def test_c_is_incorrect_format_datetime(self):
        with self.assertRaisesMessage(ValidationError, 'c is invalid'):
            do_lots_of_things(2, 'foo', '2021/10/15 20:33:05')

    def test_c_is_without_time_str(self):
        with self.assertRaisesMessage(ValidationError, 'c is invalid'):
            do_lots_of_things(2, 'foo', '2023-10-22')

    def test_c_is_bool_true(self):
        with self.assertRaisesMessage(ValidationError, 'c is invalid'):
            do_lots_of_things(2, 'foo', True)

    def test_c_is_bool_false(self):
        with self.assertRaisesMessage(ValidationError, 'c is invalid'):
            do_lots_of_things(2, 'foo', False)

    def test_c_is_valid_2022_year(self):
        with self.assertRaisesMessage(ValidationError, 'c is not next year'):
            do_lots_of_things(2, 'foo', self.dt_this_year_str)

    def test_c_is_valid_2021_year(self):
        with self.assertRaisesMessage(ValidationError, 'c is not next year'):
            do_lots_of_things(2, 'foo', self.dt_prev_year_str)


"""
Its not recommended to change settings during run time, but only doing
this for testing purpose
"""
@override_settings(ALWAYS_CHECK_C =  False)
class OverrideSettingsTestCases(BaseClassForTestingC, TestCase):

    @classmethod
    def setUpTestData(cls):
        print("\nRunning tests with overriding ALWAYS_CHECK_C setting ...\n")
        pass

    def test_with_always_check_c_false_2022_year(self):
        res = do_lots_of_things(5, 'foo', self.dt_this_year_str)
        self.assertEquals(res, 10)

    def test_with_always_check_c_false_2021_year(self):
        res = do_lots_of_things(5, 'foo', self.dt_prev_year_str)
        self.assertEquals(res, 10)

    def test_with_always_check_c_false_2023_year(self):
        res = do_lots_of_things(5, 'foo', self.dt_next_year_str)
        self.assertEquals(res, 10)