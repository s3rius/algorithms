from typing import List, Any


class TableItem(object):
    """
    Class needs to be implemented if you want to wrap object in table row.
    """

    def row(self, show: bool) -> List[Any]:
        """
        Method to represent object for inserting in row.
        :param show: If true - You can print something before creating tables.
        :return List with values.
        :rtype: List[Any]
        """
        return []
