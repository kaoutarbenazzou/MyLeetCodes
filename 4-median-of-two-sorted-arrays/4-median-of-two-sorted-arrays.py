class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merge(a1, a2):
               a3 = []
               a1_len = len(a1)
               a2_len = len(a2)
               a1_index = 0
               a2_index = 0
               for _ in range(a1_len + a2_len):
                   if a1_index >= a1_len:
                       a3.extend(a2[a2_index:])
                       return a3
                   elif a2_index >= a2_len:
                       a3.extend(a1[a1_index:])
                       return a3
                   a1_item = a1[a1_index]
                   a2_item = a2[a2_index]
                   if a1_item < a2_item:
                       a3.append(a1_item)
                       a1_index+= 1
                   elif a2_item < a1_item:
                       a3.append(a2_item)
                       a2_index += 1
                   else:
                       a3.extend([a1_item] * 2)
                       a1_index += 1
                       a2_index += 1
               return a3
        num=merge(nums1,nums2)
        if len(num)%2==1:
            median=num[len(num)//2]
        else:
            median=(num[(len(num)//2)-1]+num[(len(num)//2)])/2
        return median