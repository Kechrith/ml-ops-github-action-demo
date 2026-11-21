import pytest
from model import predict_sales


def test_prediction():
    assert predict_sales(100) == 250


def test_zero_budget():
    assert predict_sales(0) == 0


def test_negative_budget():
    with pytest.raises(ValueError):
        predict_sales(-10)
