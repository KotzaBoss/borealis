import pytest

from item.components.weight import Pound, Kilogram, Weight

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
def test_weight_int(init, change):
    w = Weight(init)
    assert w.weight == Pound(init)
    w.weight = change
    assert w.weight == Pound(change)


@pytest.mark.parametrize(
    'init, change', values
)
def test_weight_pound(init, change):
    w = Weight(Pound(init))
    assert w.weight == Pound(init)
    w.weight = Pound(change)
    assert w.weight == Pound(change)


@pytest.mark.parametrize(
    'init, change', values
)
def test_weight_kilogram(init, change):
    w = Weight(Kilogram(init))
    assert w.weight == Kilogram(init)
    w.weight = Kilogram(change)
    assert w.weight == Kilogram(change)


@pytest.mark.parametrize(
    'init, change', values
)
def test_weight_kilo_to_pound(init, change):
    w = Weight(Kilogram(init))
    assert w.weight == Kilogram(init)
    w.weight = Pound(change)
    assert w.weight == Pound(change)


@pytest.mark.parametrize(
    'init, change', values
)
def test_weight_pound_to_kilo(init, change):
    w = Weight(Pound(init))
    assert w.weight == Pound(init)
    w.weight = Kilogram(change)
    assert w.weight == Kilogram(change)
