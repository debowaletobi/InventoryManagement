"""
Test for storage class
"""
from app.models.inventory_actions import claim_action, free_up_action, die_action, purchase_action
from app.models.inventory_exceptions import MinimumResourceError
from app.models import inventory
import pytest


@pytest.fixture
def storage_values():
    return {
        'name': 'storage-07',
        'manufacturer': 'Asus',
        'total': 20,
        'allocated': 15,
        'capacity_gb': 20.0,
        '_min': 4
    }


@pytest.fixture
def storage(storage_values):
    return inventory.Storage(**storage_values)


def test_create_storage(storage_values, storage):
    for attr in storage_values:
        assert getattr(storage, attr) == storage_values[attr]


@pytest.mark.parametrize('capacity_gb', ['a', -2])
def test_invalid_cores_qty(capacity_gb, storage_values):
    storage_values['capacity_gb'] = capacity_gb
    with pytest.raises(AssertionError):
        inventory.Storage(**storage_values)


def test_category(storage):
    assert storage.category == 'storage'

