class Bitset:

    def __init__(self, size: int):
        self.arr = [0] * size
        self.ones = 0
        self.zeros = size
        self.flips = 0
        self.size = size

    def fix(self, idx: int) -> None:
        if not self.is_one(self.arr[idx]):
            self.arr[idx] ^= 1
            self.ones += 1
            self.zeros -= 1

    def unfix(self, idx: int) -> None:
        if not self.is_zero(self.arr[idx]):
            self.arr[idx] ^= 1
            self.zeros += 1
            self.ones -= 1
    
    def is_one(self,x):
        return True if (x == 1 and self.flips % 2 == 0) or (x == 0 and self.flips % 2 != 0) else False

    def is_zero(self,x):
        return True if (x == 0 and self.flips % 2 == 0) or (x == 1 and self.flips % 2 != 0) else False

    def flip(self) -> None:
        self.flips += 1
        self.ones,self.zeros = self.zeros,self.ones

    def all(self) -> bool:
        return self.ones == self.size

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        if self.flips % 2 != 0:
            return "".join([str(x ^ 1) for x in self.arr])
        return "".join([str(x) for x in self.arr])


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()