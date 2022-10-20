from datetime import datetime
from django.test import TestCase
from django.core.exceptions import ValidationError

from samples.sample_function import do_lots_of_things


# Create your tests here.
class DoLotsOfThingsTestCasesForB(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("\nRunning tests for validating 'b' ...\n")
        pass

    dt_obj = '2023-10-16 10:00:22'

    """ dt_obj = datetime.strptime(
        '2023-10-16 10:00:22',
        settings.DATETIME_FORMAT
    ) """

    def test_b_is_foo(self):
        res = do_lots_of_things(2, 'foo', self.dt_obj)
        self.assertTrue(isinstance(res, int))
        self.assertEqual(res, 4)

    def test_b_is_bar(self):
        res = do_lots_of_things(2, 'bar', self.dt_obj)
        self.assertEqual(res, 6)

    def test_b_is_not_foo_not_bar(self):
        res = do_lots_of_things(999, 'b is just b', self.dt_obj)
        self.assertEqual(res, 1998)

    def test_b_is_datetime_string(self):
        res = do_lots_of_things(2, '2023-10-15 20:33:05', self.dt_obj)
        self.assertIsInstance(res, int)

    def test_b_is_empty_string_raises_exception(self):
        with self.assertRaisesMessage(ValidationError, 'b: is invalid'):
            do_lots_of_things(2, '', self.dt_obj)

    def test_b_has_only_spaces_raises_exception(self):
        with self.assertRaisesMessage(ValidationError, 'b:     is invalid'):
            do_lots_of_things(2, '    ', self.dt_obj)

    def test_b_is_integer(self):
        with self.assertRaises(ValidationError, msg='b:123 is invalid'):
            do_lots_of_things(2, 123, self.dt_obj)

    def test_b_is_float(self):
        with self.assertRaises(ValidationError, msg='b:123.321 is invalid'):
            do_lots_of_things(2, 123.321, self.dt_obj)

    def test_b_is_bool_True_raises_exception(self):
        with self.assertRaises(ValidationError, msg='b:True is invalid'):
            do_lots_of_things(2, True, self.dt_obj)

    def test_b_is_bool_False_raises_exception(self):
        with self.assertRaises(ValidationError, msg='b:False is invalid'):
            do_lots_of_things(2, False, self.dt_obj)
