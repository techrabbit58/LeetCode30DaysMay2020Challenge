"""
Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking
about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

    Input: 1->2->3->4->5->NULL
    Output: 1->3->5->2->4->NULL

Example 2:

    Input: 2->1->3->5->6->4->7->NULL
    Output: 2->3->6->7->1->5->4->NULL

Note:

    (1) The relative order inside both the even and odd groups should remain as it was in the input.
    (2) The first node is considered odd, the second node even and so on ...

"""
from solutions.list_node import ListNode


class Solution:
    """My own approach. More variables than necessary, as it looks."""
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        actual = head
        even = head.next
        is_even = False
        odd = head
        while actual.next:
            node = actual.next
            actual.next = actual.next.next
            actual = node
            if is_even:
                odd = odd.next
            is_even = not is_even
        odd.next = even
        return head


class SolutionV2:
    """Adapted from the discussion."""
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd_head = odd = ListNode(-1)
        even_head = even = ListNode(-1)
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if even else None
        odd.next = even_head.next
        return odd_head.next


class SolutionV3:
    """Adapted from the LeetCode solution page. The solution were shown in Java."""
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head


if __name__ == '__main__':
    obj = SolutionV3()

    example = None
    expected = None
    print('result:  ', obj.oddEvenList(example), '\nexpected:', expected, end='\n\n')

    example = ListNode(1)
    expected = ListNode(1)
    print('result:  ', obj.oddEvenList(example), '\nexpected:', expected, end='\n\n')

    example = ListNode(1, ListNode(2))
    expected = ListNode(1, ListNode(2))
    print('result:  ', obj.oddEvenList(example), '\nexpected:', expected, end='\n\n')

    example = ListNode(1, ListNode(2, ListNode(3)))
    expected = ListNode(1, ListNode(3, ListNode(2)))
    print('result:  ', obj.oddEvenList(example), '\nexpected:', expected, end='\n\n')

    example = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    expected = ListNode(1, ListNode(3, ListNode(2, ListNode(4))))
    print('result:  ', obj.oddEvenList(example), '\nexpected:', expected, end='\n\n')

    example = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    expected = ListNode(1, ListNode(3, ListNode(5, ListNode(2, ListNode(4)))))
    print('result:  ', obj.oddEvenList(example), '\nexpected:', expected, end='\n\n')

    example = ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4))))))
    expected = ListNode(2, ListNode(3, ListNode(6, ListNode(1, ListNode(5, ListNode(4))))))
    print('result:  ', obj.oddEvenList(example), '\nexpected:', expected, end='\n\n')

    example = ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7)))))))
    expected = ListNode(2, ListNode(3, ListNode(6, ListNode(7, ListNode(1, ListNode(5, ListNode(4)))))))
    print('result:  ', obj.oddEvenList(example), '\nexpected:', expected, end='\n\n')

# last line of code
