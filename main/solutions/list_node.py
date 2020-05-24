"""
A node type for singly linked lists.
"""


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

    def __str__(self):
        s = [f'{self.val} -> ']
        walker = self.next
        while walker is not None:
            s.append(f'{walker.val} -> ')
            walker = walker.next
        s.append('None')
        return ''.join(s)

# last line of code
