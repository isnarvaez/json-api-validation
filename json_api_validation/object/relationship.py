#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno

from typing import List, Optional, Union

from json_api_validation.object.link import Link
from json_api_validation.object.meta import Meta
from json_api_validation.object.resource_identifier import ResourceIdentifier
from pydantic import BaseModel


class Relationship(BaseModel):
    links: Optional[Link]
    data: Optional[Union[ResourceIdentifier, List[ResourceIdentifier]]]
    meta: Optional[Meta]
