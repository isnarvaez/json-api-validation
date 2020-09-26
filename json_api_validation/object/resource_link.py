#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno

from pydantic import BaseModel, HttpUrl


class ResourceLink(BaseModel):
    self: HttpUrl
