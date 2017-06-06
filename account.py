from luhn import generate, verify


class Account:

    def __init__(self, name, acct_num, acct_limit):
        if len(str(acct_num)) < 10:
            raise AccountError('Account number must be 10 or more digits.')
        if not verify(str(acct_num)):
            raise AccountError('Account number must be luhn10 compliant.')
        if acct_limit < 0:
            raise AccountError('Account limit must be > -1.')

        self._name = name
        self._acct_num = acct_num
        self._acct_limit = acct_limit
        self._balance = 0

    @property
    def name(self):
        return self._name

    @property
    def account_num(self):
        return self._acct_num

    @property
    def acct_limit(self):
        return self._acct_limit

    @acct_limit.setter
    def acct_limit(self, value):
        if not isinstance(value, int):
            raise AccountValueError('Account limit must be an integer')
        if value < 0:
            raise AccountValueError('Account limit must be > -1')
        if value > self.balance:
            self._acct_limit = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, int):
            raise AccountValueError('Balance must be an integer')
        if value < self.acct_limit:
            self._balance = value

    def credit_account(self, amount):
        if not isinstance(amount, int):
            raise AccountValueError('Credit amount must be an integer')
        if amount < 0:
            raise AccountValueError('Credit amount must be > -1')
        self._balance -= amount

    def charge_account(self, amount):
        if not isinstance(amount, int):
            raise AccountValueError('Charge amount must be an integer')
        if amount < 0:
            raise AccountValueError('Charge amount must be > -1')
        if self.balance + amount <= self.acct_limit + 1:
            self._balance += amount

    def change_account_limit(self, new_limit):
        if not isinstance(new_limit, int):
            raise AccountValueError('Account limit must be an integer')
        if new_limit < 0:
            raise AccountValueError('Account limit must be > -1')
        if new_limit > self.balance:
            self.acct_limit = new_limit

    def reset_account(self):
        self.balance = 0


class AccountError(Exception):
    def __init__(self, message):
        self.message = message


class AccountValueError(Exception):
    def __init__(self, message):
        self.message = message
