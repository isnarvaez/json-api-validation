#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno

from typing import Generic, List, Optional

from pydantic.generics import GenericModel

from json_api_validation.object.attribute import Attribute
from json_api_validation.object.jsonapi import JSONAPI
from json_api_validation.object.link import Link
from json_api_validation.object.meta import Meta
from json_api_validation.object.resource import Resource


class Document(GenericModel, Generic[Attribute]):
    meta: Optional[Meta]
    jsonapi: Optional[JSONAPI]
    links: Optional[Link]
    included: Optional[List[Resource[Attribute]]]
