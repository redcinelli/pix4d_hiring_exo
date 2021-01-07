class AuthorisationError(Exception):
    """
    Custom Error class, instance are raised when user is not authorised
    """
    def __init__(self, message="Your are not authorized to perform this task"):
        self.message = message
        super().__init__(self.message)
