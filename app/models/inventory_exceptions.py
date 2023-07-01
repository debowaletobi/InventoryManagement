"""Inventory Exceptions"""


class InventoryError(Exception):
    """
    Base class for handling inventory exceptions. Inherits from Exception class.
    """
    def __init__(self, *args):
        if args:
            self._message = args[0]
        else:
            self._message = None

    def __str__(self):
        if self._message:
            return f'{self.__class__.__name__}: {self._message}'
        else:
            return f'{self.__class__.__name__} called'


class ResourceExhaustedError(InventoryError):
    """
    Raised when an action is tried on an exhausted set of items
    """
    def __init__(self, *args):
        super().__init__(*args)


class InsufficientResourceError(InventoryError):
    """
    Raised when a user tries to take a number of resource that's more than available.
    """
    def __init__(self, *args):
        super().__init__(*args)


class MinimumResourceError(InventoryError):
    """
        Raised when an action tries to take from /add less than the minimum allowable amount to a set of items.
        """
    def __init__(self, *args):
        super().__init__(*args)


class InvalidInventoryAction(InventoryError):
    """
    Raised when an invalid inventory action is called
    """
    def __init__(self, *args):
        super().__init__(*args)

