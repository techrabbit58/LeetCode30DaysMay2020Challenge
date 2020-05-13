"""
Week 2, Day 6: Remove K Digits

Given a non-negative integer num represented as a string,
remove k digits from the number so that the new number is
the smallest possible.

N o t e

    - The length of num is less than 10002 and will be ≥ k.
    - The given num does not contain any leading zero.

E x a m p l e s

    Input: num = "1432219", k = 3
    Output: "1219"
    Explanation: Remove the three digits 4, 3, and 2 to form
                 the new number 1219 which is the smallest.

    Input: num = "10", k = 2
    Output: "0"
    Explanation: Remove all the digits from the number and it
                 is left with nothing which is 0.

    Input: num = "10200", k = 1
    Output: "200"
    Explanation: Remove the leading 1 and the number is 200.
                 Note that the output must not contain leading
                 zeroes.

"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        return None


if __name__ == '__main__':
    print(Solution().removeKdigits('10', 2) == "0")
    print(Solution().removeKdigits('10200', 1) == "200")
    print(Solution().removeKdigits('1432219', 3) == "1219")

# last line of code
