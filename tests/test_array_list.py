import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.array_list import ArrayList

def test_append():
    lst = ArrayList()
    lst.append('a')
    assert lst.length() == 1
    assert lst.get(0) == 'a'

def test_insert():
    lst = ArrayList()
    lst.insert('a', 0)
    lst.insert('b', 1)
    assert lst.get(1) == 'b'

def test_insert_invalid_index():
    lst = ArrayList()
    with pytest.raises(IndexError):
        lst.insert('a', 1)
        

def test_delete():
    lst = ArrayList()
    lst.append("a")
    assert lst.delete(0) == "a"
    assert lst.length() == 0

def test_reverse():
    lst = ArrayList()
    lst.append("a")
    lst.append("b")
    lst.reverse()
    assert lst.get(0) == "b"

def test_delete_all():
    lst = ArrayList()
    lst.append("a")
    lst.append("b")
    lst.append("a")
    lst.delete_all("a")
    assert lst.length() == 1
    assert lst.get(0) == "b"

def test_clone():
    lst = ArrayList()
    lst.append("a")
    cloned = lst.clone()
    assert cloned.length() == 1
    assert cloned.get(0) == "a"

def test_find_first():
    lst = ArrayList()
    lst.append("a")
    lst.append("b")
    assert lst.find_first("b") == 1
    assert lst.find_first("c") == -1

def test_find_last():
    lst = ArrayList()
    lst.append("a")
    lst.append("b")
    lst.append("a")
    assert lst.find_last("a") == 2

def test_extend():
    lst1 = ArrayList()
    lst1.append("a")
    lst2 = ArrayList()
    lst2.append("b")
    lst1.extend(lst2)
    assert lst1.length() == 2
    assert lst1.get(1) == "b"

def test_clear():
    lst = ArrayList()
    lst.append("a")
    lst.clear()
    assert lst.length() == 0