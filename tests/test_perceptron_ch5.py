import pytest
import sys
sys.path.append(".")

from bin.perceptron import Perceptron

@pytest.mark.parametrize(
    "training, labels, expected",
    [
        ([[1, 1], [1, 0], [0, 1], [0, 0]], [1, 1, 1, 0], [1, 1, 1, 0]),
        ([[0, 1], [1, 1], [1, 0], [0, 0]], [0, 1, 1, 0], [0, 1, 1, 0]),
        ([[1, 0], [0, 1], [1, 1], [0, 0]], [1, 0, 1, 0], [1, 0, 1, 0]),
    ],
)
def test_perceptron(training, labels, expected):
    the_perceptron = Perceptron()
    the_perceptron.train(training, labels)

    for data_point, expected_result in zip(training, expected):
        assert the_perceptron.predict_function(data_point) == expected_result, f"Failed on data point {data_point}, expected {expected_result}"
