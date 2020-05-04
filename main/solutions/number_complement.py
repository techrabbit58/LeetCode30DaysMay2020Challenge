"""
LeetCode 30-Day Challenge, May 2020, Week 1, Day 4

Given a positive integer, output its complement number. The complement strategy is 
to flip the bits of its binary representation.

Example 1:

    Input: 5
    Output: 2
    Explanation: The binary representation of 5 is 101 (no leading zero bits), 
        and its complement is 010. So you need to output 2.

Example 2:

    Input: 1
    Output: 0
    Explanation: The binary representation of 1 is 1 (no leading zero bits),
        and its complement is 0. So you need to output 0.

Every non-negative integer N has a binary representation.  For example, 5 can be
represented as "101" in binary, 11 as "1011" in binary, and so on.  Note that
except for N = 0, there are no leading zeroes in any binary representation.

The complement of a binary representation is the number in binary you get when
changing every 1 to a 0 and 0 to a 1.  For example, the complement of "101" 
in binary is "010" in binary.

For a given number N in base-10, return the complement of it's binary
representation as a base-10 integer.

Example 3:

    Input: 7
    Output: 0
    Explanation: 7 is "111" in binary, with complement "000" in binary, which
    is 0 in base-10.

Example 4:

    Input: 10
    Output: 5
    Explanation: 10 is "1010" in binary, with complement "0101" in binary,
    which is 5 in base-10.

N o t e s

    1. The given integer is guaranteed to fit within the range of a 32-bit
       signed integer.
    2. You could assume no leading zero bit in the integer’s binary
       representation.

"""


def findComplement(num: int) -> int:
    return int(''.join([str((int(b) + 1) % 2) for b in bin(num)[2:]]), 2)


def findComplement_v2(num: int) -> int:
    if not num:
        return 1
    return ~num & sum([2 ** b for b in reversed(range((num).bit_length()))])


def findComplement_v3(num: int) -> int:
    return ~num & max(1, 2 ** (num).bit_length() - 1)


def findComplement_v4(num: int) -> int:
    return num ^ max(1, 2 ** (num).bit_length() - 1)


if __name__ == '__main__':
    print(findComplement_v4(5), 2)
    print(findComplement_v4(1), 0)
    print(findComplement_v4(7), 0)
    print(findComplement_v4(10), 5)
    print(findComplement_v4(0), 1)
    print(findComplement_v3(0), 1)
    print(findComplement_v2(0), 1)
    print(findComplement(0), 1)

# last line of code
