In a file called `plates.py`, reimplement [Vanity Plates](https://cs50.harvard.edu/python/2022/psets/2/plates/) from [Problem Set 2](https://cs50.harvard.edu/python/2022/psets/2/), restructuring your code per the below, wherein `is_valid` still expects a `str` as input and returns `True` if that `str` meets all requirements and `False` if it does not, but `main` is only called if the value of `__name__` is `"__main__"`:

```python
def main():
    ...


def is_valid(s):
    ...


if __name__ == "__main__":
    main()
```

Then, in a file called `test_plates.py`, implement **four or more** functions that collectively test your implementation of `is_valid` thoroughly, each of whose names should begin with `test_` so that you can execute your tests with:

```
pytest test_plates.py
```

#### Hints
- Be sure to include
    ```
    import plates
    ```
    or
    ```
    from plates import is_valid
    ```
    atop `test_plates.py` so that you can call `is_valid` in your tests.
    
- Take care to `return`, not `print`, a `bool` in `is_valid`. Only `main` should call `print`.

## Before You Begin

Log into [cs50.dev](https://cs50.dev/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

```
$
```

Next execute

```
mkdir test_plates
```

to make a folder called `test_plates` in your codespace.

Then execute

```
cd test_plates
```

to change directories into that folder. You should now see your terminal prompt as `test_plates/ $`. You can now execute

```
code test_plates.py
```

to make a file called `test_plates.py` where you’ll write your tests.

## How to Test

To test your tests, run `pytest test_plates.py`. Be sure you have a copy of a `plates.py` file in the same folder. Try to use correct and incorrect versions of `plates.py` to determine how well your tests spot errors:

- Ensure you have a correct version of `plates.py`. Run your tests by executing `pytest test_plates.py`. `pytest` should show that all of your tests have passed.
- Modify the correct version of `plates.py`, perhaps eliminating some of its constraints. Your program might, for example, mistakenly print “Valid” for a license plate of any length! Run your tests by executing `pytest test_plates.py`. `pytest` should show that at least one of your tests has failed.

You can execute the below to check your tests using `check50`, a program CS50 will use to test your code when you submit. (Now there are tests to test your tests!). Be sure to test your tests yourself and determine which tests are needed to ensure `plates.py` is checked thoroughly.

```
check50 cs50/problems/2022/python/tests/plates
```

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

## How to Submit

In your terminal, execute the below to submit your work.

```
submit50 cs50/problems/2022/python/tests/plates
```


### ANSWER
```python
"""
plates2.py
"""
"""
GOALS:
- vanity plates form problem set 2
- is_valid expects a str
- returns True if str meets all requirements
- returns False if not

Requirements:
- start with 2 letters
- max of 6 characters, min of 2
- numbers cannot be in middle of plate
- first number used cannot be 0
- no periods, spaces or punctuation marks
"""


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check length 
    if len(s) < 2 or len(s) > 6:
        return False
    
    # Must start with at least two letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    
     # Only letters and numbers, no punctuation
    if not s.isalnum():
        return False

    number_started = False
    for i, char in enumerate(s):
        if char.isdigit():
            if not number_started:
                number_started = True
                # First number cannot be zero
                if char == '0':
                    return False
            else:
                continue
        else:
            # Numbers cannot appear in the middle of letters
            if number_started:
                return False

    return True

if __name__ == "__main__":
    main()



```

```python
"""
test_plates2.py
"""
import pytest
from plates2 import is_valid

def test_length():
    assert is_valid("CS50") == True
    assert is_valid("H50") == False
    assert is_valid("H") == False
    assert is_valid("CCSPX50") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("CSPX50") == True


def test_beginletters():
    assert is_valid("HH87") == True
    assert is_valid("1000") == False
    assert is_valid("H0SS") == False


def test_punctuation():
    assert is_valid("CS-50") == False
    assert is_valid("PI3.14") == False

def test_first0():
    assert is_valid("01CS") == False
    assert is_valid("CS05") == False

def test_numbersend():
    assert is_valid("AAA100") == True
    assert is_valid("CS50P") == False






```