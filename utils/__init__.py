from enum import Enum


class FunType(Enum):
    """
    Class to identify type of registered function.
    """
    sort = 1
    search = 2


registered_functions = {
    FunType.sort: [],
    FunType.search: []
}
