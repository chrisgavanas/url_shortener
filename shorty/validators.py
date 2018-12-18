from exceptions import InvalidUsage
import re


def validate_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' 
        r'localhost|' 
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' 
        r'(?::\d+)?'  
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if not url:
        raise InvalidUsage('Empty url', status_code=409)
    if not re.match(regex, url):
        raise InvalidUsage('Wrong url format', status_code=409)
    return True


def validate_provider(provider_name, provider_list):
    if provider_name not in provider_list:
        raise InvalidUsage('Wrong provider input', status_code=409)
    return True
