class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int nums1Length = nums1.length;
        int nums2Length = nums2.length;
        // make sure that nums1 is the shortest array
        if (nums1Length > nums2Length) {
            return findMedianSortedArrays(nums2, nums1);
        };

        // Pointers
        int low = 0;
        int high = nums1Length;
    
        while ( low <= high ) {
            // part_1 and part_2 are the total of elems for each partition
            int part1 = (low + high) / 2; 

            // +1 to compensate when dealing with odd length of merged arrays
            int part2 = ((nums1Length + nums2Length + 1) / 2) - part1;
            
            // max value on left side of partition for each array.
            // -infinity is used when left side of part is empty, in order to make sure that left side elems
            // are always lesser than right side, specially when cross comparing
            double maxLeftNums1 = (part1 == 0) ? Double.NEGATIVE_INFINITY : nums1[part1 -1];
            double maxLeftNums2 = (part2 == 0) ? Double.NEGATIVE_INFINITY : nums2[part2 -1];

            // min value of right side of partition for each array
            // +infinity is used when right side of part is empty, in order to make sure that right side elems
            // are always greater than left side, specially when cross comparing
            double minRightNums1 = (part1 == nums1Length) ? Double.POSITIVE_INFINITY : nums1[part1];
            double minRightNums2 = (part2 == nums2Length) ? Double.POSITIVE_INFINITY : nums2[part2];

            // cross compare max and min values from each side of the partition. left side elems must be
            // lesser than right side
            if (maxLeftNums1 <= minRightNums2 && maxLeftNums2 <= minRightNums1) {
                //compute and return median
                if ((nums1Length + nums2Length) % 2 == 0){
                    // even length of merged arrays
                    return (Math.max(maxLeftNums1, maxLeftNums2) + Math.min(minRightNums1, minRightNums2)) / 2;
                } else {
                    // odd length
                    return Math.max(maxLeftNums1, maxLeftNums2);
                }
            } else if (maxLeftNums1 > minRightNums2) {
                // decrease high pointer -> part1 will be 1 elem smaller
                high = part1 - 1;
            } else {
                // increase low pointer -> part1 will be 1 elem bigger
                low = part1 + 1;
            }
        }
        return 0;
    }
}
