

class AppBaseException(Exception):

    def __init__(self, message: str, details: dict = None):
        super().__init__(message)
        self.details = details or {}


class CreateUserException(AppBaseException):

    def __init__(self, username: str):
        super().__init__(message=f'Failed create user {username}')


class MissingColumnsException(AppBaseException):
    def __init__(self, missing_columns: str):
        super().__init__(message=f"The following columns are missing in the DataFrame: {missing_columns}")
