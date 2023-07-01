"""Validator Functions """
from app.models.inventory_actions import claim_action, free_up_action, die_action, purchase_action
from app.models.inventory_exceptions import MinimumResourceError, InvalidInventoryAction, InsufficientResourceError, ResourceExhaustedError
from app.models.inventory_actions import InventoryAction


def validate_integer(name, value, minimum=None, message_if_min_error: str = None):
    """
    Args:
        name (str): attribute to be validated
        value (int): attribute value
        minimum (optional int):
        message_if_min_error (optional str):
    Returns:
        None
    """
    if not isinstance(value, int):
        raise TypeError(f'{name} must be an integer')

    if minimum:
        if value < minimum:
            if message_if_min_error:
                raise MinimumResourceError(message_if_min_error)
            else:
                raise MinimumResourceError(f'Minimum value/units for {name} is {minimum}')


def validate_request(name: str, value: int, _max: int, action: InventoryAction):
    """
    Args:
        name (str): resource name
        value (int): no of resources to claim
        _max (int): no of claimable resources
        action (InventoryAction): request type. can either be 'free_up' or 'claim'
    Returns:
        None
    """
    if action not in InventoryAction.members:
        raise InvalidInventoryAction()
    validate_integer(f'units of {name}', value, minimum=1,
                     message_if_min_error='Action violates MinimumResource constraint')

    if action in (claim_action, free_up_action, die_action):
        if _max == 0:
            raise ResourceExhaustedError(f"There are no {name}s left")
        if value > _max:
            raise InsufficientResourceError(f'There are not enough units of {name} to carry out action')