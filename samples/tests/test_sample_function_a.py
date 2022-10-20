from django.test import TestCase
from django.core.exceptions import ValidationError

from samples.sample_function import do_lots_of_things


# Create your tests here.
class DoLotsOfThingsTestCasesForA(TestCase):

    """ We can write these methods for more detailed test descriptions """
    @classmethod
    def setUpTestData(cls):
        print("\nRunning tests for validating 'a' ...\n")
        pass

    def setUp(self) -> None:
        self.dt_str = '2023-10-15 20:33:05'

    def test_a_is_zero(self):
        res = do_lots_of_things(0, 'foo', self.dt_str)
        self.assertTrue(isinstance(res, int))
        self.assertEqual(res, 0)

    def test_a_is_signed_integer(self):
        res = do_lots_of_things(-1, 'foo', self.dt_str)
        self.assertTrue(isinstance(res, int))
        self.assertEqual(res, -2)

    def test_a_is_unsigned_integer(self):
        res = do_lots_of_things(5, 'foo', self.dt_str)
        self.assertTrue(isinstance(res, int))
        self.assertEqual(res, 10)

    def test_a_is_a_very_large_integer(self):
        res = do_lots_of_things(2147483647, 'foo', self.dt_str)
        self.assertTrue(isinstance(res, int))
        self.assertEqual(res, 4294967294)

    """
    Boolean is a subclass of integer class, so True is equals to
    as 1 and False. But we strictly validate integers, hence we are
    writing test cases
    """
    def test_a_is_bool_True_raises_exception(self):
        with self.assertRaises(ValidationError, msg='a:True is invalid'):
            do_lots_of_things(True, 'foo', self.dt_str)

    def test_a_is_bool_False_raises_exception(self):
        with self.assertRaises(ValidationError, msg='a:False is invalid'):
            do_lots_of_things(True, 'foo', self.dt_str)

    def test_a_is_a_real_number_raises_exception(self):
        with self.assertRaises(ValidationError, msg='a:1.25 is invalid'):
            do_lots_of_things(1.25, 'foo', self.dt_str)

    def test_a_is_a_float_value_raises_exception(self):
        with self.assertRaises(ValidationError, msg='a:9999.9999 is invalid'):
            do_lots_of_things(9999.9999, 'foo', self.dt_str)

