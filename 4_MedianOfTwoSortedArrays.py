class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # A will always contain the smallest list
        if len(nums1) < len(nums2):
            A,B = nums1,nums2
        else:
            B,A = nums1,nums2

        # total length for where the midpoint is
        total_len = len(A)+len(B)
        half = total_len//2

        # l and r pointers for the binary search
        l,r = 0,len(A)-1

        while True:
            a_mid = (l+r)//2
            b_mid = (half - a_mid) - 2 # have to do -2 because the both arrays start at 0 so -1 per array

            a_left = A[a_mid] if a_mid >= 0 else float("-infinity")
            a_right = A[a_mid+1] if (a_mid + 1) < len(A) else float("infinity")

            b_left = B[b_mid] if b_mid >= 0 else float("-infinity")
            b_right = B[b_mid + 1] if (b_mid + 1) < len(B) else float("infinity")

            # partition is now correct
            if a_left <= b_right and b_left <= a_right:
                # odd
                if total_len % 2:
                   return min(a_right,b_right)
            
                return (max(a_left,b_left) + min(a_right,b_right)) / 2
            elif a_left > b_right:
                r = a_mid - 1
            else:
                l = a_mid + 1
                
                



