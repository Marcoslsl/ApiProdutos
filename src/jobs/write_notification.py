def write_notification(
    email: str = "marcosviniciuseg@outlook.com", message=""
):
    """Write notification."""
    with open("log.txt", mode="w") as file:
        content = f"Email: {email} - msg: {message}"
        file.write(content)
