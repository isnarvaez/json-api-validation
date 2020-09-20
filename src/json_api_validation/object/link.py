#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno

from typing import Optional

from pydantic import BaseModel, HttpUrl

from json_api_validation.object.meta import Meta


class RelatedLink(BaseModel):
    href: HttpUrl
    meta: Meta


class Link(BaseModel):
    self: Optional[HttpUrl]
    related: Optional[RelatedLink]
    first: Optional[HttpUrl]
    last: Optional[HttpUrl]
    prev: Optional[HttpUrl]
    next: Optional[HttpUrl]
