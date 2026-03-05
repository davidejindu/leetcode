class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
    need to get partion of left and right array

    get total of arrays and the half of the two arrays

    then get half of smaller array and then get from total half - smaller half

    then the rest can go to the longer array 

    so then in total you would get the half of both arrays by doing this

    if the end of smaller array you got half is smaller than the larger array + 1 then valid
    then check vice versa

    after that if the len of array is odd return the min of halfs of two array
    else add max of left partion of two arrays by the min of right partition array   

nums1 = [1,3], nums2 = [2]

total = 3
half = 1

A = [2] B = [1,3]

        """

        total = len(nums1) + len(nums2)
        half = total // 2

        A, B = nums1, nums2
        if len(B) < len(A):
            A,B = B,A

        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i+1] if (i+1) < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j+1] if (j+1) < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    return (max(Bleft, Aleft) + min(Bright, Aright)) / 2
                else:
                    return min(Bright, Aright)

            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1


        
