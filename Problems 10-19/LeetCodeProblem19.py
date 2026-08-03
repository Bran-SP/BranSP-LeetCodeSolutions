# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:#Given the head of a linked list, remove the nth node from the end of the list and return the head
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp, rem = head, head
        count = 0

	#Additional goal of doing things in 1 iteration
	#It'd be easy to do it in 2 because you do O(n) runthrough
	#to find the count and then do count - n -1 to get right before the one to remove 

	#This gets temp n-1 steps ahead of rem
        for i in range(1, n):
            temp = temp.next
            count += 1

	#This keeps going until temp is the last node and rem is right before the one to remove
        while temp.next is not None:
            temp = temp.next
            count += 1
            if temp.next is not None:
                rem = rem.next
        
        if rem == head and rem.next is None:#If it's a 1 node list, kill it
            return None
        elif rem == head and count < n:#If the element to remove is the head, kill it (n condition makes sure you dont kill head when head was just the one before the target)
            head = head.next
        else:#Otherwise do this to remove the target node
            rem.next = rem.next.next

        return head