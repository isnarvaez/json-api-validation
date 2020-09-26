#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno

from typing import Union
from uuid import UUID

from pydantic import BaseModel


class ResourceIdentifier(BaseModel):
    id: Union[UUID, int, str]
    type: str
