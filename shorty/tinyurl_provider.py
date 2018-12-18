import tinyurl


class Tinyurl:
    def __init__(self, url):
        self.url = url

    def shorten(self):
        return tinyurl.create_one(self.url)
