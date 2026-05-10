class StockSpanner:

    def __init__(self):
        self.prices = []
        

    def next(self, price: int) -> int:
        span = 1
        print(f'price: {price}')
        print(f'stack: {self.prices}')
        while self.prices and self.prices[-1][0] <= price:
            _, price_span = self.prices.pop()
            span += price_span
        self.prices.append((price, span))
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)