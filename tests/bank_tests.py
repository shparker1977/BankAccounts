import unittest
import sys
import os

sys.path.append(os.path.abspath(sys.path[0] + '/../'))
from bank import Bank, BankError

class AccountTestCase(unittest.TestCase):
    """ Tests for account.py """

    # Test the bank functions
    def test_add_two_accounts_to_bank(self):
        my_bank = Bank()
        my_bank.add_bank_account('test', 356938035643809, 1000)
        my_bank.add_bank_account('test_two', 356938035643809, 1000)

        self.assertEqual(len(my_bank.bank_accounts), 2)

    def test_charge_account(self):
        my_bank = Bank()
        my_bank.add_bank_account('test', 356938035643809, 1000)
        my_bank.bank_accounts['test'].charge_account(250)

        self.assertEqual(my_bank.bank_accounts['test'].balance, 250)

    def test_credit_account(self):
        my_bank = Bank()
        my_bank.add_bank_account('test', 356938035643809, 1000)
        my_bank.bank_accounts['test'].credit_account(500)

        self.assertEqual(my_bank.bank_accounts['test'].balance, -500)

    def test_reset_account(self):
        my_bank = Bank()
        my_bank.add_bank_account('test', 356938035643809, 1000)
        my_bank.bank_accounts['test'].credit_account(500)

        self.assertEqual(my_bank.bank_accounts['test'].balance, -500)

        my_bank.bank_accounts['test'].reset_account()

        self.assertEqual(my_bank.bank_accounts['test'].balance, 0)

    def test_change_account_limit(self):
        my_bank = Bank()
        my_bank.add_bank_account('test', 356938035643809, 1000)
        my_bank.bank_accounts['test'].change_account_limit(2000)

        self.assertEqual(my_bank.bank_accounts['test'].acct_limit, 2000)


if __name__ == '__main__':
    unittest.main()
