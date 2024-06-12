'''My Calculator Test'''
from decimal import Decimal
import pytest
from calculator.evaluation import Evaluation
from calculator.evaluations import Evaluations
from calculator.operations import add, subtract

@pytest.fixture
def setup_calculations():
    """Clear history and add sample calculations for tests."""
    Evaluations.clear_history()
    Evaluations.add_evaluation(Evaluation(Decimal('10'), Decimal('5'), add))
    Evaluations.add_evaluation(Evaluation(Decimal('20'), Decimal('3'), subtract))

def test_add_calculation(setup_calculations):
    """Test adding a calculation to the history."""
    calc = Evaluation(Decimal('4'), Decimal('4'), add)
    Evaluations.add_evaluation(calc)
    assert Evaluations.get_latest() == calc, "Failed to add the calculation to the history"

def test_get_history(setup_calculations):
    """Test retrieving the entire calculation history."""
    history = Evaluations.get_history()
    assert len(history) == 2, "History does not contain the expected number of evaluations"

def test_clear_history(setup_calculations):
    """Test clearing the entire calculation history."""
    Evaluations.clear_history()
    assert len(Evaluations.get_history()) == 0, "History was not cleared"

def test_get_latest(setup_calculations):
    """Test getting the latest calculation from the history."""
    latest = Evaluations.get_latest()
    assert latest.a
