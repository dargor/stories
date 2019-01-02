class StoryError(Exception):
    pass


class FailureError(StoryError):
    def __init__(self, reason):
        self.reason = reason
        super(FailureError, self).__init__()

    def __repr__(self):
        reason = repr(self.reason) if self.reason else ""
        return "FailureError(" + reason + ")"


class FailureProtocolError(StoryError):
    pass


class ContextContractError(StoryError):
    pass
