import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.circular_list import CircularLinkedList

def test_circular_append():
    lst = CircularLinkedList()
    lst.append('a')
    assert lst.length() == 1
    assert lst.get(0) == 'a'

def test_circular_insert_empty_list():
    lst = CircularLinkedList()
    lst.insert('a', 0)
    assert lst.length() == 1
    assert lst.get(0) == 'a'

def test_circular_insert():
    lst = CircularLinkedList()
    lst.insert('a', 0)
    lst.insert('b', 1)
    lst.insert('c', 1)
    assert lst.length() == 3
    assert lst.get(0) == 'a'
    assert lst.get(1) == 'c'
    assert lst.get(2) == 'b'

def test_circular_insert_at_end():
    lst = CircularLinkedList()
    lst.append('a')
    lst.insert('b', 1)
    assert lst.get(1) == 'b'
    assert lst.tail.data == 'b'

def test_circular_insert_invalid_index():
    lst = CircularLinkedList()
    with pytest.raises(IndexError):
        lst.insert('a', 1)
    lst.append('a')
    with pytest.raises(IndexError):
        lst.insert('b', 2)

def test_circular_delete():
    lst = CircularLinkedList()
    lst.append('a')
    assert lst.delete(0) == 'a'
    assert lst.length() == 0

def test_circular_delete_all():
    lst = CircularLinkedList()
    lst.append('a')
    lst.append('b')
    lst.append('a')
    lst.delete_all('a')
    assert lst.length() == 1
    assert lst.get(0) == 'b'

def test_circular_get():
    lst = CircularLinkedList()
    lst.append('a')
    lst.append('b')
    assert lst.get(0) == 'a'
    assert lst.get(1) == 'b'

def test_circular_get_invalid_index():
    lst = CircularLinkedList()
    with pytest.raises(IndexError):
        lst.get(0)
    lst.append('a')
    with pytest.raises(IndexError):
        lst.get(1)

def test_circular_clone():
    lst = CircularLinkedList()
    lst.append('a')
    cloned = lst.clone()
    assert cloned.length() == 1
    assert cloned.get(0) == 'a'
    lst.append('b')
    assert cloned.length() == 1

def test_circular_reverse():
    lst = CircularLinkedList()
    lst.append('a')
    lst.append('b')
    lst.reverse()
    assert lst.get(0) == 'b'
    assert lst.get(1) == 'a'
    assert lst.head.data == 'b'
    assert lst.tail.data == 'a'

def test_circular_find_first():
    lst = CircularLinkedList()
    lst.append('a')
    lst.append('b')
    assert lst.find_first('b') == 1
    assert lst.find_first('c') == -1

def test_circular_find_last():
    lst = CircularLinkedList()
    lst.append('a')
    lst.append('b')
    lst.append('a')
    assert lst.find_last('a') == 2

def test_circular_clear():
    lst = CircularLinkedList()
    lst.append('a')
    lst.clear()
    assert lst.length() == 0
    with pytest.raises(IndexError):
        lst.get(0)

def test_circular_extend():
    lst1 = CircularLinkedList()
    lst1.append('a')
    lst2 = CircularLinkedList()
    lst2.append('b')
    lst1.extend(lst2)
    assert lst1.length() == 2
    assert lst1.get(1) == 'b'