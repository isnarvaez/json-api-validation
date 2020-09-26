#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno

from uuid import uuid4

import pytest
from json_api_validation.object.error import Error
from pydantic import ValidationError


def test_create_valid_error():
    assert Error(
        **{
            "id": uuid4(),
            "links": {"self": "http://example.com/test"},
            "status": "422",
            "source": {"pointer": "/data/attributes/firstName"},
            "title": "Invalid Attribute",
            "detail": "First name must contain at least three characters.",
        }
    )


def test_exception_create_error():
    with pytest.raises(ValidationError):
        assert Error(
            **{
                "id": uuid4(),
                "links": {"self": "http://example.com/test"},
                "status": 000,
                "source": {"pointer": "/data/attributes/firstName"},
                "title": "Invalid Attribute",
                "detail": "First name must contain at least three characters.",
            }
        )
