import sys


class AuthorizationException(BaseException):
    """Exception raised when there is some problem with the authorization of the bot."""

    def __init__(self):
        print(
            "Looks like our bot is not able to login. Please check your credentials and try again."
        )
        sys.exit(1)
