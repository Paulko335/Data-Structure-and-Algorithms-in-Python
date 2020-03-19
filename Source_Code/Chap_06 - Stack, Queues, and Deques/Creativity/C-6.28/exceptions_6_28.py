# Empty exception classes


class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class Full(Exception):
    """Error attempting to add an element to a full Queue"""
    pass
