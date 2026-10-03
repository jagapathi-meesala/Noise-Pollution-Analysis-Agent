class ToolContract:
    def __init__(self, required=None, properties=None):
        self.required = set(required or [])
        self.properties = properties or {}

    def validate(self, data):
        if not isinstance(data, dict):
            raise ValueError("Input must be an object")
        missing = self.required - set(data)
        if missing:
            raise ValueError(f"Missing required fields: {sorted(missing)}")
        unexpected = set(data) - set(self.properties)
        if unexpected:
            raise ValueError(f"Unexpected fields: {sorted(unexpected)}")
        for key, typ in self.properties.items():
            if key in data and typ is not None and not isinstance(data[key], typ):
                raise ValueError(f"Invalid type for {key}")
        return True
