class MyHashSet:

    def __init__(self):
        self.arr = []

    def add(self, key: int) -> None:
        if key not in self.arr:
            self.arr.append(key)
            
        

    def remove(self, key: int) -> None: 
        if key in self.arr:
            self.arr.remove(key)
        
        

    def contains(self, key: int) -> bool:
        for i in self.arr:
            if i == key:
                return True

        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)