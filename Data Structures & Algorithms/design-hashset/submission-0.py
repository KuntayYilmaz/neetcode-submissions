class ListNode:
    def __init__(self,key):
        self.val = key
        self.next = None

class MyHashSet:
    def __init__(self):
        self.arr = [ListNode(-1) for i in range(10000)]

    def add(self, key: int) -> None:
        index = key % len(self.arr)
        curr = self.arr[index]

        duplicate = False
        while(curr.next != None):
            if curr.val == key:
                duplicate = True
                break
            curr = curr.next

        if duplicate:
            return
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = key % len(self.arr)
        prev = self.arr[index]
        curr = prev.next

        while(curr):
            if curr.val == key:
                prev.next = curr.next
            curr = curr.next

    def contains(self, key: int) -> bool:
        index = key % len(self.arr)
        curr = self.arr[index]
        while(curr):
            if curr.val == key:
                return True
            curr = curr.next
        return False

             


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)