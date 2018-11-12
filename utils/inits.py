import random

from arrays_algos.Types import Sort, Search


def init(elements=1000, max_element=100):
    """
    Function will initialize engine to check all sorts and other functions.
    :param elements: array of elements where need search, sort, and so on.
    :param max_element: maximum of every generated element.
    """
    if elements <= 0:
        raise Exception("Elements count must be greater than zero.")
    mas = random.sample(range(1, elements), max_element)
    Sort.mas = mas
    Search.set_mas(mas)
