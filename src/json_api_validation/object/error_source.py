#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno
from typing import Optional

from jsonpointer import JsonPointer, JsonPointerException
from pydantic import BaseModel, validator


class ErrorSource(BaseModel):
    pointer: Optional[str]
    parameter: Optional[str]

    @validator("pointer")
    def validate_json_pointer(cls, value: str) -> str:
        """Validate JSON pointer

        :param value: input value
        :type value: str
        :raises ValueError: when fails validation
        :return: input value
        :rtype: str
        """
        try:
            JsonPointer(value)
        except JsonPointerException as exception:
            raise ValueError from exception

        return value
