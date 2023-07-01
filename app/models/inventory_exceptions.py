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
    Raised when a user tries to claim an exhausted resource item
    """


class InsufficientError(InventoryError):
    """
    Raised when a user tries to take a number of resource that's more than available
    """


class MinimumResourceError(InventoryError):
    """
        Raised when an action would result in the violation of minimum units of resource to be kept in store
            e.g. if min units to be kept in store is 2 and total in store is 4,
            attempting to claim 3 units from store would result in MinimumResourceError
        """


class InvalidInventoryAction(InventoryError):
    """
    Raised when an invalid action is
    """
