from shorty import validators
from shorty.exceptions import InvalidUsage
from shorty.provider import provider_mapper
import pytest


valid_url = "http://www.google.com"
invalid_format = "wrongformat"
invalid_protocol = "odbc://www.google.com"
invalid_ip = "257.257.257.257"

valid_provider = "bitly"
invalid_provider = "other"


def test_validate_url_valid():
    assert validators.validate_url(valid_url)


def test_validate_provider_valid():
    assert validators.validate_provider(valid_provider, provider_mapper.keys())


def test_validate_url_invalid_format():
    with pytest.raises(InvalidUsage) as invalid_usage:
        validators.validate_url(invalid_format)
    assert invalid_usage.value.status_code == 409
    assert invalid_usage.value.message == 'Wrong url format'


def test_validate_url_invalid_protocol():
    with pytest.raises(InvalidUsage) as invalid_usage:
        validators.validate_url(invalid_protocol)
    assert invalid_usage.value.status_code == 409
    assert invalid_usage.value.message == 'Wrong url format'


def test_validate_url_invalid_ip():
    with pytest.raises(InvalidUsage) as invalid_usage:
        validators.validate_url(invalid_ip)
    assert invalid_usage.value.status_code == 409
    assert invalid_usage.value.message == 'Wrong url format'


def test_validate_provider_invalid_provider():
    with pytest.raises(InvalidUsage) as invalid_usage:
        validators.validate_provider(invalid_provider, provider_mapper.keys())
    assert invalid_usage.value.status_code == 409
    assert invalid_usage.value.message == 'Wrong provider input'




