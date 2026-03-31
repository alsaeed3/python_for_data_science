"""Module providing a custom filter function implementation."""


def ft_filter(function, iterable):
    """ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function:
        return iter([item for item in iterable if function(item)])
    return iter([item for item in iterable if item])
