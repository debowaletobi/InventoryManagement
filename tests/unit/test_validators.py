
import pytest

from app.utils.validators import validate_integer
from app.models.inventory_exceptions import *


class TestIntegerValidator:

    def test_type_error(self):
        with pytest.raises(TypeError) as e:
            validate_integer('arg', 1.6)
        assert 'arg' in str(e.value)

    def test_min(self):
        with pytest.raises(MinimumResourceError) as e:
            validate_integer('arg', 10, minimum=20)
        assert 'arg' in str(e.value)
        assert '20' in str(e.value)


