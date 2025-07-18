import pytest
from calc import add, subtract, divide, multiply 

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(2, 4) == 0.5
    assert divide(-1, -1) == 1

def test_multiply():
    assert multiply(5, 3) == 15
    assert multiply(0, 0) == 0
    assert multiply(-1, -1) == 1 
