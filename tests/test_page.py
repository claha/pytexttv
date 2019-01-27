"""Tests related to Page class."""
from pytexttv import Page


def test_page_100():
    """Test to retrieve page 100."""
    page = Page(100)

    assert page.num == 100
    assert page.title != ''
    assert page.content != ''
