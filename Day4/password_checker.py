"""
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

How many different passwords within the range given in your puzzle input meet these criteria?
Your puzzle input is 109165-576723.
"""

def is_password_valid(password, minimum_value, maximum_value):
    if not isinstance(password, int):
        #print("\tnot an integer")
        return False

    if password < minimum_value or password > maximum_value:
        #print("\toutside of range")
        return False

    password_digits = [d for d in str(password)]
    ndigits = len(password_digits)
    if ndigits != 6:
        #print("is not 6 digits")
        return False

    multiple_found = False
    idx = 1

    # Check for multiple digits and ensure successive digits are not decreasing.
    while idx < ndigits:
        previous_digit = password_digits[idx - 1]
        current_digit = password_digits[idx]

        if current_digit == previous_digit:
            multiple_found = True
        elif current_digit < previous_digit:
            return False
        idx += 1

    if not multiple_found:
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
    print(f"{len(valid_pswds)} valid passwords")
# end main()


if __name__ == "__main__":
    main()

