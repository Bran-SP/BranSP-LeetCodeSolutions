# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:#Given an array of k linked lists, each sorted in ascending order, merge them all into one sorted linked list
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #edge cases
        if not lists or len(lists) == 0:
            return None
        
        #Function for merging
        def merge2Lists(l1, l2):
            temp = ListNode()
            tail = temp

            while l1 and l2:#Algorithm for sorting the 2 linked lists together
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next

	    #If one list still remains, throw it onto the end
            if l1:
                tail.next = l1
            if l2:
                tail.next = l2
            
            return temp.next

        while(len(lists) > 1):#num of lists will shrink as we merge
            merged = []

            for i in range(0, len(lists), 2):#split lists into 2s and call merge function on them
                l1 = lists[i]
                if i < len(lists) - 1:
                    l2 = lists[i + 1]
                else:
                    l2 = None
                merged.append(merge2Lists(l1, l2))

            lists = merged

        return lists[0]
