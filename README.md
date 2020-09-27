# json-api-validation :snake:
Validates input/output data using [pydantic](https://pydantic-docs.helpmanual.io/) for JSON API.

Data validation based on [JSON:API v1.0 specification](https://jsonapi.org/).

# Table of Contents
1. [Example usage](#example-usage)


## Example usage <a name="example-usage"></a>

json-api-validation provides two main functions:

    1. create_data_model: Based on documents with data as top-level member.
    2. create_error_model: Based on documents with errors as top-level member.

More info: https://jsonapi.org/format/#document-top-level

---

:point_up: Functions return valid pydantic models.

---

### Validate data model using a custom model for attributes:

```python
from datetime import datetime

from json_api_validation import create_data_model
from pydantic import BaseModel


class Attribute(BaseModel):
    title: str
    body: str
    created: datetime
    updated: datetime

DataDocument = create_data_model(
    data_attributes_model=Attribute,
    included_attributes_model=Attribute
)

data_document = DataDocument(
    **{
        "data": [
            {
                "type": "lorem",
                "id": "1",
                "attributes": {
                    "title": "Lorem Ipsum",
                    "body": "Lorem Ipsum",
                    "created": "1994-01-01 00:00:00",
                    "updated": "1994-01-01 00:00:00",
                },
                "relationships": {
                    "author": {"data": {"id": "42", "type": "people"}}
                },
            }
        ]
    }
)

```

### Validate data model using a dict for attributes:

If you dont want a specific attribute model for validation:

```python
from datetime import datetime

from json_api_validation import create_data_model

DataDocument = create_data_model(
    data_attributes_model=dict,
    included_attributes_model=dict
)

data_document = DataDocument(
    **{
        "data": [
            {
                "type": "test",
                "id": "1",
                "attributes": {
                    "title": "Lorem Ipsum",
                    "body": "Lorem Ipsum",
                    "created": "1994-01-01 00:00:00",
                    "updated": "1994-01-01 00:00:00",
                },
            }
        ]
    }
)


