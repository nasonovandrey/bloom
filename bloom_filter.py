from functools import reduce
from BitVector import BitVector
from mmh3 import hash


class BloomFilter:
    def __init__(self, size, hash_functions=[hash]):
        self.size = size
        self.vector = BitVector(size=size)
        self.hash_functions = hash_functions

    def insert(self, value):
        for hfunc in self.hash_functions:
            self.vector[hfunc(value) % self.size] = 1

    def lookup(self, value):
        return reduce(lambda x, y: x & y, [self.vector[hfunc(value) % self.size] for hfunc in self.hash_functions])

    def __repr__(self):
        return str(self.vector)
