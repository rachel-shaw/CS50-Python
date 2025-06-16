Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called `fuel.py`, implement a program that prompts the user for a fraction, formatted as `X/Y`, wherein each of `X` and `Y` is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output `E` instead to indicate that the tank is essentially empty. And if 99% or more remains, output `F` instead to indicate that the tank is essentially full.

If, though, `X` or `Y` is not an integer, `X` is greater than `Y`, or `Y` is `0`, instead prompt the user again. (It is not necessary for `Y` to be `4`.) Be sure to catch any exceptions like [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError) or [`ZeroDivisionError`](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError).

#### Hints
- Recall that a `str` comes with quite a few methods, per [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods), including `split`.
- Note that you can handle two exceptions separately with code like:
    
    ```python
    try:
        ...
    except ValueError:
        ...
    except ZeroDivisionError:
        ...
    ```
    
    Or you can handle two exceptions together with code like:
    
    ```python
    try:
        ...
    except (ValueError, ZeroDivisionError):
        ...
    ```

## Demo
```
$ python fuel.py
Fraction: cat/dog
Fraction: 1/4
25%
$ python fuel.py
Fraction: 1/2
50%
$ python fuel.py
Fraction: 3/4
75%
$ python fuel.py
Fraction: 4/4
F
$ python fuel.py
Fraction: 1/0
Fraction: 0/1
E
$
```

## Before You Begin

Log into [cs50.dev](https://cs50.dev/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

```
$
```

Next execute

```
mkdir fuel
```

to make a folder called `fuel` in your codespace.

Then execute

```
cd fuel
```

to change directories into that folder. You should now see your terminal prompt as `fuel/ $`. You can now execute

```
code fuel.py
```

to make a file called `fuel.py` where you’ll write your program.

## How to Test

Here’s how to test your code manually:

- Run your program with `python fuel.py`. Type `3/4` and press Enter. Your program should output:
    
    ```
    75% 
    ```
    
- Run your program with `python fuel.py`. Type `1/4` and press Enter. Your program should output:
    
    ```
    25%
    ```
    
- Run your program with `python fuel.py`. Type `4/4` and press Enter. Your program should output:
    
    ```
    F
    ```
    
- Run your program with `python fuel.py`. Type `0/4` and press Enter. Your program should output:
    
    ```
    E
    ```
    
- Run your program with `python fuel.py`. Type `4/0` and press Enter. Your program should handle a [`ZeroDivisionError`](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError) and prompt the user again.
- Run your program with `python fuel.py`. Type `three/four` and press Enter. Your program should handle a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError) and prompt the user again.
- Run your program with `python fuel.py`. Type `1.5/3` and press Enter. Your program should handle a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError) and prompt the user again.
- Run your program with `python fuel.py`. Type `5/4` and press Enter. Your program should prompt the user again.

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

```
check50 cs50/problems/2022/python/fuel
```

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

## How to Submit

In your terminal, execute the below to submit your work.

```
submit50 cs50/problems/2022/python/fuel
```



### ANSWER
```python
"""
GOALS:
- implement a program that prompts the user for a fraction
- formatted as X/Y (both int)
- outputs as percent rounded to nearest integer
- If 1% or less remains, output E for empty
- if 99% or more remains, output F for full
- If x or y is not an int, x is greater than y, or y is 0, instead prompt user again
- be sure to catch any exceptions like ValueError or ZeroDivisionError
"""

def main():
	answer = get_answer()

	if 100 >= answer >= 99:
		print("F")
	elif answer <= 1:
		print("E")
	else:
		print(f"{int(answer)}%")


def get_answer():
	while True:
		try:
			userentry = input("Fraction: ")
			x,y = userentry.split("/")
			answer = int(x)/int(y)*100
			
			if answer > 100:
				continue
			return answer
	except ValueError:
		pass
	except ZeroDivisionError:
		pass

  
  

main()

```