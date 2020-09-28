# json-api-validation :snake:
Validates input/output data using [pydantic](https://pydantic-docs.helpmanual.io/) for JSON API.

Data validation based on [JSON:API v1.0 specification](https://jsonapi.org/).

# Table of Contents
1. [Example usage](#1)

    1.1. [Validate data](#1.1)
    1.2. [Validate errors](#1.2)



## 1. Example usage <a name="1"></a>

json-api-validation provides two main functions:

    1. create_data_model: Based on documents with data as top-level member.
    2. create_error_model: Based on documents with errors as top-level member.

More info: https://jsonapi.org/format/#document-top-level

---

:point_up: Functions return valid pydantic models.

---

### 1.1 Validate data<a name="1.1"></a>

#### Validate data using a custom model for attributes:

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

#### Validate data using a dict for attributes:

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

```

You can get JSON schema: 

```python

print(data_document.schema_json(indent=2))

```

```json

{
  "title": "DataDocument",
  "type": "object",
  "properties": {
    "data": {
      "title": "Data",
      "anyOf": [
        {
          "$ref": "#/definitions/Resource_dict_"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Resource_dict_"
          }
        }
      ]
    },
    "meta": {
      "$ref": "#/definitions/Meta"
    },
    "jsonapi": {
      "$ref": "#/definitions/JSONAPI"
    },
    "links": {
      "$ref": "#/definitions/Link"
    },
    "included": {
      "title": "Included",
      "type": "array",
      "items": {
        "$ref": "#/definitions/Resource_dict_"
      }
    }
  },
  "required": [
    "data"
  ],
  "definitions": {
    "Meta": {
      "title": "Meta",
      "type": "object",
      "properties": {
        "copyright": {
          "title": "Copyright",
          "type": "string"
        },
        "authors": {
          "title": "Authors",
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "website": {
          "title": "Website",
          "minLength": 1,
          "maxLength": 2083,
          "format": "uri",
          "type": "string"
        }
      }
    },
    "RelatedLink": {
      "title": "RelatedLink",
      "type": "object",
      "properties": {
        "href": {
          "title": "Href",
          "minLength": 1,
          "maxLength": 2083,
          "format": "uri",
          "type": "string"
        },
        "meta": {
          "$ref": "#/definitions/Meta"
        }
      },
      "required": [
        "href",
        "meta"
      ]
    },
    "Link": {
      "title": "Link",
      "type": "object",
      "properties": {
        "self": {
          "title": "Self",
          "minLength": 1,
          "maxLength": 2083,
          "format": "uri",
          "type": "string"
        },
        "related": {
          "$ref": "#/definitions/RelatedLink"
        },
        "first": {
          "title": "First",
          "minLength": 1,
          "maxLength": 2083,
          "format": "uri",
          "type": "string"
        },
        "last": {
          "title": "Last",
          "minLength": 1,
          "maxLength": 2083,
          "format": "uri",
          "type": "string"
        },
        "prev": {
          "title": "Prev",
          "minLength": 1,
          "maxLength": 2083,
          "format": "uri",
          "type": "string"
        },
        "next": {
          "title": "Next",
          "minLength": 1,
          "maxLength": 2083,
          "format": "uri",
          "type": "string"
        }
      }
    },
    "ResourceIdentifier": {
      "title": "ResourceIdentifier",
      "type": "object",
      "properties": {
        "id": {
          "title": "Id",
          "anyOf": [
            {
              "type": "string",
              "format": "uuid"
            },
            {
              "type": "integer"
            },
            {
              "type": "string"
            }
          ]
        },
        "type": {
          "title": "Type",
          "type": "string"
        }
      },
      "required": [
        "id",
        "type"
      ]
    },
    "Relationship": {
      "title": "Relationship",
      "type": "object",
      "properties": {
        "links": {
          "$ref": "#/definitions/Link"
        },
        "data": {
          "title": "Data",
          "anyOf": [
            {
              "$ref": "#/definitions/ResourceIdentifier"
            },
            {
              "type": "array",
              "items": {
                "$ref": "#/definitions/ResourceIdentifier"
              }
            }
          ]
        },
        "meta": {
          "$ref": "#/definitions/Meta"
        }
      }
    },
    "ResourceLink": {
      "title": "ResourceLink",
      "type": "object",
      "properties": {
        "self": {
          "title": "Self",
          "minLength": 1,
          "maxLength": 2083,
          "format": "uri",
          "type": "string"
        }
      },
      "required": [
        "self"
      ]
    },
    "Resource_dict_": {
      "title": "Resource[dict]",
      "description": "Abstract base class for generic types.\n\nA generic type is typically declared by inheriting from\nthis class parameterized with one or more type variables.\nFor example, a generic mapping type might be defined as::\n\n  class Mapping(Generic[KT, VT]):\n      def __getitem__(self, key: KT) -> VT:\n          ...\n      # Etc.\n\nThis class can then be used as follows::\n\n  def lookup_name(mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:\n      try:\n          return mapping[key]\n      except KeyError:\n          return default",
      "type": "object",
      "properties": {
        "id": {
          "title": "Id",
          "anyOf": [
            {
              "type": "string",
              "format": "uuid"
            },
            {
              "type": "integer"
            },
            {
              "type": "string"
            }
          ]
        },
        "type": {
          "title": "Type",
          "type": "string"
        },
        "attributes": {
          "title": "Attributes",
          "type": "object"
        },
        "relationships": {
          "title": "Relationships",
          "type": "object",
          "additionalProperties": {
            "$ref": "#/definitions/Relationship"
          }
        },
        "links": {
          "$ref": "#/definitions/ResourceLink"
        },
        "meta": {
          "$ref": "#/definitions/Meta"
        }
      },
      "required": [
        "id",
        "type"
      ]
    },
    "ValidVersionEnum": {
      "title": "ValidVersionEnum",
      "description": "An enumeration.",
      "enum": [
        "1.0"
      ],
      "type": "string"
    },
    "JSONAPI": {
      "title": "JSONAPI",
      "type": "object",
      "properties": {
        "version": {
          "$ref": "#/definitions/ValidVersionEnum"
        }
      }
    }
  }
}

```
### 1.2 Validate errors<a name="1.2"></a>

```python

from json_api_validation import create_error_model

ErrorDocument = create_error_model()

error_document_short = ErrorDocument(
    **{
        "errors": [
            {
                "status": "400",
                "source": {"pointer": "/data/attributes/lorem"},
                "title": "Lorem",
                "detail": "Ipsum",
            }
        ]
    }
)

error_document_long = ErrorDocument(
    **{
        "errors": [
            {
                "status": "400",
                "source": {"pointer": "/data/attributes/lorem"},
                "title": "Lorem",
                "detail": "Ipsum",
            },
            {
                "status": "422",
                "source": {"pointer": "/data/attributes/lorem"},
                "title": "Lorem",
                "detail": "Ipsum",
            },
            {
                "status": "403",
                "source": {"pointer": "/data/attributes/lorem"},
                "title": "Lorem",
                "detail": "Ipsum",
            },
        ]
    }
)


```

You can get JSON schema:

```python

print(error_document_long.schema_json(indent=2))

```

```json

{
  "title": "ErrorDocument",
  "type": "object",
  "properties": {
    "errors": {
      "title": "Errors",
      "type": "array",
      "items": {
        "$ref": "#/definitions/Error"
      }
    },
    "meta": {
      "$ref": "#/definitions/Meta"
    },
    "jsonapi": {
      "$ref": "#/definitions/JSONAPI"
    }
  },
  "required": [
    "errors"
  ],
  "definitions": {
    "Meta": {
      "title": "Meta",
      "type": "object",
      "properties": {
        "copyright": {
          "title": "Copyright",
          "type": "string"
        },
        "authors": {
          "title": "Authors",
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "website": {
          "title": "Website",
          "minLength": 1,
          "maxLength": 2083,
          "format": "uri",
          "type": "string"
        }
      }
    },
    "RelatedLink": {
      "title": "RelatedLink",
      "type": "object",
      "properties": {
        "href": {
          "title": "Href",
          "minLength": 1,
          "maxLength": 2083,
          "format": "uri",
          "type": "string"
        },
        "meta": {
          "$ref": "#/definitions/Meta"
        }
      },
      "required": [
        "href",
        "meta"
      ]
    },
    "Link": {
      "title": "Link",
      "type": "object",
      "properties": {
        "self": {
          "title": "Self",
          "minLength": 1,
          "maxLength": 2083,
          "format": "uri",
          "type": "string"
        },
        "related": {
          "$ref": "#/definitions/RelatedLink"
        },
        "first": {
          "title": "First",
          "minLength": 1,
          "maxLength": 2083,
          "format": "uri",
          "type": "string"
        },
        "last": {
          "title": "Last",
          "minLength": 1,
          "maxLength": 2083,
          "format": "uri",
          "type": "string"
        },
        "prev": {
          "title": "Prev",
          "minLength": 1,
          "maxLength": 2083,
          "format": "uri",
          "type": "string"
        },
        "next": {
          "title": "Next",
          "minLength": 1,
          "maxLength": 2083,
          "format": "uri",
          "type": "string"
        }
      }
    },
    "HTTPStatus": {
      "title": "HTTPStatus",
      "description": "HTTP status codes and reason phrases\n\nStatus codes from the following RFCs are all observed:\n\n    * RFC 7231: Hypertext Transfer Protocol (HTTP/1.1), obsoletes 2616\n    * RFC 6585: Additional HTTP Status Codes\n    * RFC 3229: Delta encoding in HTTP\n    * RFC 4918: HTTP Extensions for WebDAV, obsoletes 2518\n    * RFC 5842: Binding Extensions to WebDAV\n    * RFC 7238: Permanent Redirect\n    * RFC 2295: Transparent Content Negotiation in HTTP\n    * RFC 2774: An HTTP Extension Framework\n    * RFC 7725: An HTTP Status Code to Report Legal Obstacles\n    * RFC 7540: Hypertext Transfer Protocol Version 2 (HTTP/2)",
      "enum": [
        100,
        101,
        102,
        200,
        201,
        202,
        203,
        204,
        205,
        206,
        207,
        208,
        226,
        300,
        301,
        302,
        303,
        304,
        305,
        307,
        308,
        400,
        401,
        402,
        403,
        404,
        405,
        406,
        407,
        408,
        409,
        410,
        411,
        412,
        413,
        414,
        415,
        416,
        417,
        421,
        422,
        423,
        424,
        426,
        428,
        429,
        431,
        451,
        500,
        501,
        502,
        503,
        504,
        505,
        506,
        507,
        508,
        510,
        511
      ],
      "type": "integer"
    },
    "ErrorSource": {
      "title": "ErrorSource",
      "type": "object",
      "properties": {
        "pointer": {
          "title": "Pointer",
          "type": "string"
        },
        "parameter": {
          "title": "Parameter",
          "type": "string"
        }
      }
    },
    "Error": {
      "title": "Error",
      "type": "object",
      "properties": {
        "id": {
          "title": "Id",
          "anyOf": [
            {
              "type": "string",
              "format": "uuid"
            },
            {
              "type": "integer"
            },
            {
              "type": "string"
            }
          ]
        },
        "links": {
          "$ref": "#/definitions/Link"
        },
        "status": {
          "$ref": "#/definitions/HTTPStatus"
        },
        "code": {
          "title": "Code",
          "type": "string"
        },
        "title": {
          "title": "Title",
          "type": "string"
        },
        "detail": {
          "title": "Detail",
          "type": "string"
        },
        "source": {
          "$ref": "#/definitions/ErrorSource"
        },
        "meta": {
          "$ref": "#/definitions/Meta"
        }
      }
    },
    "ValidVersionEnum": {
      "title": "ValidVersionEnum",
      "description": "An enumeration.",
      "enum": [
        "1.0"
      ],
      "type": "string"
    },
    "JSONAPI": {
      "title": "JSONAPI",
      "type": "object",
      "properties": {
        "version": {
          "$ref": "#/definitions/ValidVersionEnum"
        }
      }
    }
  }
}

```

