import pytest
from bank2 import value

def test_value_hello():
    assert value("hello") == 0
    assert value("Hello, Newman") == 0

def test_value_h():
    assert value("Hey") == 20
    assert value("how you doing?") == 20

def test_value_other():
    assert value("What's happening?") == 100