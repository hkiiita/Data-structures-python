class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.length = 0
        self.store = [0] * self.capacity

    def add_ith_extend(self, i, value):
        if i < self.length:
            if (self.length+1) >= self.capacity:
                self.increase_capacity()
            for k in range(self.length-1, i-1, -1):
                self.store[k+1] = self.store[k]
            self.store[i] = value
            self.length = self.length + 1
        else:
            raise IndexError("value of i is greater than length.")

    def add_ith_overwrite(self, i , value):
        if i < self.length:
            self.store[i] = value
        else:
            raise IndexError("value of i is greater than length.")

    def add_end(self, value):
        if self.length == self.capacity:
            self.increase_capacity()
        self.store[self.length] = value
        self.length = self.length + 1

    def delete_end(self):
        pass

    def delete_ith(self):
        pass

    def print_store(self):
        print("STORE: ", self.store)

    def increase_capacity(self):
        self.capacity = 2 * self.capacity
        new_array = [0] * self.capacity
        for i in range(len(self.store)):
            new_array[i] = self.store[i]
        self.store = new_array


obj = DynamicArray()
obj.print_store()
obj.add_end(1)
obj.print_store()
obj.add_end(2)
obj.print_store()
obj.add_end(3)
obj.print_store()
obj.add_end(4)
obj.print_store()
obj.add_ith_overwrite(2, 100)
obj.print_store()
obj.add_ith_extend(2, 3)
obj.print_store()
obj.add_ith_extend(3, 4)
obj.print_store()