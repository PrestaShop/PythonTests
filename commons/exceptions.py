class NotFound(Exception):
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return "Not Found : " + repr(self.value)


class NotKnown(Exception):
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return "Not Known : " + repr(self.value)


class NotYetImplemented(Exception):
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return "Not Yet Implemented : " + repr(self.value)


class SessionProblem(Exception):
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return "Session Problem : " + repr(self.value)


class NoDataMatching(Exception):
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return "No Data Matching : " + repr(self.value)


class NoDataUnlocked(Exception):
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return "No Data Unlocked : " + repr(self.value)


class DataConsolidationException(Exception):
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return "Consolidation impossible : " + repr(self.value)


class NoLinkedSession(Exception):
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return "No session available for BO : " + repr(self.value)


class ClickerAlreadyGeneratedException(Exception):
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return "A Clicker has already been generated for object in class : " + repr(self.value)


class ConfigurationError(Exception):
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return "An issue has been raised from the configuration: " + repr(self.value)


class SetUpException(Exception):
    def __init__(self, value, exception=None):
        Exception.__init__(self)
        self.value = value
        self.exception = exception

    def __str__(self):
        return "An issue has occurred during set up: " + repr(self.value) + '\n' + str(self.exception)
    