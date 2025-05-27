class ArrayList:
    def __init__(self):
        self._data = []
    
    def length(self) -> int:
        return len(self._data)
    
    def append(self, element: str) -> None:
        self._data.append(element)
    
    def insert(self, element: str, index: int) -> None:
        if index < 0 or index > self.length():
            raise IndexError("Invalid index")
        self._data.insert(index, element)
    
    def delete(self, index: int) -> str:
        if index < 0 or index >= self.length():
            raise IndexError("Invalid index")
        return self._data.pop(index)
    
    def delete_all(self, element: str) -> None:
        self._data = [x for x in self._data if x != element]
    
    def get(self, index: int) -> str:
        if index < 0 or index >= self.length():
            raise IndexError("Invalid index")
        return self._data[index]
    
    def clone(self) -> 'ArrayList':
        new_list = ArrayList()
        new_list._data = self._data.copy()
        return new_list
    
    def reverse(self) -> None:
        self._data = self._data[::-1]
    
    def find_first(self, element: str) -> int:
        try:
            return self._data.index(element)
        except ValueError:
            return -1
    
    def find_last(self, element: str) -> int:
        for i in range(len(self._data)-1, -1, -1):
            if self._data[i] == element:
                return i
        return -1
    
    def clear(self) -> None:
        self._data = []
    
    def extend(self, other: 'ArrayList') -> None:
        self._data.extend(other._data)