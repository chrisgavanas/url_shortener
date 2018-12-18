import logging
from bitly_provider import Bitly
from tinyurl_provider import Tinyurl
from validators import validate_provider, validate_url
from exceptions import InvalidUsage
from flask import jsonify
from collections import OrderedDict


provider_mapper = OrderedDict([
    ("bitly", Bitly),
    ("tinyurl", Tinyurl)
    ])


class Provider(object):
    def __init__(self, request):
        self.url = request.json.get('url')
        self.provider_name = request.json.get('provider')
        self.provider_instance = None

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        validate_url(value)
        self._url = value

    @property
    def provider_name(self):
        return self._provider_name

    @provider_name.setter
    def provider_name(self, value):
        if value:
            validate_provider(value, provider_mapper.keys())
            self._provider_name = value
        else:
            self._provider_name = ""

    @property
    def provider_instance(self):
        return self._provider_instance

    @provider_instance.setter
    def provider_instance(self, value):
        if self.provider_name:
            self._provider_instance = provider_mapper.get(self.provider_name)(self.url)

    def shorten(self):
        if self.provider_name:
            return self.form_response(self.provider_instance.shorten())
        return self.provider_picker()

    def provider_picker(self):
        log = logging.getLogger('provider')
        for provider in provider_mapper.keys():
            try:
                return self.form_response(provider_mapper.get(provider)(self.url).shorten())
            except:
                log.warning('{0} is unavailable'.format(provider))
        raise InvalidUsage('All url shortening providers seem unavailable', status_code=409)

    def form_response(self, link):
        return jsonify(dict(url=self.url, link=link))
