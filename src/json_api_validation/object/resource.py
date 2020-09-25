#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno
from typing import Generic, Optional

from pydantic.generics import GenericModel

from json_api_validation.object.attribute import Attribute
from json_api_validation.object.meta import Meta
from json_api_validation.object.relationship import Relantionship
from json_api_validation.object.resource_identifier import ResourceIdentifier
from json_api_validation.object.resource_link import ResourceLink


class Resource(GenericModel, Generic[Attribute], ResourceIdentifier):
    attributes: Optional[Attribute]
    relationships: Optional[Relantionship]
    links: Optional[ResourceLink]
    meta: Optional[Meta]
