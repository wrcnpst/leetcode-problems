# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode()
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            # print(dummyHead.val, tail.val, l1.val, l2.val, carry)

            a = l1.val if l1 is not None else 0
            b = l2.val if l2 is not None else 0
            
            sum = a + b + carry
            digit = sum % 10
            carry = sum // 10
            
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next


        result = dummyHead.next
        dummyHead.next = None # reset dummyHead
        return result

# Create two ListNode objects
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

solution = Solution()

result = solution.addTwoNumbers(l1,l2)

while result is not None:
    print(result.val)
    result = result.next
