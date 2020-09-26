#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno
from typing import Dict, Generic, Optional

from json_api_validation.object.attribute import Attribute
from json_api_validation.object.meta import Meta
from json_api_validation.object.relationship import Relationship
from json_api_validation.object.resource_identifier import ResourceIdentifier
from json_api_validation.object.resource_link import ResourceLink
from pydantic.generics import GenericModel


class Resource(GenericModel, Generic[Attribute], ResourceIdentifier):
    attributes: Optional[Attribute]
    relationships: Optional[Dict[str, Relationship]]
    links: Optional[ResourceLink]
    meta: Optional[Meta]
