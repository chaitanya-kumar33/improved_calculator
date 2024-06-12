'''My Calculator Test'''
from decimal import Decimal
import pytest
from calculator.evaluation import Evaluation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("a_, b_, operation, expected", [
    (Decimal('15'), Decimal('3'), add, Decimal('18')),
    (Decimal('20'), Decimal('10'), subtract, Decimal('10')),
    (Decimal('7'), Decimal('3'), multiply, Decimal('21')),
    (Decimal('12'), Decimal('4'), divide, Decimal('3')),
    (Decimal('10.5'), Decimal('2.5'), add, Decimal('13.0')),
    (Decimal('10.5'), Decimal('0.5'), subtract, Decimal('10.0')),
    (Decimal('7.5'), Decimal('3'), multiply, Decimal('22.5')),
    (Decimal('12'), Decimal('2'), divide, Decimal('6')),
])
def test_evaluation_operations(a_, b_, operation, expected):
    """
    Test calculation operations with various scenarios.
    
    This test ensures that the Calculation class correctly performs the arithmetic operation
    (specified by the 'operation' parameter) on two Decimal operands ('a' and 'b'),
    and that the result matches the expected outcome.
    
    Parameters:
        a (Decimal): The first operand in the calculation.
        b (Decimal): The second operand in the calculation.
        operation (function): The arithmetic operation to perform.
        expected (Decimal): The expected result of the operation.
    """
    eval_instance = Evaluation(a_, b_, operation)
    assert eval_instance.perform() == expected, f"Failed {operation.__name__} operation with {a_} and {b_}"

def test_evaluation_repr():
    """
    Test the string representation (__repr__) of the Calculation class.
    
    This test verifies that the __repr__ method of a Calculation instance returns a string
    that accurately represents the state of the Calculation object, including its operands and operation.
    """
    eval_instance = Evaluation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Evaluation(10, 5, add)"
    assert repr(eval_instance) == expected_repr, "The __repr__ method output does not match the expected string."

def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ValueError.
    
    This test checks that attempting to perform a division operation with a zero divisor
    correctly raises a ValueError, as dividing by zero is mathematically undefined and should be handled as an error.
    """
    eval_instance = Evaluation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        eval_instance.perform()
