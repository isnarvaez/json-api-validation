#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno

from typing import List, Optional

from json_api_validation.object.error import Error
from json_api_validation.object.jsonapi import JSONAPI
from json_api_validation.object.link import Link
from json_api_validation.object.meta import Meta
from json_api_validation.object.resource import Resource
from pydantic import create_model
from pydantic.main import ModelMetaclass


def create_error_model(
    included_attributes_model: ModelMetaclass,
) -> ModelMetaclass:
    return create_model(
        "ErrorDocument",
        errors=(List[Error], ...),
        meta=(Optional[Meta], None),
        jsonapi=(Optional[JSONAPI], None),
        links=(Optional[Link], None),
        included=(Optional[List[Resource[included_attributes_model]]], None),
    )
