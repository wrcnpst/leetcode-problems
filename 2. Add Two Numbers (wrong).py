# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = []
        global quotient

        def find_a(l1, l2):
            if len(l1) >= len(l2):
                return l1, l2
            else:
                return l2, l1
        
        a, b = find_a(l1, l2)
        quotient = 0

        for i in range(len(a)+1):
            if i == len(a):
                if quotient != 0:
                    ret.append(quotient)
                break
            
            if i > len(b)-1:
                a_item = a[i]
                b_item = 0
            else:
                a_item = a[i]
                b_item = b[i]
            
            temp_add = a_item + b_item + quotient
            if temp_add >= 10:
                quotient = temp_add // 10
                remainder = temp_add % 10
                ret.append(remainder)
            else:    
                ret.append(temp_add)
                quotient = 0
                
        print(ret)
        return ret
            
            

# Create an instance of Solution
s = Solution()

# Define the lists
# l1 = [2,4,3]
# l2 = [5,6,4]

# l1 = [0]
l2 = [0]

l1 = [9,9,9,9,9,9,9]
# l2 = [9,9,9,9]

# l1 = [9,9,9,9]
# l2 = [9,9,9,9]

# Call the method
s.addTwoNumbers(l1, l2)