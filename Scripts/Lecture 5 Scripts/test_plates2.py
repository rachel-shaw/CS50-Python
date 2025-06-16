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


