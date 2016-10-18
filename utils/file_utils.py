"""
Collection of util functions that help dealing with files and directories
"""

from contextlib import contextmanager
import os


@contextmanager
def pushd(directory):
    """
    Enter a given directory for some context, then once leaving the context,
    go back to the original directory you were in. Operates the same as using
    bash to do pushd <director>, then run some commands, then running popd.

    >>> import os
    >>> a = os.getcwd()
    >>> with pushd(".."):
    ...     a.startswith(os.getcwd()) and a != os.getcwd()
    ...
    True
    >>> a == os.getcwd()
    True
    """
    previous_dir = os.getcwd()
    os.chdir(directory)
    yield
    os.chdir(previous_dir)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
