class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i1 = 0
        i2 = 0
        n1 = 0
        n2 = 0
        len1 = len(nums1)
        len2 = len(nums2)
        len_total = len1 + len2
        len_half  = len_total // 2 + 1
        for x in range(len_half):
            if i1<len1 and i2<len2:
                if nums1[i1] <= nums2[i2]:
                    n1 = n2
                    n2 = nums1[i1]
                    i1 += 1
                else:
                    n1 = n2
                    n2 = nums2[i2]
                    i2 += 1
            elif i2<len2:
                n1 = n2
                n2 = nums2[i2]
                i2 += 1
            else:
                n1 = n2
                n2 = nums1[i1]
                i1 += 1
        if len_total % 2:
            return float(n2)
        else:
            return (n1 + n2)/2