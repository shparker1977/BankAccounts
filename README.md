README:

Pre-Requisites:
    - Python3
    - virtualenv

Installation:
    - In program directory run 
	- `virtualenv -p python3 venv`
    	- `source venv/bin/activate`
	- `pip install -r requirements.txt`
    - `python bank_program.py`
	- manual entry of commands
    - `python bank_program.py < input_file.txt`
	- Run program with input file

Language/Tools/Library Choices:
    Python3:  Python3 was chosen because it is capable of providing Object-Oriented paradigms and provides native object inheritance for classes.
    Pip:  pip was chosen for package management for it's ease of use and native integration with python
    Virtualenv: virtualenv was chosen to keep all dependencies local to the project without interfering with python dependencies for other applications.
    luhn python package:  This package was chosen to do the luhn10 validation so that luhn10 validation algorighms would not need to be programmed.

Design choices and tradeoffs:
    Account class (Account.py) 
	The account class was created to simply handle one account.
  		This allows an account to be created for any purpose that adheres to the requirements.
  	There is validation in the account class to protect it's properties from illegal actions.
    Bank class (Bank.py):
	The bank class will handle a dictionary of Accounts.
	The dictionary class will handle KeyValue exceptions for non-existent accounts.
	A custom BankError will be raised if a duplicate account is added to the bank.
    bank_program.py
	The bank_program.py simply runs a loop that accepts bank commands and processes them.
	It processes them through the Bank class for bank actions and the Account class for account actions
	It catches potential errors and handles them accordingly.
    __init__.py:
	__init__.py was created so that these classes can be treated as a module

    Testing:
	- All tests are in the test folder
	- Class tests use the python unittest framework for validation
	- Functional test uses bash for testing (since this will be run from the cli)
	- account_tests.py
		- `python account_test.py`
		- account_tests.py tests the functions and requirements for the Account class
	- bank_test.py
		- `python bank_test.py`
		- bank_test.py tests the functions and requirements of managing accounts through the Bank class
		- erroneous input was not tested in the bank_tests since it is covered in the account tests
	- bank_program_test.sh
		- This is the functional test that tests all of the inputs provided in the requirements
