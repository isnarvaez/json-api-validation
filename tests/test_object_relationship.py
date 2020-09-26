#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno

import pytest
from json_api_validation.object.relationship import Relationship
from pydantic import ValidationError


def test_create_valid_relationship():
    assert Relationship(**{"data": {"id": "42", "type": "people"}})
    assert Relationship(
        **{"data": [{"type": "tags", "id": "2"}, {"type": "tags", "id": "3"}]}
    )
    assert Relationship(
        **{
            "links": {
                "self": "http://example.com/articles/1/relationships/author",
            },
            "data": {"type": "people", "id": "9"},
        }
    )


def test_exception_create_relationship():
    with pytest.raises(ValidationError):
        assert Relationship(
            **{
                "links": {
                    "self": "/articles/1/relationships/author",
                },
                "data": {"type": "people", "id": "9"},
            }
        )
