import sys
from account import Account


class Bank(object):

    def __init__(self):
        bank_accounts = []
        bank_directives = ['Add', 'Charge', 'Credit']

    def validate_input(self, command):



bank_accounts = []


def read_input(source):
    if source == 'stdin':
        while True:
            command = sys.stdin.readline()
            process_command(command)
            if not command:
                break
            sys.stdout.write(command)

def process_command(command):
    split_command = command.split(' ')
    directive = split_command[0]
    if directive == 'Add':
        add_account(split_command)
    elif directive == 'Charge':
        charge_account(split_command)
    elif directive == 'Credit':
        credit_account(split_command)


def add_account(add_command):
    pass


def charge_account(charge_command):
    pass


def credit_account(credit_command):
    pass
