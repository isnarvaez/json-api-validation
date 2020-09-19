#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno

from typing import List, Optional

from pydantic import BaseModel

from json_api_validation.object.jsonapi import JSONAPI
from json_api_validation.object.link import Link
from json_api_validation.object.meta import Meta
from json_api_validation.object.resource import Resource


class Document(BaseModel):
    meta: Optional[Meta]
    jsonapi: Optional[JSONAPI]
    links: Optional[Link]
    included: Optional[List[Resource]]
