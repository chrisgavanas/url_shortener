from bitly_api import bitly_api


class Bitly:
    def __init__(self, url):
        self.url = url

    def shorten(self):
        connection = bitly_api.Connection(access_token='356db55c276e2825fedbde89a0c35385430218ae')
        return connection.shorten(self.url)['url']