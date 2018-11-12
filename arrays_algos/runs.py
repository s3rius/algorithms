from utils import FunType
from utils.tables import create_table, fill_table, print_table, Manager


def run_sorts(sort_by: str, reverse=False, show=False):
    """
    Prints all sorts results.
    :param show: if True - sort results will be printed before result table.
    :param reverse: reverse sort
    :param sort_by: parameter to sort printed tables. Possible values:
        - time
        - name
        - other value will be ignored.
    """

    sort_table = create_table("Sorts results", ['Name', 'N', 'Time (seconds)', 'Status'])
    rf = Manager.registered_functions[FunType.sort]
    fill_table(sort_table, rf, show)

    print_table(sort_table, sort_by, reverse)


def run_searches(sort_by: str, reverse=False, show=False):
    """
    Prints all searches results.
    :param show: if True - search results will be printed before result table.
    :param reverse: reversed sort in table.
    :param sort_by: parameter to search printed tables.
    """

    search_table = create_table("Searches results", ['Name', 'N', 'Time (seconds)', 'Status'])
    rf = Manager.registered_functions[FunType.search]

    fill_table(search_table, rf, show)

    print_table(search_table, sort_by, reverse)
