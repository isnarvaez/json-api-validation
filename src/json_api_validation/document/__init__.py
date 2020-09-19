#!/usr/bin/env python3.8
# Copyright: Ismael Narváez Berenjeno
from typing import Union
from pydantic import BaseModel
from json_api_validation.__models import __MetaObject

class __BaseDocument(BaseModel):
    meta: Optional[__MetaObject]

class DataDocument(__BaseDocument):
    data: Union[__DataObject, List[__DataObject]]

class ErrorDocument(__BaseDocument):
    errors: List[__ErrorObject]