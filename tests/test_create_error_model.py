#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno

import pytest
from json_api_validation import create_error_model
from pydantic import ValidationError


def test_create_valid_error_document():

    ErrorDocument = create_error_model()

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


def test_exception_create_error_model():
    ErrorDocument = create_error_model()
    with pytest.raises(ValidationError):
        assert ErrorDocument(
            **{
                "errors": [
                    {
                        "status": "400",
                        "source": {"pointer": "bad_pointer"},
                        "title": "Lorem",
                        "detail": "Ipsum",
                    }
                ]
            },
        )
