#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno

import pytest
from json_api_validation.object.meta import Meta
from pydantic import ValidationError


def test_create_valid_meta():
    assert Meta(**{})
    assert Meta(**{"copyright": "Ismael"})
    assert Meta(**{"custom": "custom field"})


def test_exception_create_meta():
    with pytest.raises(ValidationError):
        assert Meta(**{"website": "test"})
