import pytest
import ast
import importlib

# Test to check for file docstring
def test_file_docstring():
    with open('assignment.py', 'r') as file:
        tree = ast.parse(file.read())
    docstring = ast.get_docstring(tree)
    assert docstring is not None, "DMACC Student, there does not appear to be a docstring at the top of your file. Please add a docstring explaining what your code does."

# Test to verify _initialize_dictionary to expected outcome
def test_initialize_dictionary():
    from assignment import _initialize_dictionary
    expected = {
        "juan": "708-555-9878",
        "michael": "630-555-0009",
        "steve": "630-555-1112",
        "jimmy": "515-555-9999",
        "tony": "847-555-4443",
        "merle": "312-555-9823",
        "willie": "414-555-6767"
    }
    result = _initialize_dictionary()
    assert result == expected, f"DMACC Student, the function '_initialize_dictionary' did not return the expected dictionary.\nExpected: {expected}\nActual: {result}\nPlease check your dictionary initialization logic."

# Tests for create_new_name_and_number
def test_create_new_name_and_number_happy_path(monkeypatch):
    from assignment import create_new_name_and_number, _initialize_dictionary
    a_dict = _initialize_dictionary()
    inputs = iter(["john", "515-555-1234"])
    try:
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        create_new_name_and_number(a_dict)
        expected = "515-555-1234"
        assert a_dict["john"] == expected, f"DMACC Student, the function 'create_new_name_and_number' did not add the expected key:value pair.\nExpected: 'john': '{expected}'\nActual: 'john': '{a_dict['john']}'\nPlease check your input handling and dictionary update logic."
    except TypeError:
        assert False == True, f"DMACC Student, this may be failing if you have something like name=input() with no words in input()"

def test_create_new_name_and_number_invalid_then_happy_path(monkeypatch):
    from assignment import create_new_name_and_number, _initialize_dictionary
    a_dict = _initialize_dictionary()
    inputs = iter(["juan", "john", "515-555-1234"])
    try:
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        create_new_name_and_number(a_dict)
        expected = "515-555-1234"
        assert a_dict["john"] == expected, f"DMACC Student, the function 'create_new_name_and_number' did not add the expected key:value pair after invalid input.\nExpected: 'john': '{expected}'\nActual: 'john': '{a_dict['john']}'\nPlease check your input handling and dictionary update logic."
    except TypeError:
        assert False == True, f"DMACC Student, this may be failing if you have something like name=input() with no words in input()"

# Tests for update_phone_number
def test_update_phone_number_happy_path(monkeypatch):
    from assignment import update_phone_number, _initialize_dictionary
    a_dict = _initialize_dictionary()
    inputs = iter(["juan", "515-555-4321"])
    try:
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        update_phone_number(a_dict)
        expected = "515-555-4321"
        assert a_dict["juan"] == expected, f"DMACC Student, the function 'update_phone_number' did not update the expected key:value pair.\nExpected: 'juan': '{expected}'\nActual: 'juan': '{a_dict['juan']}'\nPlease check your input handling and dictionary update logic."
    except TypeError:
        assert False == True, f"DMACC Student, this may be failing if you have something like name=input() with no words in input()"

def test_update_phone_number_invalid_then_happy_path(monkeypatch):
    from assignment import update_phone_number, _initialize_dictionary
    a_dict = _initialize_dictionary()
    inputs = iter(["john", "juan", "515-555-4321"])
    try:
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        update_phone_number(a_dict)
        expected = "515-555-4321"
        assert a_dict["juan"] == expected, f"DMACC Student, the function 'update_phone_number' did not update the expected key:value pair after invalid input.\nExpected: 'juan': '{expected}'\nActual: 'juan': '{a_dict['juan']}'\nPlease check your input handling and dictionary update logic."
    except TypeError:
        assert False == True, f"DMACC Student, this may be failing if you have something like name=input() with no words in input()"

if __name__ == "__main__":
    pytest.main()