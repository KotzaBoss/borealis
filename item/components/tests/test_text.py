import pytest

from item.components.text import Text


@pytest.mark.parametrize(
    'txt', [
        'test1',
        'test2',
        "test123",
        "\nnewline\n",
        "tab\ttab"
    ]
)
def test_text(txt):
    t = Text(txt)
    assert t.text == txt
