# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        res = 0
        nums1.sort()
        mid = len(nums1) // 2
        if len(nums1) % 2 == 1:
            res = nums1[mid]
        else:
            print(mid-1, mid)
            res = (nums1[mid-1] + nums1[mid]) / 2

        return float(res)
