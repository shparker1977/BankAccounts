from account import Account
import collections


class Bank:

    def __init__(self):

        self.bank_accounts = collections.OrderedDict()

    def add_bank_account(self, name, acct_num, acct_limit):
        new_account = Account(name, acct_num, acct_limit)
        if new_account.name in self.bank_accounts.keys():
            raise BankError('Invalid Input')

        self.bank_accounts[new_account.name] = new_account

    def list_all_accounts(self):
        for x in self.bank_accounts:
            print(x + ', ' + str(self.bank_accounts[x].account_num) + ': ' + str(self.bank_accounts[x].balance))


class BankError(Exception):
    def __init__(self, message):
        self.message = message
