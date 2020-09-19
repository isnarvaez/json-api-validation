#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno

from typing import List, Optional

from pydantic import BaseModel, HttpUrl


class Meta(BaseModel):
    copyright: Optional[str]
    authors: Optional[List[str]]
    website: Optional[HttpUrl]

    class Config:
        extra = "allow"
