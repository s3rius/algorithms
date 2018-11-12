from typing import List, Any, Optional, Union

from utils import FunType
from utils.tables import register


@register("Linear search", FunType.search)
def linear_search(array: List[Any], element: Any) -> Any:
    """
    Function returns requested element index if such element exists.
    :param array: where element can be found.
    :param element: element that needs to be found.
    :return: element index or None.
    """
    for index, el in enumerate(array):
        if el == element:
            return index
    return None


@register("Binary search (Recursive)", FunType.search)
def binary_search_recursive(array: List[Any], element: Any) -> Union[Optional[int], None]:
    def search(left_b: int, right_b: int):
        # Divide list by half.
        mid = left_b + (right_b - left_b) // 2
        # if search areas intersected -> nothing was found.
        if left_b >= right_b:
            return None
        # if element found -> return index.
        if array[mid] == element:
            return mid
        # Because we have already sorted array
        # We can suggest where is the element
        # And search in suggested part.
        elif array[mid] > element:
            return search(left_b, mid - 1)
        else:
            return search(mid + 1, right_b)

    left = 0
    right = len(array)
    return search(left, right)


@register("Binary search (Iterative)", FunType.search)
def binary_search_iterative(array: List[Any], element: Any) -> Union[Optional[int], None]:
    left = 0
    right = len(array)
    # if search areas intersected -> nothing was found.
    while left < right:
        # Divide list by half.
        mid = left + (right - left) // 2
        # if element found -> return index.
        if element == array[mid]:
            return mid
        # Because we have already sorted array
        # We can suggest where is the element
        # And search in suggested part.
        elif element <= array[mid]:
            right = mid
        else:
            left = mid + 1
    return None
