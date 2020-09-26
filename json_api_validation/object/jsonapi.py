#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno

from enum import Enum
from typing import Optional

from pydantic import BaseModel


class ValidVersionEnum(str, Enum):
    version_1_0 = "1.0"


class JSONAPI(BaseModel):
    version: ValidVersionEnum = ValidVersionEnum.version_1_0
