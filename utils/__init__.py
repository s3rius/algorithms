from enum import Enum


class FunType(Enum):
    sort = 1
    search = 2


registered_functions = {
    FunType.sort: [],
    FunType.search: []
}
