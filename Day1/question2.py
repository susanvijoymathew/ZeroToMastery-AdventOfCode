"""
Continuation of question 1.
Once the initial fuel is calculated, calculate the fuel requirements for it. Continue doing this until you get 0 or
negative fuel as a result. Total up all the calculated fuel requirements and that is the final answer for a mass module.

So, for each module mass, calculate its fuel and add it to the total. Then, treat the fuel amount you just calculated
as the input mass and repeat the process, continuing until a fuel requirement is zero or negative. For example:

    * A module of mass 14 requires 2 fuel. This fuel requires no further fuel (2 divided by 3 and rounded down is 0,
    which would call for a negative fuel), so the total fuel required is still just 2.
    * At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2). 216 then
    requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, which requires no further fuel. So, the total
    fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
    * The fuel required by a module of mass 100756 and its fuel is: 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 +
    2 = 50346.

What is the sum of the fuel requirements for all of the modules on your spacecraft when also taking into account the
mass of the added fuel? (Calculate the fuel requirements for each module separately, then add them all up at the end.)

Module mass input is as same as question 1.
"""

"""
NOTE about importing modules. Reference:
https://stackoverflow.com/questions/41816973/modulenotfounderror-what-does-it-mean-main-is-not-a-package

The core issue I think is when you import with a dot:
    from .p_02_paying_debt_off_in_a_year import compute_balance_after
It is equivalent to:
    from __main__.p_02_paying_debt_off_in_a_year import compute_balance_after
where __main__ refers to your current module p_03_using_bisection_search.py.

So, omit the dot when importing a file from the current directory.
MUST have an __init__.py for your files to become modules and __init__.py can be empty.
"""

import question1

def calculate_full_fuel_requirement(module_mass):
    result = question1.calculate_fuel_requirement(module_mass)
    if result <= 0:
        return 0
    return result + calculate_full_fuel_requirement(result)


full_fuel_list = []
for mass in question1.module_mass_list:
    full_fuel_list.append(calculate_full_fuel_requirement(mass))

print(question1.totalUp(full_fuel_list))