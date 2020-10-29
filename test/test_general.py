from src.code import to_camel_case

#pytest -v test/test_general.py

def test_with_down_slash():
    assert to_camel_case("the_stealth_warrior") == "theStealthWarrior"

def test_with_slash():
    assert to_camel_case("the-stealth-warrior") == "theStealthWarrior"

def test_first_capitalize():
    assert to_camel_case("The-stealth-warrior") == "TheStealthWarrior"

def test_first_not_capitalize():
    assert to_camel_case("the-stealth-warrior") == "theStealthWarrior"

def test_ABC():
    assert to_camel_case("A-B-C") == "ABC"