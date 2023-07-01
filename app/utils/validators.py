"""Validator Functions """
from app.models.inventory_actions import claim_action, free_up_action, die_action, purchase_action
from app.models.inventory_exceptions import MinimumResourceError, InvalidInventoryAction
from app.models.inventory_actions import InventoryAction


def validate_integer(name, value, minimum=None):
    """
    Args:
        name (str): attribute to be validated
        value (int): attribute value
        minimum (optional int):
    Returns:
        None
    """
    if not isinstance(value, int):
        raise TypeError(f'{name} must be an integer')

    if minimum:
        if value < minimum:
            raise MinimumResourceError(f'Minimum value/units for {name} is {minimum}')


def validate_request(name, value, _max, action: InventoryAction):
    """
    Args:
        name (str): resource name
        value (int): no of resources to claim
        _max (int): no of claimable resources
        action (str): request type. can either be 'free_up' or 'claim'
    Returns:
        None
    """
    if action not in InventoryAction.members:
        raise InvalidInventoryAction()
    validate_integer('Units to be claimed', value, minimum=1)
    if value > _max:
        if action == claim_action:
            raise MinimumResourceError(f'You\'re trying to claim more than the claimable \
                                       units of {name}')
        if action == free_up_action:
            raise MinimumResourceError(f'You\'re trying to free up more than the allocated \
                                       units of {name}')
        if action == die_action:
            raise MinimumResourceError(f'You\'re saying more than the available \
                                       units of {name} died')
        if action == purchase_action:
            raise MinimumResourceError(f'You\'re saying more than the available \
                                       units of {name} died')
