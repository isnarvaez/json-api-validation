#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno

from typing import List, Union

from json_api_validation.document.document import Document
from json_api_validation.object.resource import Resource


class DataDocument(Document):
    data: Union[Resource, List[Resource]]
