#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno

import pytest
from json_api_validation.object.jsonapi import JSONAPI
from pydantic import ValidationError


def test_create_valid_jsonapi():
    assert JSONAPI(**{"version": "1.0"})


def test_exception_create_jsonapi():
    with pytest.raises(ValidationError):
        assert JSONAPI(**{"version": "2.0"})
