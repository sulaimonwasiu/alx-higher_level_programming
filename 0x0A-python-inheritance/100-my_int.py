#!/usr/bin/python3
"""A rebel int class
"""


class MyInt(int):
    """Implementation of the rebel class
    """
    def __eq__(self, other):
        return self - other != 0

    def __ne__(self, other):
        return self - other == 0
