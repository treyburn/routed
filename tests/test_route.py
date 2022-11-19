"""Tests for Route module"""
import pytest

from src.route.models import InputDataModel, OutputDataModel, RouteConstraints
from src.route.route import create_route


@pytest.fixture()
def test_matrix() -> InputDataModel:
    """Solveable test matrix"""
    distance_matrix = [
        [0, 2451, 713, 1018, 1631, 1374, 2408, 213, 2571, 875, 1420, 2145, 1972],
        [2451, 0, 1745, 1524, 831, 1240, 959, 2596, 403, 1589, 1374, 357, 579],
        [713, 1745, 0, 355, 920, 803, 1737, 851, 1858, 262, 940, 1453, 1260],
        [1018, 1524, 355, 0, 700, 862, 1395, 1123, 1584, 466, 1056, 1280, 987],
        [1631, 831, 920, 700, 0, 663, 1021, 1769, 949, 796, 879, 586, 371],
        [1374, 1240, 803, 862, 663, 0, 1681, 1551, 1765, 547, 225, 887, 999],
        [2408, 959, 1737, 1395, 1021, 1681, 0, 2493, 678, 1724, 1891, 1114, 701],
        [213, 2596, 851, 1123, 1769, 1551, 2493, 0, 2699, 1038, 1605, 2300, 2099],
        [2571, 403, 1858, 1584, 949, 1765, 678, 2699, 0, 1744, 1645, 653, 600],
        [875, 1589, 262, 466, 796, 547, 1724, 1038, 1744, 0, 679, 1272, 1162],
        [1420, 1374, 940, 1056, 879, 225, 1891, 1605, 1645, 679, 0, 1017, 1200],
        [2145, 357, 1453, 1280, 586, 887, 1114, 2300, 653, 1272, 1017, 0, 504],
        [1972, 579, 1260, 987, 371, 999, 701, 2099, 600, 1162, 1200, 504, 0],
    ]
    num_vehicles = 4
    depot = 0
    return InputDataModel(distance_matrix, num_vehicles, depot)


@pytest.fixture()
def test_constraints() -> RouteConstraints:
    """Valid constraints for use with the `test_matrix` fixture"""
    return RouteConstraints("Distance", 0, 5500)


@pytest.fixture()
def test_constraints_invalid() -> RouteConstraints:
    """Invalid constraints for use with the `test_maxtrix` fixture as
    the capacity is too low"""
    return RouteConstraints("Distance", 0, 50)


def test_create_route(
    test_matrix: InputDataModel, test_constraints: RouteConstraints
) -> None:
    """Positive test case of solvable route"""
    solution = create_route(test_matrix, test_constraints)
    assert solution == [
        OutputDataModel(path=[0, 12, 8, 2, 0], distance=5143),
        OutputDataModel(path=[0, 3, 6, 7, 0], distance=5119),
        OutputDataModel(path=[0, 5, 11, 1, 4, 9, 0], distance=5120),
        OutputDataModel(path=[0, 10, 0], distance=2840),
    ]


def test_create_route_invalid(
    test_matrix: InputDataModel, test_constraints_invalid: RouteConstraints
) -> None:
    """Negative test case of unsolvable route"""
    with pytest.raises(Exception):
        _ = create_route(test_matrix, test_constraints_invalid)


def test_create_route_mokeypatching() -> None:
    # TODO: Implement monkeypatching so we can actually unit test create route
    return