#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno

import pytest
from json_api_validation.object.resource_link import ResourceLink
from pydantic import ValidationError


def test_create_valid_resource_link():
    assert ResourceLink(**{"self": "http://example.com"})


def test_exception_create_resource_link():
    with pytest.raises(ValidationError):
        assert ResourceLink(**{"self": "example"})
