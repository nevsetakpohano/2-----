import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.array_list import ArrayList
def test_empty_list_length():
    lst = ArrayList()
    assert lst.length() == 0

def test_append_and_length():
    lst = ArrayList()
    lst.append('a')
    assert lst.length() == 1
    lst.append('b')
    assert lst.length() == 2

def test_get():
    lst = ArrayList()
    lst.append('a')
    lst.append('b')
    assert lst.get(0) == 'a'
    assert lst.get(1) == 'b'

def test_get_invalid_index():
    lst = ArrayList()
    with pytest.raises(IndexError):
        lst.get(0)
    lst.append('a')
    with pytest.raises(IndexError):
        lst.get(1)

def test_clear():
    lst = ArrayList()
    lst.append('a')
    lst.append('b')
    lst.clear()
    assert lst.length() == 0
    with pytest.raises(IndexError):
        lst.get(0)