class AuthorisationError(Exception):
    def __init__(self, message="Your are not authorized to perform this task"):
        self.message = message
        super().__init__(self.message)
