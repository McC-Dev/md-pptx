class MissingDataException(Exception):
    """Exception raised if data is missing.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)