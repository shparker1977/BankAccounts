#!/bin/sh


##### Test 1 ####
echo "Add John 4375751593 1000
Charge John 100
Add Maddy 2927642419 1000
Credit Maddy 300
Credit John 50
Charge Maddy 50" > input_file.txt

expected_output="John, 4375751593: 50
Maddy, 2927642419: -250"
output=$(python ../bank_program.py < input_file.txt)

if [ "$output" == "$expected_output" ]; then
    echo "Test 1 passed"
else
    echo "Test 1 failed"
fi


##### Test 2 ####
echo "Add Jamie 2927642419 1000
Charge Jamie 1001
Charge Jamie 5" > input_file.txt

expected_output="Jamie, 2927642419: 5"
output=$(python ../bank_program.py < input_file.txt)

if [ "$output" == "$expected_output" ]; then
    echo "Test 2 passed"
else
    echo "Test 2 failed"
fi


##### Test 3 ####
echo "Add Alice 9771351039 450
Credit Alice 175
Reset Alice
Charge Alice 100" > input_file.txt

expected_output="Alice, 9771351039: 100"
output=$(python ../bank_program.py < input_file.txt)

if [ "$output" == "$expected_output" ]; then
    echo "Test 3 passed"
else
    echo "Test 3 failed"
fi


##### Test 4 ####
echo "Add Alice 9771351039 450
Charge Alice 999
UpdateLimit Alice 1000
Charge Alice 1000" > input_file.txt

expected_output="Alice, 9771351039: 1000"
output=$(python ../bank_program.py < input_file.txt)

if [ "$output" == "$expected_output" ]; then
    echo "Test 4 passed"
else
    echo "Test 4 failed"
fi


##### Test 5 ####
echo "Add Vsevolodovich 123123123 1000
Charge Vsevolodovich 100" > input_file.txt

expected_output="Invalid input."
output=$(python ../bank_program.py < input_file.txt)

if [ "$output" == "$expected_output" ]; then
    echo "Test 5 passed"
else
    echo "Test 5 failed"
fi


##### Test 6 ####
echo "Add Vsevolodovich 9771351039 1000
Charge Bill 100" > input_file.txt

expected_output="Invalid input."
output=$(python ../bank_program.py < input_file.txt)

if [ "$output" == "$expected_output" ]; then
    echo "Test 6 passed"
else
    echo "Test 6 failed"
fi


##### Test 7 ####
echo "Add Charles 555635394664 500
Charge Charles -500" > input_file.txt

expected_output="Invalid input."
output=$(python ../bank_program.py < input_file.txt)

if [ "$output" == "$expected_output" ]; then
    echo "Test 7 passed"
else
    echo "Test 7 failed"
fi


##### Test 8 ####
echo "Add Alice 9771351039 450
Credit Alice four-hundred" > input_file.txt

expected_output="Invalid input."
output=$(python ../bank_program.py < input_file.txt)

if [ "$output" == "$expected_output" ]; then
    echo "Test 8 passed"
else
    echo "Test 8 failed"
fi

rm input_file.txt