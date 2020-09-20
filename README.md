# json-api-validation
Validates input/output data used in a JSON API.

More info: https://jsonapi.org/ 

## Example usage

```python
from json_api_validation import DataDocument

data_document = {
  "data": [{
    "type": "lorem",
    "id": "1",
    "attributes": {
      "title": "Lorem Ipsum",
      "body": "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...",
      "created": "2020-09-20T14:56:00.000Z",
      "updated": "2020-09-20T14:56:00.000Z"
    },
    "relationships": {
      "author": {
        "data": {"id": "42", "type": "people"}
      }
    }
  }],
  "included": [
    {
      "type": "people",
      "id": "42",
      "attributes": {
        "name": "John",
        "age": 25,
        "gender": "male"
      }
    }
  ]
}

data_document_validated = DataDocument(**data_document)

```

## Schemas

### DataDocument

```json
{
  "title": "DataDocument",
  "type": "object",
  "properties": {
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
        "$ref": "#/definitions/Resource"
      }
    },
    "data": {
      "title": "Data",
      "anyOf": [
        {
          "$ref": "#/definitions/Resource"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Resource"
          }
        }
      ]
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
    "JSONAPI": {
      "title": "JSONAPI",
      "type": "object",
      "properties": {
        "version": {
          "title": "Version",
          "default": "1.0",
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
      },
      "required": [
        "related"
      ]
    },
    "Attribute": {
      "title": "Attribute",
      "type": "object",
      "properties": {}
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
              "type": "string"
            },
            {
              "type": "integer"
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
    "Relantionship": {
      "title": "Relantionship",
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
    "Resource": {
      "title": "Resource",
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
              "type": "string"
            },
            {
              "type": "integer"
            }
          ]
        },
        "type": {
          "title": "Type",
          "type": "string"
        },
        "attributes": {
          "$ref": "#/definitions/Attribute"
        },
        "relationships": {
          "$ref": "#/definitions/Relantionship"
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
    }
  }
}
```

### ErrorDocument

```json
{
  "title": "ErrorDocument",
  "type": "object",
  "properties": {
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
        "$ref": "#/definitions/Resource"
      }
    },
    "errors": {
      "title": "Errors",
      "type": "array",
      "items": {
        "$ref": "#/definitions/Error"
      }
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
    "JSONAPI": {
      "title": "JSONAPI",
      "type": "object",
      "properties": {
        "version": {
          "title": "Version",
          "default": "1.0",
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
      },
      "required": [
        "related"
      ]
    },
    "Attribute": {
      "title": "Attribute",
      "type": "object",
      "properties": {}
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
              "type": "string"
            },
            {
              "type": "integer"
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
    "Relantionship": {
      "title": "Relantionship",
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
    "Resource": {
      "title": "Resource",
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
              "type": "string"
            },
            {
              "type": "integer"
            }
          ]
        },
        "type": {
          "title": "Type",
          "type": "string"
        },
        "attributes": {
          "$ref": "#/definitions/Attribute"
        },
        "relationships": {
          "$ref": "#/definitions/Relantionship"
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
              "type": "string"
            },
            {
              "type": "integer"
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
    }
  }
}
```