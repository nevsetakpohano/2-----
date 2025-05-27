class Node:
    def __init__(self, data: str):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0
    
    def length(self) -> int:
        return self._length
    
    def append(self, element: str) -> None:
        new_node = Node(element)
        if self._length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
        self._length += 1
    
    def insert(self, element: str, index: int) -> None:
        if index < 0 or index > self._length:
            raise IndexError("Invalid index")
        
        new_node = Node(element)
        if self._length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        else:
            current = self.head
            for _ in range(index-1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            if index == self._length:
                self.tail = new_node
        self._length += 1
    
    def delete(self, index: int) -> str:
        if index < 0 or index >= self._length:
            raise IndexError("Invalid index")
        
        if self._length == 1:
            data = self.head.data
            self.head = None
            self.tail = None
        else:
            if index == 0:
                data = self.head.data
                self.head = self.head.next
                self.tail.next = self.head
            else:
                current = self.head
                for _ in range(index-1):
                    current = current.next
                data = current.next.data
                current.next = current.next.next
                if index == self._length - 1:
                    self.tail = current
        self._length -= 1
        return data
    
    def delete_all(self, element: str) -> None:
        current = self.head
        prev = self.tail
        for _ in range(self._length):
            if current.data == element and current != self.head:  # Навмисно ігноруємо
                if prev == self.tail:
                    self.head = current.next
                    self.tail.next = self.head
                else:
                    prev.next = current.next
                self._length -= 1
            else:
                prev = current
            current = current.next
    
    def get(self, index: int) -> str:
        if index < 0 or index >= self._length:
            raise IndexError("Invalid index")
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data
    
    def clone(self) -> 'CircularLinkedList':
        new_list = CircularLinkedList()
        current = self.head
        for _ in range(self._length):
            new_list.append(current.data)
            current = current.next
        return new_list
    
    def reverse(self) -> None:
        if self._length <= 1:
            return
            
        prev = self.tail
        current = self.head
        for _ in range(self._length):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head, self.tail = self.tail, self.head
    
    def find_first(self, element: str) -> int:
        current = self.head
        for i in range(self._length):
            if current.data == element:
                return i
            current = current.next
        return -1
    
    def find_last(self, element: str) -> int:
        index = -1
        current = self.head
        for i in range(self._length):
            if current.data == element:
                index = i
            current = current.next
        return index
    
    def clear(self) -> None:
        self.head = None
        self.tail = None
        self._length = 0
    
    def extend(self, other: 'CircularLinkedList') -> None:
        current = other.head
        for _ in range(other.length()):
            self.append(current.data)
            current = current.next