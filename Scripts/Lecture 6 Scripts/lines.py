"""
GOALS:
- implement a program that expects exactly one command-line argument, the name or path of a python file
- outputs the number of lines of code in that file
- excluding comments and blank lines
- exit via sys.exit if:
    - if user does not specify exactly one command-line argument
    - if user does not end in .py
    - if files does not exist
- assume any line that starts with # is a comment
"""

