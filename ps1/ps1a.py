# Problem Set 1 part A
# Name: <M. Mehdi Taherzadeh>


import numpy as np
import math
import random

tests = [['TEST CASE 1', 'Cost of Your Dream Home: 1000000',
                        'Starting Annual Salary: 120000',
                        'Percernt of Your Salary to Save, as a Decimal: 0.10', 183],
        ['TEST CASE 2', 'Cost of Your Dream Home: 500000',
                        'Starting Annual Salary: 80000',
                        'Percernt of Your Salary to Save, as a Decimal: 0.15', 105]]



for test in tests:
    print('++++++++++++++++++++++++\nFor', test[0], 'use these inputs:')
    for value in test[1:-1]:
        print('    ', value)
    print('-----------------------')

    # The parameters specified by the user
    total_cost = float(input("Please enter the total cost of your dream home:"))
    annual_salary = float(input("Please enter your annual salary:"))
    portion_saved = float(input("Please enter the portion of salary to be saved:"))

    # The initialized parameters
    portion_down_payment = 0.25 * total_cost
    monthly_salary = annual_salary / 12
    current_savings = 0
    r = 0.04

    months_needed = 0
    #while not saved enough, add to the months
    while current_savings < portion_down_payment:
        current_savings = current_savings * (1 + r / 12)
        current_savings += portion_saved * monthly_salary
        months_needed +=1
        if (months_needed % 6) == 0:
            monthly_salary = annual_salary / 12

    if test[-1] == months_needed:
        print('-----------------------\nCORRECT! Your result matches the expected output output')
    else:
        print('-----------------------\nOops! Something went wrong, your reslut does not match the expected output')
    print('The Expected output for', test[0], 'is:', test[-1],
          '\nRESULT ---> Number of months needed to save money for your dream home:', months_needed)
