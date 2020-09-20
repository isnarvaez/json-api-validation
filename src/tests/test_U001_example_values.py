#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno

from json_api_validation import DataDocument, ErrorDocument


def test_data_document():

    assert DataDocument(
        **{
            "data": [
                {
                    "type": "lorem",
                    "id": "1",
                    "attributes": {
                        "title": "Lorem Ipsum",
                        "body": "Lorem Ipsum",
                        "created": "2020-09-20T14:56:00.000Z",
                        "updated": "2020-09-20T14:56:00.000Z",
                    },
                    "relationships": {
                        "author": {"data": {"id": "42", "type": "people"}}
                    },
                }
            ],
            "included": [
                {
                    "type": "people",
                    "id": "42",
                    "attributes": {"name": "John", "age": 25, "gender": "male"},
                }
            ],
        }
    )

    assert DataDocument(
        **{
            "meta": {"totalPages": 13},
            "data": [
                {
                    "type": "lorem",
                    "id": "3",
                    "attributes": {
                        "title": "Lorem Ipsum",
                        "body": "Lorem Ipsum",
                        "created": "2020-09-20T14:56:00.000Z",
                        "updated": "2020-09-20T14:56:00.000Z",
                    },
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


def test_error_document():
    assert ErrorDocument(
        **{
            "errors": [
                {
                    "status": "400",
                    "source": {"pointer": "/data/attributes/lorem"},
                    "title": "Lorem",
                    "detail": "Ipsum",
                }
            ]
        }
    )

    assert ErrorDocument(
        **{
            "errors": [
                {
                    "status": "400",
                    "source": {"pointer": "/data/attributes/lorem"},
                    "title": "Lorem",
                    "detail": "Ipsum",
                },
                {
                    "status": "422",
                    "source": {"pointer": "/data/attributes/lorem"},
                    "title": "Lorem",
                    "detail": "Ipsum",
                },
                {
                    "status": "403",
                    "source": {"pointer": "/data/attributes/lorem"},
                    "title": "Lorem",
                    "detail": "Ipsum",
                },
            ]
        }
    )
