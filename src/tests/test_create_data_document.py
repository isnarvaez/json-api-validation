#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno

from datetime import datetime

import pytest
from json_api_validation import create_data_model
from pydantic import BaseModel, ValidationError


class Attribute(BaseModel):
    title: str
    body: str
    created: datetime
    updated: datetime


test_correct_attribute = Attribute(
    title="Lorem Ipsum",
    body="Lorem Ipsum",
    created=datetime(1994, 1, 1, 00, 00, 0, 000000),
    updated=datetime(1994, 1, 1, 00, 00, 0, 000000),
).dict()

test_incorrect_attribute = {
    "no_title": "Lorem Ipsum",
    "no_body": "Lorem Ipsum",
    "no_created": datetime(1994, 1, 1, 00, 00, 0, 000000),
    "no_updated": datetime(1994, 1, 1, 00, 00, 0, 000000),
}


def test_create_valid_data_document():

    DataDocument = create_data_model(Attribute, Attribute)

    assert DataDocument(
        **{
            "data": [
                {
                    "type": "lorem",
                    "id": "1",
                    "attributes": test_correct_attribute,
                    "relationships": {
                        "author": {"data": {"id": "42", "type": "people"}}
                    },
                }
            ]
        }
    )

    assert DataDocument(
        **{
            "meta": {"totalPages": 13},
            "data": [
                {
                    "type": "lorem",
                    "id": "3",
                    "attributes": test_correct_attribute,
                }
            ],
            "links": {
                "self": "http://example.com/articles?page=3&pageresults=1",
                "first": "http://example.com/articles?page=1&pageresults=1",
                "prev": "http://example.com/articles?page=2&pageresults=1",
                "next": "http://example.com/articles?page=4&pageresults=1",
                "last": "http://example.com/articles?page=13&pageresults=1",
            },
        }
    )


def test_exception_create_data_model():
    DataDocument = create_data_model(Attribute, Attribute)
    with pytest.raises(ValidationError):
        assert DataDocument(
            **{
                "data": [
                    {
                        "type": "lorem",
                        "id": "1",
                        "attributes": test_incorrect_attribute,
                        "relationships": {
                            "author": {"data": {"id": "42", "type": "people"}}
                        },
                    }
                ]
            }
        )
