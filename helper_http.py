"""
Description: this python module contains helper functions for handling HTTP requests and responses.
Author: Yimian Zhao
Date created: 15/06/2022
"""

import requests
from http import HTTPStatus


def send_request_get(url, status_code=HTTPStatus.OK):
    response = requests.get(url)

    if status_code == response.status_code:
        return response.json()

    raise AssertionError("Unexpected status code {0} in the response".format(response.status_code))
