import re


# region Auth Validators
def validate_email(email):
    return True if re.match("[^@]+@[^@]+\.[^@]+", email) else False


def validate_password(password):
    l, u, d = 0, 0, 0
    if len(password) >= 8:
        for i in password:
            if i.islower():
                l += 1
            if i.isupper():
                u += 1
            if i.isdigit():
                d += 1
    return True if l >= 1 and u >= 1 and d >= 1 and l + u + d == len(password) else False
# endregion Auth Validators


# region Ad Validators
def validate_area(area):
    try:
        if 0 < float(area) < 1000:
            return True
    except ValueError:
        return False


def compare_values(value1, value2):
    return True if float(value1) > float(value2) else False


def validate_price(price):
    try:
        if 0 < float(price) < 100000000:
            return True
    except ValueError:
        return False
# endregion Ad Validators
