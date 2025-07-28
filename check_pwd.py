# A2: TDD - check_pwd.py
# Date: 7/28/25
# Author: Jiayi Zhou
# Description: This is the check_pwd function. It checks if the password meets requirements.


# Citation for the following lines:
# Adapted from: https://docs.python.org/3/library/stdtypes.html
# And https://www.guru99.com/test-driven-development.html
def check_pwd(pwd):
    # Check if password is too short (less than 8 characters)
    if len(pwd) < 8:
        return False
    # Check if password is too long (more than 20 characters)
    if len(pwd) > 20:
        return False
    # Check for at least one lowercase letter
    if not any(c.islower() for c in pwd):
        return False
    # Check for at least one uppercase letter
    if not any(c.isupper() for c in pwd):
        return False
    # Check for at least one digit
    if not any(c.isdigit() for c in pwd):
        return False
    # Check for at least one allowed symbol
    allowed_symbols = set("~`!@#$%^&*()_+-=")  # Information from Canvas A2 TDD page
    if not any(c in allowed_symbols for c in pwd):
        return False
    return True
