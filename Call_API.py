# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import json
import logging
import requests
from datetime import datetime


class ConnectionError(Exception):
    def __init__(self, response, content=None, message=None):
        self.response = response
        self.content = content
        self.message = message

    def __str__(self):
        message = "Failed."
        if hasattr(self.response, 'status_code'):
            message += " Response status:{status_code}.".format(
                status_code=self.response.status_code)
        if hasattr(self.response, 'reason'):
            message += " Response message:{reason}.".format(
                reason=self.response.reason)
        if self.content is not None:
            message += " Error message: " + self.content
        return message


class Redirection(ConnectionError):
    """3xx Redirection
    """

    def __str__(self):
        message = super(Redirection, self).__str__()
        if self.response.get('Location'):
            message = "{message} => {location}".format(
                message=message, location=self.response.get('Location'))
        return message


class MissingParam(TypeError):
    pass


class MissingConfig(Exception):
    pass


class ClientError(ConnectionError):
    """4xx Client Error
    """
    pass


class BadRequest(ClientError):
    """400 Bad Request
    """
    pass


class UnauthorizedAccess(ClientError):
    """401 Unauthorized
    """
    pass


class ForbiddenAccess(ClientError):
    """403 Forbidden
    """
    pass


class ResourceNotFound(ClientError):
    """404 Not Found
    """
    pass


class ResourceConflict(ClientError):
    """409 Conflict
    """
    pass


class ResourceGone(ClientError):
    """410 Gone
    """
    pass


class ResourceInvalid(ClientError):
    """422 Invalid
    """
    pass


class ServerError(ConnectionError):
    """5xx Server Error
    """
    pass


class MethodNotAllowed(ClientError):
    """405 Method Not Allowed
    """

    def allowed_methods(self):
        return self.response['Allow']


class ApiClient(object):

    def __init__(self, api_url):
        self._api_host = api_url

    @staticmethod
    def _merge_dict(data, *override):
        result = {}
        for current_dict in (data,) + override:
            result.update(current_dict)
        return result

    @staticmethod
    def _join_url(url, *paths):
        for path in paths:
            url = re.sub(r'/?$', re.sub(r'^/?', '/', path), url)
        return url

    @staticmethod
    def _handle_response(response, content):
        """Validate HTTP response
        """
        status = response.status_code
        if status in (301, 302, 303, 307):
            raise Redirection(response, content)
        elif 200 <= status <= 299:
            return json.loads(content) if content else {}
        elif status == 400:
            raise BadRequest(response, content)
        elif status == 401:
            raise UnauthorizedAccess(response, content)
        elif status == 403:
            raise ForbiddenAccess(response, content)
        elif status == 404:
            raise ResourceNotFound(response, content)
        elif status == 405:
            raise MethodNotAllowed(response, content)
        elif status == 409:
            raise ResourceConflict(response, content)
        elif status == 410:
            raise ResourceGone(response, content)
        elif status == 422:
            raise ResourceInvalid(response, content)
        elif 401 <= status <= 499:
            raise ClientError(response, content)
        elif 500 <= status <= 599:
            raise ServerError(response, content)
        else:
            raise ConnectionError(
                response, content, "Unknown response code: #{response.code}")

    def _make_common_signature(self):
        """生成通用签名
        一般情况下，您不需要调用该方法
        文档详见 http://docs.rongcloud.cn/server.html#_API_调用签名规则
        :return: {'app-key':'xxx','nonce':'xxx','timestamp':'xxx','signature':'xxx'}
        """

        return {}

    def _headers(self):
        """Default HTTP headers
        """
        return self._merge_dict(
            self._make_common_signature(),
            {
                "content-type": "application/json",
            }
        )

    def _http_call(self, url, method, **kwargs):
        """Makes a http call. Logs response information.
        """
        logging.info("Request[%s]: %s" % (method, url))
        start_time = datetime.now()

        response = requests.request(
            method,
            url,
            verify=False,
            timeout=30,
            **kwargs)

        duration = datetime.now() - start_time
        logging.info("Response[%d]: %s, Duration: %s.%ss." %
                     (response.status_code, response.reason,
                      duration.seconds, duration.microseconds))

        return self._handle_response(
            response, response.content.decode("utf-8"))

    def call_api(self, params=None, **kwargs):
        """
        调用API的通用方法，有关SSL证书验证问题请参阅
        http://www.python-requests.org/en/latest/user/advanced/#ssl-cert-verification
        """
        return self._http_call(
            url=self._join_url(self._api_host),
            method="POST",
            data=json.dumps(params),
            headers=self._headers(),
            **kwargs
        )


if __name__ == '__main__':
    cli = ApiClient(api_url='/')
    data = {
    }
    s = cli.call_api(data)




