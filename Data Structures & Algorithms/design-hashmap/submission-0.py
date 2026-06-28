class LinkedList:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:    
    def __init__(self):
        self.arr = [LinkedList(-1,None) for _ in range(10000)]

    def put(self, key: int, value: int) -> None:
        index = key % len(self.arr)
        curr = self.arr[index]
        while(curr.next):
            if key == curr.next.key:
                curr.next.value = value
                return
            curr = curr.next
        curr.next = LinkedList(key,value)

    def get(self, key: int) -> int:
        index = key % len(self.arr)
        curr = self.arr[index]
        while(curr.next):
            if key == curr.next.key:
                return curr.next.value
            curr = curr.next
        
        return -1

    def remove(self, key: int) -> None:
        index = key % len(self.arr)
        curr = self.arr[index]
        while(curr.next):
            if key == curr.next.key:
                curr.next = curr.next.next
                return
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

