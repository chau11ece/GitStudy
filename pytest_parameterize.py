import unittest

import pytest


class MyTestCase():
    def test_something(self):
        assert 1

    def test_setup_fails(self):
        pass

    def test_call_fails(self):
        assert 0

    def test_fail2(self):
        assert 0

    # Hi Chau, something wrong with this testcase; pls help to correct.
    @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
    def test_eval(self, test_input, expected):
        assert eval(test_input) == expected


if __name__ == '__main__':
    unittest.main()
