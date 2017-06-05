import unittest
import sys
import os

sys.path.append(os.path.abspath(sys.path[0] + '/../'))
from account import Account


class BankProgramTestCase(unittest.TestCase):
    """ Tests for account.py """

    def test_action_on_non_existent_account(self):
        pass

    def test_negative_amount_charged(self):
        pass

    def test_negative_balance_limit_provided_during_creation(self):
        pass

    def test_negative_balance_limit_update(self):
        pass

    def test_account_number_less_than_10_digits(self):
        pass

    def test_account_number_not_luhn10_compliant(self):
        pass

    def test_string_passed_as_balance(self):
        pass

    def test_string_passed_as_limit(self):
        pass

    def test_string_passed_as_charge_amount(self):
        pass

    def test_string_passed_as_credit_amount(self):
        pass

if __name__ == '__main__':
    unittest.main()