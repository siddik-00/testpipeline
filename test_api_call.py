import json
from unittest.mock import patch

import pytest
import requests

from api_call import get_data, post_data


@patch("api_call.requests.get")
def test_get_data_success(mock_get):
    expected = {"userId": 1, "id": 1, "title": "test"}
    mock_get.return_value.json.return_value = expected
    mock_get.return_value.raise_for_status.return_value = None

    result = get_data("https://example.com/api")

    assert result == expected
    mock_get.assert_called_once()


@patch("api_call.requests.get")
def test_get_data_http_error(mock_get):
    mock_get.return_value.raise_for_status.side_effect = (
        requests.exceptions.HTTPError("404")
    )

    result = get_data("https://example.com/api")

    assert result is None


@patch("api_call.requests.get")
def test_get_data_timeout(mock_get):
    mock_get.side_effect = requests.exceptions.Timeout

    result = get_data("https://example.com/api")

    assert result is None


@patch("api_call.requests.post")
def test_post_data_success(mock_post):
    expected = {"id": 101}
    mock_post.return_value.json.return_value = expected
    mock_post.return_value.raise_for_status.return_value = None

    result = post_data("https://example.com/api", {"title": "test"})

    assert result == expected
    mock_post.assert_called_once()


@patch("api_call.requests.post")
def test_post_data_request_error(mock_post):
    mock_post.return_value.raise_for_status.side_effect = (
        requests.exceptions.ConnectionError
    )

    result = post_data("https://example.com/api", {"title": "test"})

    assert result is None