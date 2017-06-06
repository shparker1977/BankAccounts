import sys
from account import AccountError, AccountValueError
from bank import Bank, BankError


# split command to directive and parameters
def process_command(command, my_bank):
    split_command = command.split(' ')
    directive = split_command[0]
    account_name = split_command[1]
    if len(split_command) > 2:
        try:
            command_params = [int(x.rstrip()) for x in split_command[2:]]
        except ValueError:
            sys.stdout.write('Invalid input.')
            sys.exit(1)

    if directive == 'Add':
        try:
            my_bank.add_bank_account(account_name, *command_params)
        except KeyError as e:
            sys.stdout.write('Invalid input.')
            sys.exit(1)
        except BankError as e:
            sys.stdout.write('Invalid input.')
            sys.exit(1)
        except AccountError as e:
            sys.stdout.write('Invalid input.')
            sys.exit(1)
    elif directive == 'Charge':
        try:
            my_bank.bank_accounts[account_name].charge_account(*command_params)
        except AccountValueError as e:
            sys.stdout.write('Invalid input.')
            sys.exit(1)
        except KeyError as e:
            sys.stdout.write('Invalid input.')
            sys.exit(1)
    elif directive == 'Credit':
        try:
            my_bank.bank_accounts[account_name].credit_account(*command_params)
        except AccountValueError as e:
            sys.stdout.write('Invalid input.')
            sys.exit(1)
        except KeyError as e:
            sys.stdout.write('Invalid input.')
            sys.exit(1)
    elif directive == 'Reset':
        try:
            my_bank.bank_accounts[account_name].reset_account()
        except KeyError as e:
            sys.stdout.write('Invalid input.')
            sys.exit(1)
    elif directive == 'UpdateLimit':
        try:
            my_bank.bank_accounts[account_name].change_account_limit(*command_params)
        except AccountValueError as e:
            sys.stdout.write('Invalid input.')
            sys.exit(1)
        except KeyError as e:
            sys.stdout.write('Invalid input.')
            sys.exit(1)


def main():

    my_bank = Bank()

    while True:
        try:
            command = sys.stdin.readline().rstrip()
            if command is None or command == '\n' or command == '':
                break
            process_command(command, my_bank)
        except EOFError:
            exit(0)


    my_bank.list_all_accounts()

if __name__ == '__main__':
    main()
