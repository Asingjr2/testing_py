"""Working through pytest tutorial examples.

All test can be run with cmd line pytest.  Requires test to start with 'test'.
Third party library uses basic assert statement.

Pytest allows test to pass if validation is address when testing against errors
(e.g. type check for number vs string).

"""
import pytest

def capital(letters):
    if not isinstance(letters, str):
        raise TypeError("Please enter a string.")
    return letters.capitalize()

def test_capital():
    assert capital('cat') == 'Cat'
    # assert capital_case('cat') == 'Cat'   line would fail

def test_raises_non_string_error():
    """Function that works with type errors for addtional validation and passes if check in original function."""
    with pytest.raises(TypeError):
        capital(51)
