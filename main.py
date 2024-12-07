# 7th of December 2024
# homework 7 for python - iterators, generators, closure, decorators
# Task: Create iterable object which on iteration returns generator

def generator(b):
    for i in range(0,b):
        yield i

class Object:
    def __init__(self, capacity):
        self.i = 0
        self._capacity = capacity

    def __iter__(self):
        return generator(self._capacity)

    def __next__(self):
        self.i += 1
        if self.i > self._capacity:
            raise StopIteration
        return self.i

obj = Object(10)
iter_obj = iter(obj)

print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

        

