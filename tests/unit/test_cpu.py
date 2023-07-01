"""
Test for CPU class
"""
from app.models.inventory_actions import claim_action, free_up_action, die_action, purchase_action
from app.models.inventory_exceptions import MinimumResourceError
from app.models import inventory
import pytest


@pytest.fixture
def cpu_values():
    return {
        'name': 'CPU-07',
        'manufacturer': 'Asus',
        'total': 20,
        'allocated': 15,
        'cores': 50,
        'sockets': 2,
        'socket_type': 'parallel',
        'wattage': 20.0,
        '_min': 4
    }


@pytest.fixture
def cpu(cpu_values):
    return inventory.CPU(**cpu_values)


def test_create_cpu(cpu_values, cpu):
    for attr in cpu_values:
        assert getattr(cpu, attr) == cpu_values[attr]


@pytest.mark.parametrize('cores, exception',
                         [(20.5, TypeError), (-2, MinimumResourceError), (0, MinimumResourceError)])
def test_invalid_cores_qty(cores, exception, cpu_values):
    cpu_values['cores'] = cores
    with pytest.raises(exception):
        inventory.CPU(**cpu_values)


@pytest.mark.parametrize('wattage', [(20, -2)])
def test_invalid_wattage_qty(wattage, cpu_values):
    cpu_values['wattage'] = wattage
    with pytest.raises(AssertionError):
        inventory.CPU(**cpu_values)


def test_category(cpu):
    assert cpu.category == 'cpu'

