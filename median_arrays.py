import math


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        no_of_iter = 0
        total_length = len(nums1) + len(nums2)
        median_length = math.ceil(total_length/2)
        index_nums1 = 0
        index_nums2 = 0
        combined_arr = []
        while no_of_iter != median_length and (
              index_nums1 < len(nums1) and index_nums2 < len(nums2)):
            if nums1[index_nums1] < nums2[index_nums2]:
                combined_arr.append(nums1[index_nums1])
                index_nums1 += 1
                no_of_iter += 1
            else:
                combined_arr.append(nums2[index_nums2])
                index_nums2 += 1
                no_of_iter += 1
        print (combined_arr)
        while no_of_iter < median_length:
            if index_nums1 == len(nums1):
                combined_arr.append(nums2[index_nums2])
                index_nums2 += 1
                no_of_iter += 1
            elif index_nums2 == len(nums2):
                combined_arr.append(nums1[index_nums1])
                index_nums1 += 1
                no_of_iter += 1
        print (combined_arr)
        if total_length % 2 == 0:
            if index_nums1 == len(nums1):
                combined_arr.append(nums2[index_nums2])
            elif index_nums2 == len(nums2):
                combined_arr.append(nums1[index_nums1])
            elif nums1[index_nums1] < nums2[index_nums2]:
                combined_arr.append(nums1[index_nums1])
            else:
                combined_arr.append(nums2[index_nums2])
            return (combined_arr[-1] + combined_arr[-2])/2
        else:
            return combined_arr[-1]


solution1 = Solution()
print(solution1.findMedianSortedArrays([1, 2, 3, 5], []))
