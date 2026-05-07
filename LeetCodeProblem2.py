# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:#Given two linked lists representing two positive integers (digits in reverse order), add the two numbers and return sum as a linked list
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        length = 1
        length2 = 1
        dum_lis = l1
        dum_lis2 = l2
	#get the length of both numbers
        while dum_lis.next != None:
            dum_lis = dum_lis.next
            length+=1

        while dum_lis2.next != None:
            dum_lis2 = dum_lis2.next
            length2+=1

        ans = 0
        enc_ans = []

	#create cases for nums being equal or one being bigger than the other
        if length > length2:
            for j in range(length2):
                ans += (l1.val + l2.val)*10**j
                l1 = l1.next
                l2 = l2.next
            for k in range(length2, length):#extra digits
                ans += (l1.val)*10**k
                l1 = l1.next
        elif length < length2:
            for j in range(length):
                ans += (l1.val + l2.val)*10**j
                l1 = l1.next
                l2 = l2.next
            for k in range(length, length2):#extra digits
                ans+= (l2.val)*10**k
                l2 = l2.next
        else:
            for j in range(length):
                ans += (l1.val + l2.val)*10**j
                l1 = l1.next
                l2 = l2.next
	#list comp get the int as an array and reverse it
        enc_ans = [int(x) for x in str(ans)]
        enc_ans =  enc_ans[::-1]

	#deal with edge cases
        if len(enc_ans) == 0:
            return ListNode()
        elif len(enc_ans) == 1:
            return ListNode(enc_ans[0], None)
        else:
            head = ListNode(enc_ans[0], ListNode(enc_ans[1], None))
            fin_ans = head
            for l in range(1, len(enc_ans)):
                fin_ans.next = ListNode()
                fin_ans = fin_ans.next
                fin_ans.val = enc_ans[l]
                fin_ans.next = None
        return head