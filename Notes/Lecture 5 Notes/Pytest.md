
<iframe width="560" height="315" 
src="https://video.cs50.io/6cnpRCUWhMY" 
title="YouTube video player" frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>


```python

"""
Convert Script
"""
def main():
	while True:
		au = input("AU: ")
		try:
			au = float(au)
			break
		except ValueError:
			continue

	print(f"{au} AU is {convert(au)} m")

def convert(au):
	if not isinstance(au, (int, float)):
		raise TypeError("au must be an int or float")
	return au * 149597870700

if __name__ == "__main__":
	main()


"""
TEST Script
"""
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

```