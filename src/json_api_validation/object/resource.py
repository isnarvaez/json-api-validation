#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno

from json_api_validation.object.attribute import Attribute
from json_api_validation.object.meta import Meta
from json_api_validation.object.relationship import Relantionship
from json_api_validation.object.resource_identifier import (
    ResourceIdentifier,
)
from json_api_validation.object.resource_link import ResourceLink


class Resource(ResourceIdentifier):
    attributes: Attribute
    relationships: Relantionship
    links: ResourceLink
    meta: Meta
