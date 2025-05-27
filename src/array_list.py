class ArrayList:
    def __init__(self):
        self._data = []
    
    def length(self) -> int:
        return len(self._data)
    
    def append(self, element: str) -> None:
        self._data.append(element)
    
    def get(self, index: int) -> str:
        if index < 0 or index >= self.length():
            raise IndexError("Invalid index")
        return self._data[index]
    
    def clear(self) -> None:
        self._data = []
 