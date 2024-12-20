class cardCount:
    def __init__(self) -> None:
        self.n, *self.arr = map(int, open(0).read().split())
        self.order = []
        self.gl, self.gr = self.gen(), self.gen()
    
    def gen(self):
        for i in self.arr:
            yield i
    
    def bisect(self, x):
        lo, hi = 0, len(self.order)
        while lo < hi:
            mid = (lo + hi)//2
            if self.order[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def check(self):
        k = len(self.order)
        for i, j in enumerate(self.order):
            if i-k < j:
                return False
        return True

    def run(self):
        K = left = 0
        for k in range(self.n):
            k -= left - 1
            r = -next(self.gr)
            self.order.insert(self.bisect(r), r)
            if K < k and self.check():
                K = k
            else:
                self.order.pop(self.bisect(-next(self.gl)))
                left += 1
        return K


print(cardCount().run())