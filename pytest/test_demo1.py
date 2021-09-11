import pytest


@pytest.mark.hoo
def test_m3():
    assert True


def test_m4():
    assert False


@pytest.mark.login
def test_m5():
    assert 10 == 10


def test_m6():
    assert "hello" == "Hello"


def test_m2():
    name = "selenium"
    assert name.upper() == "SeLENIUM"
