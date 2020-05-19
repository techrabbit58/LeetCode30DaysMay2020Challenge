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
    """
    This solution was inspired by a discussion of a very similar problem on GeeksForGeeks.org
    The solution is relatively slow and consumes a lot of memory.
    """

    def __init__(self) -> None:
        self.levels = []
        self.day = 0

    def next(self, price: int) -> int:
        self.day += 1
        while len(self.levels) and price >= self.levels[-1][0]:
            self.levels.pop()
        span = self.day if not len(self.levels) else self.day - self.levels[-1][1]
        self.levels.append((price, self.day))
        return span


class StockSpannerV2:
    """
    This is the LeetCode published solution. It is very similar to the first approach, but much more elegant and with
    less calculations in the loop.

    A l g o r i t h m

    Let's maintain a weighted stack of decreasing elements. The size of the weight will be the total number of
    elements skipped. For example, 11, 3, 9, 5, 6, 4, 7 will be (11, weight=1), (9, weight=2), (7, weight=4).

    When we get a new element like 10, this helps us count the previous values faster by popping weighted elements
    off the stack. The new stack at the end will look like (11, weight=1), (10, weight=7).
    """

    def __init__(self) -> None:
        self.monotone_stack = []

    def next(self, price: int) -> int:
        weight = 1
        while self.monotone_stack and self.monotone_stack[-1][0] <= price:
            weight += self.monotone_stack.pop()[1]
        self.monotone_stack.append((price, weight))
        return weight


if __name__ == '__main__':
    obj = StockSpannerV2()
    print(obj.next(100) == 1)
    print(obj.next(80) == 1)
    print(obj.next(60) == 1)
    print(obj.next(70) == 2)
    print(obj.next(60) == 1)
    print(obj.next(75) == 4)
    print(obj.next(85) == 6)
    print('-' * 15)

    obj = StockSpannerV2()
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
    print('-' * 15)

    obj = StockSpannerV2()
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
    print('-' * 15)

    obj = StockSpannerV2()
    print(obj.next(28) == 1)
    print(obj.next(14) == 1)
    print(obj.next(28) == 3)
    print(obj.next(35) == 4)
    print(obj.next(46) == 5)
    print(obj.next(53) == 6)
    print(obj.next(66) == 7)
    print(obj.next(80) == 8)
    print(obj.next(87) == 9)
    print(obj.next(88) == 10)
    print('-' * 15)

# last line of code
