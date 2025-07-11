class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        # make sure that nums1 is the shortest array
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        # pointers
        low = 0
        high = m

        while low <= high:
            # part_1 and part_2 are the total of elems for each partition
            part1 = (low + high) // 2
            # +1 to compensate when dealing with odd length of merged arrays
            part2 = (m + n + 1) // 2 - part1
            
            # max value on left side of partition for each array.
            # -infinity is used when left side of part is empty, in order to make sure that left side elems
            # are always lesser than right side, specially when cross comparing
            max_left_1 = float('-inf') if part1 == 0 else nums1[part1 - 1]
            max_left_2 = float('-inf') if part2 == 0 else nums2[part2 - 1]

            # min value of right side of partition for each array
            # +infinity is used when right side of part is empty, in order to make sure that right side elems
            # are always greater than left side, specially when cross comparing
            min_right_1 = float('inf') if part1 == m else nums1[part1]
            min_right_2 = float('inf') if part2 == n else nums2[part2]

            # cross compare max and min values from each side of the partition. left side elems must be
            # lesser than right side
            if max_left_1 <= min_right_2 and max_left_2 <= min_right_1:
                #compute and return median
                if (m + n) % 2 == 0:
                    # even elngth of merged arrays
                    return (max(max_left_1,max_left_2) + min(min_right_1, min_right_2)) / 2
                else:
                    # odd length
                    return max(max_left_1,max_left_2)
            elif max_left_1 > min_right_2:
                # decrease high pointer -> part1 will be 1 elem smaller
                high = part1 - 1
            else:
                # increase low pointer -> part1 will be 1 elem bigger
                low = part1 + 1
