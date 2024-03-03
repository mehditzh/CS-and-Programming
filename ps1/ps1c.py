# Problem Set 1 Part C
# Name: <M. Mehdi Taherzadeh>


import numpy as np
import math
import random

tests= [['TEST CASE 1', 'Starting Salary: 150000',
                        'Best Saving Rate: 0.4411',
                        'Steps in Bisection Search: 12'],
        ['TEST CASE 2', 'Starting Salary: 300000',
                        'Best Saving Rate: 0.2206',
                        'Steps in Bisection Search: 9'],
        ['TEST CASE 3', 'Starting Salary: 10000',
                        'It is not possible to pay the down payment in three years']]

for test in tests:
    print('++++++++++++++++++++++++\nFor', test[0], 'use this value as input:\n',
          '     ', test[1])

    # We want to save enough in a certain amount of time (i.e. 36 months).
    # What should be the optimum saving rate to achieve this?
    total_cost = float(1000000)
    annual_salary = float(input("Please enter your annual salary:"))

    portion_down_payment = 0.25 * total_cost
    monthly_salary = annual_salary/12
    current_savings = 0
    r = 0.04
    semi_annual_raise = 0.07


    #calculate final savings with the initialized saving rate


    #print('saving rate is:', portion_saved)
    #print('current savings:', current_savings, 'and down payment is:', portion_down_payment)

    #while not saved enough, add to the months
    months_needed = 36
    portion_saved = portion_down_payment / (36 * monthly_salary)
    steps = 1
    while current_savings < (portion_down_payment - 100) or current_savings > (portion_down_payment + 100):
        current_savings = 0
        annual_salary_1 = annual_salary
        monthly_salary_1 = monthly_salary
        for month in range(1, 37):
            current_savings = current_savings * (1 + r / 12)
            current_savings += portion_saved * monthly_salary_1
            if (month % 6) == 0:
                annual_salary_1 = annual_salary_1 * (1 + semi_annual_raise)
                monthly_salary_1 = annual_salary_1 / 12
        print('>>> step', steps, ': Total savings for down payment with this guess:', current_savings)
        print('    Saving rate', steps, ':', portion_saved)
        if current_savings > (portion_down_payment + 100):
            portion_saved = ((portion_down_payment + 100) / current_savings) * portion_saved
            steps += 1

        elif current_savings < (portion_down_payment - 100):
            portion_saved = ((portion_down_payment - 100) / current_savings) * portion_saved
            steps += 1

    print('------------------------\n>>> The expected output is:')
    for value in test[2:]:
        print('     ', value)
    if portion_saved < 1:
        print('>>> RESULT:'
              '\n      Saving Rate:', (portion_saved // 0.0001) / 10000,
              '\n      Search Steps:', steps)
        #print('current_savings:', current_savings)
    else:
        print('RESULT:'
              '\n      It is not possible to pay the down payment in three years!')