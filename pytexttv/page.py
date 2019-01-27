"""Class to retrieve and represent a page."""
import requests


class Page():
    """Class to store information about a page."""

    def __init__(self, num):
        """Initialize a page."""
        # Request data
        url = 'http://api.texttv.nu/api/get/{0}?app=pytexttv'.format(num)
        response = requests.get(url)

        # Extract data
        data = response.json()[0]
        self._num = int(data['num'])
        self._title = data['title']
        self._content = data['content']

    @property
    def num(self):
        """Return num."""
        return self._num

    @property
    def title(self):
        """Return title."""
        return self._title

    @property
    def content(self):
        """Return content."""
        return self._content
