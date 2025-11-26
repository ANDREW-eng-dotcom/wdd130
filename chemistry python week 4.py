def test_make_periodic_table():
    """verify that the make_periodic_table function works correctly,
    parameters:none
    return:nothing
    """
    #call the make_periodic_table function and store the returned
    #dictionary in a variable named periodic_table_dict.
    periodic_table_dict = make_periodic_table()
    
    #verify that the make_periodic_table function returns a dictionary.
    assert isinstance(periodic_table_dict,dict),\
        "make_periodic_table function must return a dictionary:"\
            f"expected a dictionary but found a {type(periodic_table_dict)}"
            
    # check each item in the periodic table dictionary.
    check_element(periodic_table_dict,"H",["Hydrogen", 1.00794])
    check_element(periodic_table_dict,"O",["Oxygen", 15.9994])
    check_element(periodic_table_dict,"C",["Carbon", 12.0107])
    check_element(periodic_table_dict,"Na",["Sodium", 22.98976928])
    check_element(periodic_table_dict,"Cl",["Chlorine", 35.453])
    # Add more check_element calls as needed, but ensure the elements exist in make_periodic_table
# Define index constants for element properties
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

from math import isclose

def check_element(periodic_table_dict,symbol,expected):
    """Verify that the actual element that came from the
    periodic_table_dict contains the same values as the expected element.
    parameters
        symbol:a symbol for a chemical element
        expected:a list that contains the expected values for symbol
        Return:nothing
    """
    #Verify that symbol is in the periodic table dictionary.
    assert symbol in periodic_table_dict,\
        f'"{symbol}" is missing from the periodic table dictionary.'
    actual=periodic_table_dict[symbol]
    
    #verify that the element's name is correct.
    act_name=actual[NAME_INDEX]
    exp_name=expected[NAME_INDEX]
    assert act_name==exp_name,\
        f'wrong name for "{symbol}":'\
        f'expected {exp_name} but found{act_name}'
        
    #verify that the element's atomic mass is correct.
    act_mass = actual[ATOMIC_MASS_INDEX]
    exp_mass = expected[ATOMIC_MASS_INDEX]
    assert isclose(act_mass, exp_mass, rel_tol=1e-5),\
        f"wrong atomic mass for {exp_name}"\
        f"expected {exp_mass} but found {act_mass}"
            
            
class FormulaError(Exception):
    """Custom exception for invalid chemical formulas."""
    pass

def parse_formula(formula, periodic_table_dict):
    """
    Parses a chemical formula and returns a list of tuples (symbol, quantity).
    This is a simple implementation for demonstration purposes.
    """
    import re
    pattern = r'([A-Z][a-z]?)(\d*)'
    matches = re.findall(pattern, formula)
    result = []
    for (symbol, qty) in matches:
        qty = int(qty) if qty else 1
        result.append((symbol, qty))
    return result

def make_periodic_table():
    """Return a dictionary representing a simplified periodic table."""
    return {
        "H": ["Hydrogen", 1.00794],
        "O": ["Oxygen", 15.9994],
        "C": ["Carbon", 12.0107],
        "Na": ["Sodium", 22.98976928],
        "Cl": ["Chlorine", 35.453],
        # Add more elements as needed for your tests
    }

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """
    Compute the molar mass of a compound given a list of (symbol, quantity) pairs and a periodic table dictionary.
    """
    total_mass = 0
    for symbol, quantity in symbol_quantity_list:
        if symbol not in periodic_table_dict:
            raise FormulaError(f"Element symbol '{symbol}' not found in periodic table.")
        atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]
        total_mass += atomic_mass * quantity
    return total_mass

def test_parse_formula():
    """verify that the parse_formula function works correctly.
    parameters:none
    Return:nothing
    """
    # Call the make_periodic_table function
    # and verify that it returns a dictionary.
    periodic_table_dict = make_periodic_table()
    assert isinstance(periodic_table_dict, dict),\
        "make_periodic_table function must return a dictionary:"\
         f"expected a dictionary but found a {type(periodic_table_dict)}"
         
    # Call the parse_formula function and
    # verify that it returns a list.
    sym_quant_list = parse_formula("H20",periodic_table_dict)
    assert isinstance(sym_quant_list,list),\
        "parse_formula function must return a list:"\
        f"expected a list but found a {type(sym_quant_list)}"
        
    # call the compute_molar_mass function four times and 
    # verify that it returns the correct number each time.
    assert parse_formula("H2O",periodic_table_dict) == [("H",2),("O",1)]
    assert parse_formula("C6H6",periodic_table_dict) == [("C",6),("H",6)]
    assert parse_formula("(C2(NaCl)4H2)2C4Na",periodic_table_dict) == [("C",8),("Na",9),("Cl",8),("H",4)]

# call the parse_formula function six times,each time
# with a different invalid chemical formula.verify that 
# parse_formula function raises an exception each time
periodic_table_dict = make_periodic_table()
import pytest
with pytest.raises(FormulaError):
    parse_formula("L", periodic_table_dict)
with pytest.raises(FormulaError):
    parse_formula("4H", periodic_table_dict)
with pytest.raises(FormulaError):
    parse_formula("H2L4", periodic_table_dict)
with pytest.raises(FormulaError):
    parse_formula("-H", periodic_table_dict)
with pytest.raises(FormulaError):
    parse_formula("H2O", periodic_table_dict)
with pytest.raises(FormulaError):
    parse_formula("H2)O3", periodic_table_dict)
                                                                 
def test_compute_molar_mass():
    """verify that the compute_molar_mass function works correctly.
    Parameters:none
    return:nothing
    """    
    
    #call the make_periodic_table function
    #and verify that it returns a dictionary.
def parse_formula(formula, periodic_table_dict):
    """
    Parses a chemical formula and returns a list of tuples (symbol, quantity).
    This is a simple implementation for demonstration purposes.
    Raises FormulaError for invalid formulas.
    """
    import re
    if not formula or not re.match(r'^[A-Za-z0-9()]+$', formula):
        raise FormulaError("Invalid formula format.")
    pattern = r'([A-Z][a-z]?)(\d*)'
    matches = re.findall(pattern, formula)
    if not matches:
        raise FormulaError("Invalid formula format.")
    result = []
def make_periodic_table():
    """Return a dictionary representing a simplified periodic table."""
    return {
        "H": ["Hydrogen", 1.00794],
        "O": ["Oxygen", 15.9994],
        "C": ["Carbon", 12.0107],
        "Na": ["Sodium", 22.98976928],
        "Cl": ["Chlorine", 35.453],
        "He": ["Helium", 4.002602],
        "N": ["Nitrogen", 14.0067],
        "S": ["Sulfur", 32.065],
        # Add more elements as needed for your tests
    }

# The following test code should be outside of any function definition
from pytest import approx
periodic_table_dict = make_periodic_table()
assert compute_molar_mass([["C",13],["H",16],["O",2]],periodic_table_dict) == approx(232.27834)

# call the main function that is part of pytest so that the 
# computer will execute the test functions in this file.
import sys
import pytest
pytest.main(["-v","--tb=line","-rN",sys.argv[0]])
    
    # (Removed duplicate and incorrectly indented test_parse_formula function)
