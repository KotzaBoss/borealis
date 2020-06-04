import pytest

from item.components.capacity import Capacity, CubicFeet, CubicMeter
from item.components.weight import Kilogram

values = [
    (1, 5),
    (155, 500),
    (-123, -42),
    (-123, 10),
    (0, 0),
    (-1, 0),
    (1, 0),
    (-56, 56)
]


@pytest.mark.parametrize(
    'init, change', values
)
def test_capacity_int(init, change):
    w = Capacity(init)
    assert w.capacity == init
    w.capacity = change
    assert w.capacity == change


@pytest.mark.parametrize(
    'init, change', values
)
def test_capacity_pound3(init, change):
    w = Capacity(CubicMeter(init))
    assert w.capacity == CubicMeter(init)
    w.capacity = CubicMeter(change)
    assert w.capacity == CubicMeter(change)


@pytest.mark.parametrize(
    'init, change', values
)
def test_capacity_cm3gram(init, change):
    w = Capacity(CubicFeet(init))
    assert w.capacity == CubicFeet(init)
    w.capacity = CubicFeet(change)
    assert w.capacity == CubicFeet(change)


@pytest.mark.parametrize(
    'init, change', values
)
def test_capacity_cm3_to_pound3(init, change):
    w = Capacity(CubicFeet(init))
    assert w.capacity == CubicFeet(init)
    w.capacity = CubicMeter(change)
    assert w.capacity == CubicMeter(change)


@pytest.mark.parametrize(
    'init, change', values
)
def test_capacity_pound3_to_cm3(init, change):
    w = Capacity(CubicMeter(init))
    assert w.capacity == CubicMeter(init)
    w.capacity = CubicFeet(change)
    assert w.capacity == CubicFeet(change)


@pytest.mark.parametrize(
    'init', [
        15.6,
        '1',
        None,
        10
    ]
)
def test_weight_invalid(init):
    if init == 10:
        init = Kilogram(init)
    with pytest.raises(TypeError):
        w = Capacity(init)
