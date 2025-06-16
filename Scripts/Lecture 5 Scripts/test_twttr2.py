import pytest
from twttr2 import shorten

def test_case():
    assert shorten("hello") == "hll"
    assert shorten("CS50") == "CS50"
    assert shorten("Where are you?") == "Whr r y?"
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"