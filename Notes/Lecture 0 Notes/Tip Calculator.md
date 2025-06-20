In the United States, it’s customary to leave a tip for your server after dining in a restaurant, typically an amount equal to 15% or more of your meal’s cost. Not to worry, though, we’ve written a tip calculator for you, below!

```
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO


def percent_to_float(p):
    # TODO


main()
```

Well, we’ve written _most_ of a tip calculator for you. Unfortunately, we didn’t have time to implement two functions:

- `dollars_to_float`, which should accept a `str` as input (formatted as `$##.##`, wherein each `#` is a decimal digit), remove the leading `$`, and return the amount as a `float`. For instance, given `$50.00` as input, it should return `50.0`.
- `percent_to_float`, which should accept a `str` as input (formatted as `##%`, wherein each `#` is a decimal digit), remove the trailing `%`, and return the percentage as a `float`. For instance, given `15%` as input, it should return `0.15`.

Assume that the user will input values in the expected formats.

#### Hints
-  Recall that `input` returns a `str`, per [docs.python.org/3/library/functions.html#input](https://docs.python.org/3/library/functions.html#input).
- Recall that `float` can convert a `str` to a `float`, per [docs.python.org/3/library/functions.html#float](https://docs.python.org/3/library/functions.html#float).
- Recall that a `str` comes with quite a few methods, per [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).

## Demo
```
$ python tip.py
How much was the meal? $50.00
What percentage would you like to tip? 15%
Leave $7.50
$
```

## Before You Begin

Log into [cs50.dev](https://cs50.dev/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

```
$
```

Next execute

```
mkdir tip
```

to make a folder called `tip` in your codespace.

Then execute

```
cd tip
```

to change directories into that folder. You should now see your terminal prompt as `tip/ $`. You can now execute

```
code tip.py
```

to make a file called `tip.py`. Copy and paste the code above into a file, and complete the implementations of `dollars_to_float` and `percent_to_float`, replacing each `TODO` with one or more lines of your own code.

## How to Test

Here’s how to test your code manually:

- Run your program with `python tip.py`. Type `$50.00` and press Enter. Then, type `15%` and press Enter. Your program should output:
    
    ```
    Leave $7.50    
    ```
    
- Run your program with `python tip.py`. Type `$100.00` and press Enter. Then, type `18%` and press Enter. Your program should output:
    
    ```
    Leave $18.00
    ```
    
- Run your program with `python tip.py`. Type `$15.00` and press Enter. Then, type `25%` and press Enter. Your program should output
    
    ```
    Leave $3.75
    ```
    

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

```
check50 cs50/problems/2022/python/tip
```

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

## How to Submit

In your terminal, execute the below to submit your work.

```
submit50 cs50/problems/2022/python/tip
```



### ANSWER

```python
"""
GOALS:
- Implement two functions:
- dollars_to_float, which should accept a str as input (formatted as $##.##); $50.00 as input should return 50.0
- percent_to_float, which should accept a str as input (formatted as ##%); 15% as input should return as 0.15
- Assume the user will input values in the expected formulas
"""  

def main():
	dollars = dollars_to_float(input("How much was the meal? "))
	percent = percent_to_float(input("What percentage would you like to tip? "))
	tip = dollars * percent
	print(f"Leave ${tip:.2f}")
	
	
def dollars_to_float(d):
	d = d.replace("$", "") #to remove $
	return float(d)
	
def percent_to_float(p):
	p = float(p.replace("%", "")) #to remove $
	perc = p /100
	return perc


main()
```