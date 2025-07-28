# A2: TDD - check_pwd.py
# Date: 7/28/25
# Author: Jiayi Zhou
# Description: This is the check_pwd function. It checks if the password meets requirements.


# Citation for the following lines:
# Adapted from: https://docs.python.org/3/library/stdtypes.html
def check_pwd(pwd):
    # Check if password is too short (less than 8 characters)
    if len(pwd) < 8:
        return False
    return True
