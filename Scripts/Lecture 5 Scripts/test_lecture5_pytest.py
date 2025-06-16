import pytest 
from lecture5 import convert

def test_convert_pos():
    assert convert(1) == 149597870700
    assert convert(2) == 149597870700 * 2
    assert convert(2.5) == 149597870700 * 2.5 #floats can be imprecise depending where cut off
    assert convert(0.001) == pytest.approx(149597870.691) #approx takes into account float imprecision
    assert convert(0.001) == pytest.approx(149597870.691, abs=0.1) #says if answer within +/- 0.1 of expected, allow to pass

def test_convert_neg():
    assert convert(-1) == 149597870700 * -1
    assert convert(-2.5) == 149597870700 * -2.5

def test_convert_zero():
    assert convert(0) == 149597870700 * 0

def test_convert_typeerror():
    with pytest.raises(TypeError):
        convert("cat") #if type in "cat" will raise typeerror

