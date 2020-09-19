#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno

from pydantic import BaseModel


class JSONAPI(BaseModel):
    version: str = "1.0"
