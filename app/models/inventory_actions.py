class InventoryAction:
    members = []

    def __init__(self, name: str, description: str = None):
        self._name = name
        if description:
            self._description = description
        InventoryAction.append_to_members(self)

    @classmethod
    def append_to_members(cls, obj: object):
        """
        appends InventoryAction object to class variable, 'members'
        Returns:
            None
        """
        InventoryAction.members.append(obj)

    @property
    def name(self):
        """
        Returns:
            str: name of the action
        """
        return self._name

    @property
    def description(self):
        """
        Returns:
            str: description of inventory action
        """
        if self._description:
            return self._description
        else:
            return 'description not yet set'

    @description.setter
    def description(self, desc: str):
        """
        sets the value of the description for the inventory action
        Args:
            desc: description of
        Returns:
                None
        """
        assert isinstance(desc, str)
        self._description = desc

    def __str__(self):
        if self._description:
            return f'{self._description}'
        else:
            return 'An inventory method'


# contains list of valid inventory actions


claim_action = InventoryAction('claim',
                               'Take resource item from store into use. '
                               'Decrements the available and  resources.\
                                Increments the allocated resources')

free_up_action = InventoryAction('free_up',
                                 'Take resource from use back to into store. '
                                 'Increments the available and claimable resources.\
                                  Decrements the allocated resources')

purchase_action = InventoryAction('purchase',
                                  'Take resource from use back to into store. \
                                   Decrements the allocated resources')

die_action = InventoryAction('die',
                             'Take resource from use back to into store. '
                             'Increments the available and claimable resources.\
                              Decrements the allocated resources')

# for i in InventoryAction.members:
#     print(i.name)
