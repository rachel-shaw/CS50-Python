import pytest
from fuel2 import convert, gauge

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25

def test_convert_valueerror():
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ValueError):
        convert("1.5/3")

def test_convert_zerodiverror():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(25) == "25%"