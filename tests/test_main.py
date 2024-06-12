"""
This module contains tests for the calculate_and_print function
from the main module.
"""

import pytest
from main import calculate_and_print

# Define test cases for the calculate_and_print function using pytest.mark.parametrize
@pytest.mark.parametrize("operand1_string, operand2_string, operation_string, expected_string", [
    # Test addition
    ("5", "3", 'add', "The result of 5 add 3 is equal to 8"),
    # Test subtraction
    ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"),
    # Test multiplication
    ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"),
    # Test division
    ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5"),
    # Test division by zero
    ("1", "0", 'divide', "An error occurred: Cannot divide by zero"),
    # Test unknown operation
    ("9", "3", 'unknown', "Unknown operation: unknown"),
    # Test invalid operand1 input
    ("operand1", "3", 'add', "Invalid number input: operand1 or 3 is not a valid number."),
    # Test invalid operand2 input
    ("5", "operand2", 'subtract', "Invalid number input: 5 or operand2 is not a valid number.")
])
def test_calculate_and_print(operand1_string, operand2_string, operation_string, expected_string, capsys):
    """
    Test the calculate_and_print function with various inputs and expected outputs.
    
    Parameters:
    - operand1_string: The first operand as a string
    - operand2_string: The second operand as a string
    - operation_string: The operation to perform (add, subtract, multiply, divide, unknown)
    - expected_string: The expected output string
    
    Uses capsys to capture printed output from the calculate_and_print function.
    """
    # Call the function with the provided operands and operation
    calculate_and_print(operand1_string, operand2_string, operation_string)
    # Capture the output printed by the function
    captured = capsys.readouterr()
     # Assert that the captured output matches the expected output
    assert captured.out.strip() == expected_string
