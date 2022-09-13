import pytest


# @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [
    ([1, 2, 3], 6),
    ([5, 6, 7], 10),
])
def test_sum(test_input, expected):
    assert sum(test_input) == expected