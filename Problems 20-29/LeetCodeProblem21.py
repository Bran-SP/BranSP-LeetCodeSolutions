# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:#Given the heads of two linked lists list1 and list2, merge them into one sorted linked list (you should do it by splicing the two, not just converting the lists to a big array)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        ans = ListNode()
        curr = ans #curr is a dummy node representing where we are. ans will be connected to the head of what we return
        
        while list1 and list2:#Run while both lists arent empty
            if list1.val <= list2.val:#If list1's value is smaller or equal, throw it onto our answer and move list1 forward
                curr.next = ListNode(list1.val, None)
                curr = curr.next
                list1 = list1.next
            else:#Otherwise do the above but for list2 and its current value
                curr.next = ListNode(list2.val, None)
                curr = curr.next
                list2 = list2.next
        
	#After finishing that while loop, place any remaining bits on the end.

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        else:#IF we meet this condition it means we had 2 empty lists
            return None

        return ans.next