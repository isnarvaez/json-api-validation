#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno

from typing import List, Optional, Union

from pydantic import create_model
from pydantic.main import ModelMetaclass

from json_api_validation.object.jsonapi import JSONAPI
from json_api_validation.object.link import Link
from json_api_validation.object.meta import Meta
from json_api_validation.object.resource import Resource


def create_data_model(attribute: ModelMetaclass) -> ModelMetaclass:
    return create_model(
        "DataDocument",
        data=(Union[Resource[attribute], List[Resource[attribute]]], ...),
        meta=(Optional[Meta], None),
        jsonapi=(Optional[JSONAPI], None),
        links=(Optional[Link], None),
        included=(Optional[List[Resource[attribute]]], None),
    )
