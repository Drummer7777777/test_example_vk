import pytest


@pytest.mark.parametrize('test_input,expected', [
    (['auto', 'test'], 8),
    (['', 'test'], 4),
    (['auto', ''], 4),
    (['', ''], 0),
    ([25, 25], 4),
    ([25], 2),
    ([], 0),
    ([-2], 2)
])
def test_len_str(test_input, expected):
    try:
        assert sum(map(len, test_input)) == expected
    except TypeError:
        assert sum(map(len, map(str, test_input))) == expected


@pytest.mark.parametrize('test_input,expected', [
    ('auto', 'AUTO'),
    ('Auto', 'AUTO'),
    ('AUTO', 'AUTO')
])
def test_upper_str(test_input, expected):
    assert test_input.upper() == expected


@pytest.mark.parametrize('test_input,expected', [
    ('auto', 'Auto'),
    ('aUto', 'Auto'),
    ('Auto', 'Auto')
])
def test_title_str(test_input, expected):
    assert test_input.title() == expected


@pytest.mark.parametrize('test_input,expected', [
    ([1, 1], 2),
    ([], 0),
    ([1, -1], 0),
    ([-1, -1], -2),
    ([1], 1)
])
def test_sum_int(test_input, expected):
    assert sum(test_input) == expected


@pytest.mark.parametrize('test_input,expected', [
    ([1, 1], 0),
    ([-1], -1),
    ([-1, -1], -2)
])
def test_raz_int(test_input, expected):
    try:
        if test_input[1] < 0:
            assert test_input[0] + test_input[1] == expected
        else:
            assert test_input[0] - test_input[1] == expected
    except IndexError:
        if len(test_input) == 1:
            assert test_input[0] == expected


@pytest.mark.parametrize('test_input,expected', [
    ([2, 2], 4),
    ([0, 0], 1),
    ([2, -2], 0.25),
    ([-2, 2], 4)
])
def test_degree_int(test_input, expected):
    assert test_input[0] ** test_input[1] == expected
