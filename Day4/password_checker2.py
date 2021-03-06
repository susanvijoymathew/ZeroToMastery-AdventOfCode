"""
Same rules as the previous challenge (password_checker.py). Rules stated here.
Rules for valid password:
    It is a six-digit number.
    The value is within the range given in your puzzle input.
    Two adjacent digits are the same (like 22 in 122345).
    Going from left to right, the digits never decrease; they only ever increase or stay the same
    (like 111123 or 135679).

Other than the range rule, the following are true:
    111111 meets these criteria (double 11, never decreases).
    223450 does not meet these criteria (decreasing pair of digits 50).
    123789 does not meet these criteria (no double).

In addition to the above rules, there should be one group of adjacent digits where the count of the repeating digits
is 2.
    112233 meets this criteria (There are 3 groups in this password: 2 of 1s, 2 of 2s, and 2 of 3s).
    123444 does not meet this criteria (The count for the repeating digit 4 is 3, not 2 and no other repeating  digits
    to take into consideration.
    111122 meets this criteria because it contains double 2.
    111799 meets this criteria because it contains double 9.

How many different passwords within the range given in your puzzle input meet these criteria?
Your puzzle input is 109165-576723.
"""


def is_password_valid(password, minimum_value, maximum_value):
    if not isinstance(password, int):
        return False

    if password < minimum_value or password > maximum_value:
        return False

    password_digits = [d for d in str(password)]
    ndigits = len(password_digits)
    if ndigits != 6:
        return False

    repeating = []
    idx = 1

    # Check for multiple digits and ensure successive digits are not decreasing.
    while idx < ndigits:
        previous_digit = password_digits[idx - 1]
        current_digit = password_digits[idx]

        if current_digit == previous_digit:
            if current_digit not in repeating:
                repeating.append(current_digit)
        elif current_digit < previous_digit:
            return False
        idx += 1

    if not repeating:
        return False
    else:
        group_of_2_only = False
        for s in repeating:
            if password_digits.count(s) == 2:
                group_of_2_only = True

    if not group_of_2_only:
        return False

    return True
# end is_password_valid()


def main():
    minval = 109165
    maxval = 576723
    valid_pswds = []

    for pswd in range(minval, maxval + 1):
        if is_password_valid(pswd, minval, maxval):
            valid_pswds.append(pswd)

    print(valid_pswds)
    print(f"{len(valid_pswds)} valid passwords")  # 1756 is too low
# end main()


if __name__ == "__main__":
    main()

