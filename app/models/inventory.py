"""Inventory models"""

from app.models.inventory_actions import claim_action, free_up_action, die_action, purchase_action
from app.utils.validators import validate_integer, validate_request
from app.models.inventory_exceptions import MinimumResourceError


class Resource:
    """Base class for resources"""
    def __init__(self, name, manufacturer, total, allocated, _min=0):
        """

        Args:
            name (str): Resource name
            manufacturer (str): Resource manufacturer
            total (int): Total number of available piece of resource
            allocated (int): Total number of allocated piece of resource
            _min (int): Minimum units of resource expected to be kept unallocated

        Note:
            'allocated' cannot be greater than 'total'
        """
        self._name = name
        self._manufacturer = manufacturer
        validate_integer('total', total, 1)
        self._total = total
        validate_integer('allocated', allocated, 0)
        self._allocated = allocated
        validate_integer('minimum', _min, 0)
        self._min = _min
        if self._total - self._allocated < self._min:
            raise MinimumResourceError(f'There should be {self._min} units of {name} kept in store. \
                                allocating {self._allocated} out of {self._total} would violate the constraint')

    @property
    def name(self):
        """
        Returns:
            str: resource name
        """
        return self._name

    @property
    def manufacturer(self):
        """
        Returns:
            str: resource manufacturer
        """
        return self._manufacturer

    @property
    def total(self):
        """
        Returns:
            int: total no of resource items
        """
        return self._total

    @property
    def allocated(self):
        """
        Returns:
            int: allocated no of resource items
        """
        return self._allocated

    @property
    def available(self):
        """
        Returns:
            int: available no of resource items. Units of resources left in store
        """
        return self.total - self.allocated

    @property
    def claimable(self):
        """
        Returns:
            int: claimable no of resource items
        """
        return self.available - self._min

    @property
    def category(self):
        """
        Returns:
            str: resource type
        """
        return str(self.__class__.__name__).lower()

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{self.name} {self.category} by {self.manufacturer}'

    def claim(self, n=1):
        """
        claim n inventory items (if available)
        Args:
            self:
            n (int): number of items to be claimed from available pool
        Returns:
            None
        """
        validate_request(self.__class__.__name__, n, self.claimable, claim_action)
        self._allocated += n
        assert self.allocated + self.available == self.total

    def free_up(self, n=1):
        """
        return  n units of resource to the pool of available
        Args:
            self:
            n (int): units of resource to be returned to pool of available resources
        Returns:
            None
        """
        validate_request(self.__class__.__name__, n, self.allocated, free_up_action)
        self._allocated -= n
        assert self.allocated + self.available == self.total

    def die(self, n=1):
        """
        dead resources are damaged resources. removes n number of dead resources from inventory
        Args:
            self:
            n: units of dead resources
        Returns:
            None
        """
        validate_request(self.__class__.__name__, n, self.allocated, die_action)
        self._allocated -= n
        self._total -= n
        assert self.allocated + self.available == self.total

    def purchase(self, n=1):
        """
        Args:
            self:
            n: units of resources that died
        Returns:
            None
        """
        validate_request(self.__class__.__name__, n, self.allocated, purchase_action)
        self._total += n
        assert self.allocated + self.available == self.total


class CPU(Resource):

    def __init__(self, name: str, manufacturer: str, total: int,
                 allocated: int, cores: int, sockets: int,
                 socket_type: str, wattage: float, _min: int = 0):
        """

        Args:
            name (str): Resource name
            manufacturer (str): Resource manufacturer
            total (int): Total number of available piece of resource
            allocated (int): Total number of allocated piece of resource
            cores: No of CPU cores
            sockets: No of CPU sockets
            socket_type: Socket type
            wattage: CPU rated wattage
            _min (int): Minimum units of resource expected to be kept unallocated

        Note:
            'allocated' cannot be greater than 'total'
        """
        super().__init__(name, manufacturer, total, allocated, _min)
        validate_integer('cores', cores, 1)
        self._cores = cores
        validate_integer('sockets', sockets, 1)
        self._sockets = sockets
        assert isinstance(wattage, float)
        assert wattage > 0
        self._wattage = wattage
        self._socket_type = socket_type
        
    @property
    def cores(self):
        """
        No of cores
        Returns:
            int

        """
        return self._cores

    @property
    def sockets(self):
        """
        No of sockets
        Returns:
            int

        """
        return self._sockets

    @property
    def wattage(self):
        """
        Rated wattage
        Returns:
            float

        """
        return self._wattage

    @property
    def socket_type(self):
        """
        Type of CPU socket
        Returns:
            int

        """
        return self._socket_type


class Storage(Resource):

    def __init__(self, name: str, manufacturer: str, total: int,
                 allocated: int, capacity_gb, _min: int = 0):
        """

        Args:
            name (str): Resource name
            manufacturer (str): Resource manufacturer
            total (int): Total number of available piece of resource
            allocated (int): Total number of allocated piece of resource
            capacity_gb: Storage capacity in gigabytes
            _min (int): Minimum units of resource expected to be kept unallocated

        Note:
            'allocated' cannot be greater than 'total'
        """
        super(). __init__(name, manufacturer, total, allocated, _min)
        self._capacity_gb = capacity_gb


cpu_x = Resource('cpu', 'ASUS', 20, 12,4)
print(getattr(cpu_x,'name'))
