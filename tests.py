# A2: TDD - tests.py
# Date: 7/28/25
# Author: Jiayi Zhou
# Description: This is the unit test file for the check_pwd module, with TDD process.

import unittest
from check_pwd import check_pwd  #check_pwd is requirement in Canvas explanation


# Citation for the following lines:
# Adopted from: https://docs.python.org/3/library/stdtypes.html
class TestCheckPwd(unittest.TestCase):
    def test_short_password(self):
        """Test that passwords shorter than 8 characters are rejected"""
        self.assertFalse(check_pwd("Zx12!"))  # 5 characters

    def test_long_password(self):
        """Test that passwords longer than 20 characters are rejected"""
        self.assertFalse(check_pwd("Z" * 19 + "x1!"))  # 23 characters

    def test_no_lowercase(self):
        """Test that passwords without lowercase letters are rejected"""
        self.assertFalse(check_pwd("ZXCVBNM1!"))  # valid length, no lowercase

    def test_no_uppercase(self):
        """Test that passwords without uppercase letters are rejected"""
        self.assertFalse(check_pwd("zxcvbnm1!"))  # valid length, no uppercase


if __name__ == "__main__":
  unittest.main()
