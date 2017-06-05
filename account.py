from luhn import generate, verify


class Account:

    def __init__(self, name, acct_num, acct_limit, balance=0):
        if len(str(acct_num)) < 10:
            raise AccountError('Account number must be 10 or more digits.')
        if not verify(str(acct_num)):
            raise AccountError('Account number must be luhn10 compliant.')
        if acct_limit <= 0:
            raise AccountError('Account limit must be > 0.')

        self._name = name
        self._acct_num = acct_num
        self._acct_limit = acct_limit
        self._balance = balance

    @property
    def name(self):
        return self._name

    @property
    def account_num(self):
        return self._account_num

    @property
    def acct_limit(self):
        return self._acct_limit

    @acct_limit.setter
    def acct_limit(self, value):
        if value > 0 and value > self.balance:
            self._acct_limit = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < self.acct_limit:
            self._balance = value

    def credit_account(self, amount):
        self.balance -= amount

    def charge_account(self, amount):
        self.balance += amount

    def change_account_limit(self, new_limit):
        self.acct_limit = new_limit

    def reset_account(self):
        self.balance = 0


class AccountError(Exception):
    def __init__(self, message):
        self.message = message
