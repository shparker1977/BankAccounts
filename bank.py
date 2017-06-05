from account import Account


class Bank:

    def __init__(self):

        self.bank_accounts = dict()

    def add_bank_account(self, name, acct_num, acct_limit, balance=0):
        new_account = Account(name, acct_num, acct_limit, balance=0)
        self.bank_accounts[new_account.name] = new_account

    def charge_bank_account(self, account_name, charge):
        pass

    def credit_bank_account(self, account_name, credit):
        pass

    def change_account_limit(self, account_name, new_limit):
        pass

    def list_all_accounts(self):
        for x in self.bank_accounts:
            print(x.name + ', ' + x.acct_num + ', ' + x.balance)
