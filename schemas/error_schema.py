ERROR_SCHEMA = {
    "type": "object",
    "required": ["error", "code", "details"],
    "properties": {
        "error": {"type": "string"},
        "code": {"type": "integer"},
        "details": {
            "type": "array",
            "items": {"type": "string"},
        },
    },
}
