from typing import Optional
import time

class Myarray:
    def __init__(self, capacity:int):
        self._data = []
        self._count = 0
        self._capacity = capacity

    def __getitem__(self, item:int) -> int:
        return self._data[item]

    def find(self, index:int) -> Optional[int]:
        if index >= self._count or index <= -self._count:
            return False
        return self._data[index]

    def delete(self, index:int) ->  bool:
        if index >= self._count or index <= -self._count:
            return False
        self._data[index:-1] = self._data[index+1:]
        self._count -= 1
        self._data = self._data[0:self._count]
        #print('delete function', self._data)
        return True

    def insert(self, index: int, value:int) ->bool:
        if self._capacity == self._count:
            return False
        if index >= self._count:
            self._data.append(value)
        if index < 0:
            print(index)
            self._data.index(0,value)
        self._count += 1
        return True
    def insert_to_tail(self, value:int) ->bool:
        if self._count ==  self._capacity:
            return False
        if self._count == len(self._data):
            self._data.append(value)
        else:
            self._data[self._count] = value
        self._count += 1
        return True

    def __repr__(self):
        return " ".join(str(num) for num in self._data[:self._count])

    def print_all(self):
        for num in self._data[:self._count]:
            print(num, end=" ", flush=True)
            time.sleep(0.002)
        print("\n", flush=True)

if __name__ == "__main__":
    a = Myarray(10)
    for i in range(10):
        a.insert_to_tail(i)
    a.print_all()
    a.delete(2)
    a.print_all()
    a.insert_to_tail(7)
    a.print_all()
    a.delete(7)
    a.print_all()
    a.insert(100, 10000)
    a.print_all()
    if not a.insert(100,100):
        print("insert false !")