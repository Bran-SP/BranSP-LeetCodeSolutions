class Solution:#Given two sorted arrays nums1 and nums 2 of size m and n respectively, return the median of the two sorted arrays
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #merge sort with the first part already done for us? That's O(n + m) unfortunately

        l1 = len(nums1)
        l2 = len(nums2)

        #just some code that handles base cases quickly
        if l1 == 0 and l2 == 0:
            return 0
        elif l1 == 0:
            if l2 % 2 == 0:
                return ((nums2[l2 // 2 - 1] + nums2[l2 // 2]) / 2)
            else:
                return nums2[l2 // 2]
        elif l2 == 0:
            if l1 % 2 == 0:
                return ((nums1[(l1 // 2) - 1] + nums1[l1 // 2]) / 2)
            else:
                return nums1[l1 // 2]

        #we want an O(log(n+m)) solution. Try a binary search inspired example

        #first we make it so that A always points to the smaller of the two
        A, B = nums1, nums2
        if l1 > l2:
            A, B = nums2, nums1

        med = (l1 + l2) // 2 #Let's store this now so we can quit early if possible

        l, r = 0, len(A) - 1 #the bounds of the part of A we care about, we'll cut it in half
        #each time to achieve that binary search effect

        while True:
            i = (l + r) // 2 #midpoint of A
            j = med - i - 2 #We only need "mid" number of elements to reach the median, so
            #starting partition point of B should reflect that

            #Set values on either side of partition and add catches for if they're OoB
            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i + 1] if (i + 1) < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if (j + 1) < len(B) else float('inf')

            #Idea is that if Aleft < Bright and Bleft < Aright, because of how we defined the
            #partitions, either Aright or Bright should be the median (though if the total
            #size is even, it's only one of the median values, the other being the greater of
            #Aleft and Bleft)

            if Aleft <= Bright and Bleft <= Aright:
                #odd solution
                if (l1 + l2) % 2 == 1:
                    return min(Aright, Bright)
                else: #even solution
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1 #If partition point too far in, cut left side of A window into 2
                #halves
            else:
                l = i + 1 #Only other case is Bleft is too big, so we shift A window right in
                #order to shift B window left