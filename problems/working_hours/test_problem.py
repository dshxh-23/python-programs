import pytest
from problem import convert

# Testing for correct values:
def test_convert_type1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("1 AM to 9 AM") == "01:00 to 09:00"
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"
    assert convert("4 PM to 12 PM") == "16:00 to 12:00"

# Testing for correct values in different formats
def test_convert_type2():
    assert convert("12:30 AM to 12:00 PM") == "00:30 to 12:00"
    assert convert("3:45 PM to 12 AM") == "15:45 to 00:00"
    assert convert("8 AM to 5:30 PM") == "08:00 to 17:30"

# Testing for incorrect values
def test_convert_type3():
    with pytest.raises(ValueError):
        assert convert("8 am to 5:30 PM")
    with pytest.raises(ValueError):
        assert convert("8 AM to 5:30 pm")
    with pytest.raises(ValueError):
        assert convert("8AM to 5:30 PM")
    with pytest.raises(ValueError):
        assert convert("0 AM To 31:30 PM")
    with pytest.raises(ValueError):
        assert convert("8: AM to 5:30 PM")
    with pytest.raises(ValueError):
        assert convert("8 AM to 5: PM")
    with pytest.raises(ValueError):
        assert convert("15 AM to 17:30 PM")
    with pytest.raises(ValueError):
        assert convert("8 AM to 13:30 PM")
    with pytest.raises(ValueError):
        assert convert("8 AM 5 PM")
    with pytest.raises(ValueError):
        assert convert("8AM 5PM")
    with pytest.raises(ValueError):
        assert convert("8 AM PM")
