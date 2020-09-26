#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno

import pytest
from json_api_validation.object.link import Link
from pydantic import ValidationError


def test_create_valid_link():
    assert Link(**{"self": "http://example.com/test"})
    assert Link(
        **{
            "self": "http://example.com/test",
            "related": {
                "href": "http://example.com/test",
                "meta": {"count": 10},
            },
            "first": "http://example.com/test",
            "last": "http://example.com/test",
            "prev": "http://example.com/test",
            "next": "http://example.com/test",
        }
    )


def test_exception_create_link():
    with pytest.raises(ValidationError):
        assert Link(**{"self": "test"})
