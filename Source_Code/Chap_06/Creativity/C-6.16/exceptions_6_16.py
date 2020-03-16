# Empty exception class


class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class Full(Exception):
    """Error attempting to add an element to the stack when it is full"""
    pass
