class PortableAdapter:
    def invoke(self, tool, payload):
        return tool(payload)
