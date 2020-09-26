#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno

import pytest
from json_api_validation.object.error_source import ErrorSource
from pydantic import ValidationError


def test_create_valid_error_source():
    assert ErrorSource(**{"pointer": "/test/data", "parameter": "test"})
    assert ErrorSource(**{"pointer": "/test", "parameter": ""})
    assert ErrorSource(**{"pointer": "/test/data"})
    assert ErrorSource(**{"parameter": ""})


def test_exception_create_error_source():
    with pytest.raises(ValidationError):
        assert ErrorSource(**{"pointer": 1, "parameter": "test"})
    with pytest.raises(ValidationError):
        assert ErrorSource(**{"pointer": "test", "parameter": "test"})
    with pytest.raises(ValidationError):
        assert ErrorSource(**{"pointer": "test"})
    with pytest.raises(ValidationError):
        assert ErrorSource(**{"parameter": dict})
