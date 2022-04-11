
#import pytest


# pytest.fixture to find the fixture whose name matches the argument,
#  passes that return value into our test case

def inc(x):
    return x + 1


def test_answer():
    assert inc(4) == 5

