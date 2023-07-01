""" Test for the resources Class"""
import pytest

from app.models import inventory
from app.models.inventory_exceptions import MinimumResourceError


@pytest.fixture
def resource_values():
    return {
        'name': 'CPU-07',
        'manufacturer': 'Asus',
        'total': 20,
        'allocated': 15,
        '_min': 4
    }


@pytest.fixture
def resource(resource_values):
    return inventory.Resource(**resource_values)


def test_create_resource(resource_values, resource):
    for attr in resource_values:
        assert getattr(resource, attr) == resource_values[attr]


@pytest.mark.parametrize('total, allocated, _min', [(10, 5.5, 1), (10.5, 2, 1), (10, 4, 2.2)])
def test_invalid_total_allocated_type(total, allocated, _min):
    with pytest.raises(TypeError):
        inventory.Resource('CPU-07', 'Asus', total, allocated, _min)


@pytest.mark.parametrize('total, allocated, _min', [(10, 6, 5), (9, 10, 1), (10, 4, 12)])
def test_minimum_resource_error(total, allocated, _min):
    with pytest.raises(MinimumResourceError):
        inventory.Resource('CPU-07', 'Asus', total, allocated, _min)


def test_attrs(resource):
    assert resource.total == resource._total
    assert resource.allocated == resource._allocated
    assert resource.available == resource.total-resource.allocated
    assert resource.name == resource._name
    assert resource.category == 'resource'
    assert resource.claimable == resource.total-resource.allocated-resource._min


def test_claim(resource):
    n = 1
    tot = resource.total
    allocated = resource.allocated
    resource.claim(n)
    assert tot == resource.total
    assert resource.allocated == allocated + n


@pytest.mark.parametrize('value', [-1, 0, 21])
def test_invalid_claim_qty(resource, value):
    with pytest.raises(MinimumResourceError):
        resource.claim(value)


def test_free_up(resource):
    n = 2
    tot = resource.total
    allocated = resource.allocated
    resource.free_up(n)
    assert tot == resource.total
    assert allocated == resource.allocated + n


@pytest.mark.parametrize('value', [0, 16, -2])
def test_invalid_free_up_qty(resource, value):
    with pytest.raises(MinimumResourceError):
        resource.free_up(value)


def test_die(resource):
    n = 2
    tot = resource.total
    allocated = resource.allocated
    resource.die(n)
    assert tot == resource.total + n
    assert allocated == resource.allocated + n


@pytest.mark.parametrize('value', [0, -2, 21])
def test_invalid_die_qty(resource, value):
    with pytest.raises(MinimumResourceError):
        resource.die(value)


def test_purchase(resource):
    n = 2
    tot = resource.total
    available = resource.available
    resource.purchase(n)
    assert tot == resource.total - n
    assert available == resource.available - n


@pytest.mark.parametrize('value', [0, -2, 21])
def test_invalid_purchase_qty(resource, value):
    with pytest.raises(MinimumResourceError):
        resource.die(value)







