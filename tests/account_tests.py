import unittest
import sys
import os

sys.path.append(os.path.abspath(sys.path[0] + '/../'))
from account import Account, AccountError


class AccountTestCase(unittest.TestCase):
    """ Tests for account.py """

    def test_account_number_less_than_ten_digits(self):
        try:
            Account('test', 1234567, 1)
        except AccountError as e:
            self.assertEqual(e.message, 'Account number must be 10 or more digits.')

    def test_account_number_not_luhn10_compliant(self):
        try:
            Account('test', 12345678901, 1)
        except AccountError as e:
            self.assertEqual(e.message, 'Account number must be luhn10 compliant.')

    def test_account_with_zero_limit(self):
        try:
            Account('test', 356938035643809, 0)
        except AccountError as e:
            self.assertEqual(e.message, 'Account limit must be > 0.')

    def test_balance_exceeds_limit(self):
        test_account = Account('test', 356938035643809, 1)
        test_account.charge_account(2)

        self.assertEqual(test_account.balance, 0)

    def test_reset_account(self):
        test_account = Account('test', 356938035643809, 100)
        test_account.reset_account()

        self.assertEqual(test_account.balance, 0)

    def test_charge_over_limit_ignored(self):
        test_account = Account('test', 356938035643809, 3)
        test_account.charge_account(5)

        self.assertEqual(test_account.balance, 0)

    def test_change_account_limit(self):
        test_account = Account('test', 356938035643809, 1)
        test_account.change_account_limit(100)

        self.assertEqual(test_account.acct_limit, 100)

    def test_change_account_limit_to_zero(self):
        test_account = Account('test', 356938035643809, 1)
        test_account.change_account_limit(0)

        self.assertEqual(test_account.acct_limit, 1)

    def test_charge_account(self):
        test_account = Account('test', 356938035643809, 100)
        test_account.charge_account(20)

        self.assertEqual(test_account.balance, 20)

    def test_credit_account(self):
        test_account = Account('test', 356938035643809, 100)
        test_account.credit_account(20)

        self.assertEqual(test_account.balance, -20)


if __name__ == '__main__':
    unittest.main()