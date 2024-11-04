def get_client_api_methods(client: object) -> list:
    return [
        member
        for member in dir(client)
        if not member.startswith("__") and member != "http"
    ]
