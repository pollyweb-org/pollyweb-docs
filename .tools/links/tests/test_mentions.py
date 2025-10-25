import sys
import pathlib
import pytest

# Ensure the link_replacements package is importable when running tests directly.
ROOT = pathlib.Path(__file__).resolve().parents[1]  # .tools/links
sys.path.insert(0, str(ROOT))

from link_replacements.mentions import format_dynamic_link_text


@pytest.mark.parametrize(
    "token,expected",
    [
        ("Assess handler", "`Assess` 📃 handler"),
        ("DoSomething script", "`DoSomething` 📃 script"),
        ("Consume flow", "`Consume` ⏩ flow"),
        ("Items table", "`Items` 🪣 table"),
    ],
)
def test_format_dynamic_link_text_special_tokens(token, expected):
    assert format_dynamic_link_text(token) == expected


def test_format_dynamic_link_text_triple_brace():
    assert format_dynamic_link_text("X Y", triple_brace=True) == "`{X Y}`"
