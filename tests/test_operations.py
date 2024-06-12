'''My Calculator Test'''
from decimal import Decimal
import pytest
from calculator.evaluation import Evaluation
from calculator.operations import add, subtract, multiply, divide

def test_operation_add():
    """Test adding a calculation to the history."""
    evaluation = Evaluation(Decimal('11'), Decimal('9'), add)
    assert evaluation.perform() == Decimal('20'), "Add operation failed"

def test_operation_subtract():
    """Test subtracting a calculation to the history."""
    evaluation = Evaluation(Decimal('5'), Decimal('5'), subtract)
    assert evaluation.perform() == Decimal('0'), "Subtract operation failed"

def test_operation_multiply():
    """Test multiplying a calculation to the history."""
    evaluation = Evaluation(Decimal('5'), Decimal('5'), multiply)
    assert evaluation.perform() == Decimal('25'), "Multiply operation failed"

def test_operation_divide():
    """Test adding division to the history."""
    evaluation = Evaluation(Decimal('10'), Decimal('5'), divide)
    assert evaluation.perform() == Decimal('2'), "Divide operation failed"

def test_divide_by_zero():
    """Test adding divide by zero to the history."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        evaluation = Evaluation(Decimal('10'), Decimal('0'), divide)
        evaluation.perform()
