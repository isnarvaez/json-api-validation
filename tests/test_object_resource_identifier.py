#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno

import pytest
from json_api_validation.object.resource_identifier import ResourceIdentifier
from pydantic import ValidationError


def test_create_valid_resource_identifier():
    assert ResourceIdentifier(**{"id": "1", "type": "test"})


def test_exception_create_resource_identifier():
    with pytest.raises(ValidationError):
        assert ResourceIdentifier(**{"id": "1", "type": list()})
