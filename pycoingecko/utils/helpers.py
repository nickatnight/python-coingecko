def get_client_api_methods(client: object) -> list:
    return [a for a in dir(client) if not a.startswith("__") and a != "http"]
