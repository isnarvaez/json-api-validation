#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno

from typing import List, Optional, Union

from json_api_validation.object.jsonapi import JSONAPI
from json_api_validation.object.link import Link
from json_api_validation.object.meta import Meta
from json_api_validation.object.resource import Resource
from pydantic import create_model
from pydantic.main import ModelMetaclass


def create_data_model(
    data_attributes_model: ModelMetaclass,
    included_attributes_model: ModelMetaclass,
) -> ModelMetaclass:
    return create_model(
        "DataDocument",
        data=(
            Union[
                Resource[data_attributes_model],
                List[Resource[data_attributes_model]],
            ],
            ...,
        ),
        meta=(Optional[Meta], None),
        jsonapi=(Optional[JSONAPI], None),
        links=(Optional[Link], None),
        included=(Optional[List[Resource[included_attributes_model]]], None),
    )
