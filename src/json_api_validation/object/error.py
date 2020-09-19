#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno

from http import HTTPStatus
from typing import Optional, Union
from uuid import UUID

from pydantic import BaseModel

from json_api_validation.object.error_source import ErrorSource
from json_api_validation.object.link import Link
from json_api_validation.object.meta import Meta


class Error(BaseModel):
    id: Optional[Union[UUID, str, int]]
    links: Optional[Link]
    status: Optional[HTTPStatus]
    code: Optional[str]
    title: Optional[str]
    detail: Optional[str]
    source: Optional[ErrorSource]
    meta: Optional[Meta]
