import pytest
import working_hrs_converter

# Testing for correct values:
def test_convert_type1():
    assert working_hrs_converter.convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert working_hrs_converter.convert("1 AM to 9 AM") == "01:00 to 09:00"
    assert working_hrs_converter.convert("9 PM to 5 AM") == "21:00 to 05:00"
    assert working_hrs_converter.convert("4 PM to 12 PM") == "16:00 to 12:00"

# Testing for correct values in different formats
def test_convert_type2():
    assert working_hrs_converter.convert("12:30 AM to 12:00 PM") == "00:30 to 12:00"
    assert working_hrs_converter.convert("3:45 PM to 12 AM") == "15:45 to 00:00"
    assert working_hrs_converter.convert("8 AM to 5:30 PM") == "08:00 to 17:30"

# Testing for incorrect values
def test_convert_type3():
    with pytest.raises(ValueError):
        assert working_hrs_converter.convert("8 am to 5:30 PM")
    with pytest.raises(ValueError):
        assert working_hrs_converter.convert("8 AM to 5:30 pm")
    with pytest.raises(ValueError):
        assert working_hrs_converter.convert("8AM to 5:30 PM")
    with pytest.raises(ValueError):
        assert working_hrs_converter.convert("0 AM To 31:30 PM")
    with pytest.raises(ValueError):
        assert working_hrs_converter.convert("8: AM to 5:30 PM")
    with pytest.raises(ValueError):
        assert working_hrs_converter.convert("8 AM to 5: PM")
    with pytest.raises(ValueError):
        assert working_hrs_converter.convert("15 AM to 17:30 PM")
    with pytest.raises(ValueError):
        assert working_hrs_converter.convert("8 AM to 13:30 PM")
    with pytest.raises(ValueError):
        assert working_hrs_converter.convert("8 AM 5 PM")
    with pytest.raises(ValueError):
        assert working_hrs_converter.convert("8AM 5PM")
    with pytest.raises(ValueError):
        assert working_hrs_converter.convert("8 AM PM")
