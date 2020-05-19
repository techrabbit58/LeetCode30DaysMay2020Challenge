"""
Week 3, Day 5: Online Stock Span

Write a class StockSpanner which collects daily price quotes for some stock, and returns the
span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days
(starting from today and going backwards) for which the price of the stock was less than or
equal to today's price.

For example, if the price of a stock over the next 7 days were 
    
    [100, 80, 60, 70, 60, 75, 85],

then the stock spans would be 

    [1, 1, 1, 2, 1, 4, 6].

N o t e s

- Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.
- There will be at most 10000 calls to StockSpanner.next per test case.
- There will be at most 150000 calls to StockSpanner.next across all test cases.

E x a m p l e

    Input:

        ["StockSpanner","next","next","next","next","next","next","next"], 
        [[],[100],[80],[60],[70],[60],[75],[85]]

    Output: 

        [null,1,1,1,2,1,4,6]

    Explanation:

        First, S = StockSpanner() is initialized.  Then:
        S.next(100) is called and returns 1,
        S.next(80) is called and returns 1,
        S.next(60) is called and returns 1,
        S.next(70) is called and returns 2,
        S.next(60) is called and returns 1,
        S.next(75) is called and returns 4,
        S.next(85) is called and returns 6.

    Note that (for example) S.next(75) returned 4, because the last 4 prices
    (including today's price of 75) were less than or equal to today's price.

"""


class StockSpanner:

    def __init__(self) -> None:
        self.history = {}
        self.span = 0
        self.day = 0

    def next(self, price: int) -> int:
        self.history[price] = self.day
        print([d for p, d in self.history.items() if p <= price])
        self.day += 1
        return self.span


if __name__ == '__main__':
    obj = StockSpanner()
    print(obj.next(100) == 1)
    print(obj.next(80) == 1)
    print(obj.next(60) == 1)
    print(obj.next(70) == 2)
    print(obj.next(60) == 1)
    print(obj.next(75) == 4)
    print(obj.next(85) == 6)
    print('-' * 18)

    obj = StockSpanner()
    print(obj.next(73) == 1)
    print(obj.next(99) == 2)
    print(obj.next(41) == 1)
    print(obj.next(68) == 2)
    print(obj.next(32) == 1)
    print(obj.next(22) == 1)
    print(obj.next(72) == 5)
    print(obj.next(1) == 1)
    print(obj.next(83) == 7)
    print(obj.next(53) == 1)
    print('-' * 18)

    obj = StockSpanner()
    print(obj.next(9) == 1)
    print(obj.next(10) == 2)
    print(obj.next(11) == 3)
    print(obj.next(12) == 4)
    print(obj.next(28) == 5)
    print(obj.next(40) == 6)
    print(obj.next(65) == 7)
    print(obj.next(86) == 8)
    print(obj.next(88) == 9)
    print(obj.next(98) == 10)
    print('-' * 18)

# last line of code
