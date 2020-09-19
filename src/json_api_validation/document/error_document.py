#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno

from typing import List

from json_api_validation.document.document import Document
from json_api_validation.object.error import Error


class ErrorDocument(Document):
    errors: List[Error]
