# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        curr = l1
        while curr:
            num1 = num1*10+curr.val
            curr = curr.next
        
        num2 = 0
        curr = l2
        while curr:
            num2 = num2*10+curr.val
            curr = curr.next
        
        result = int(str(num1)[::-1])+int(str(num2)[::-1])
        if result == 0:
            return ListNode(0)
        demo = ListNode(0)
        curr = demo
        while result:
            node = ListNode(result%10)
            curr.next = node
            curr = curr.next
            result//=10
        
        return demo.next
