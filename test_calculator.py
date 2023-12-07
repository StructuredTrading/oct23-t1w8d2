import pytest
from calculator import add, subtract, multiply, divide

def test_basic():
    assert "hello" == "hello"

def test_add():
    assert add(2, 3) == 5
    assert add(0, 20) == 20
    assert add(-5, 3) == -2

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(7, 0) == 7

def test_multiply():
    assert multiply(2, 7) == 14

def test_divide():
    assert divide(50, 10) == 5
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)