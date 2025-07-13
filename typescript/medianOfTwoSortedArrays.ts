function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
    const nums1Length: number = nums1.length;
    const nums2Length: number = nums2.length;
    // make sure that nums1 is the shortest array
    if (nums1Length > nums2Length) {
        return findMedianSortedArrays(nums2, nums1);
    };
    
    //pointers
    let low: number = 0;
    let high: number = nums1Length;
    
    while ( low <= high ) {
        // part_1 and part_2 are the total of elems for each partition
        let part1: number = Math.floor((low + high) / 2);
        
        // +1 to compensate when dealing with odd length of merged arrays
        let part2: number = Math.floor((nums1Length + nums2Length + 1) / 2) - part1;
            
        // max value on left side of partition for each array.
        // -infinity is used when left side of part is empty, in order to make sure that left side elems
        // are always lesser than right side, specially when cross comparing
        let maxLeftNums1: number = part1 === 0 ? -Infinity : nums1[part1 - 1];
        let maxLeftNums2: number = part2 === 0 ? -Infinity : nums2[part2 - 1];

        // min value of right side of partition for each array
        // +infinity is used when right side of part is empty, in order to make sure that right side elems
        // are always greater than left side, specially when cross comparing
        let minRightNums1: number = part1 === nums1Length ? Infinity : nums1[part1];
        let minRightNums2: number = part2 === nums2Length ? Infinity : nums2[part2];
        // cross compare max and min values from each side of the partition. left side elems must be
        // lesser than right side
        if (maxLeftNums1 <= minRightNums2 && maxLeftNums2 <= minRightNums1){
            //compute and return median
            if ((nums1Length + nums2Length) % 2 === 0){
                // even length of merged arrays
                return (Math.max(maxLeftNums1, maxLeftNums2) + Math.min(minRightNums1, minRightNums2)) / 2;
            } else {
                // odd length
                return Math.max(maxLeftNums1, maxLeftNums2);
            };
        } else if (maxLeftNums1 > minRightNums2) {
            // decrease high pointer -> part1 will be 1 elem smaller
            high = part1 - 1;
        } else {
            // increase low pointer -> part1 will be 1 elem bigger
            low = part1 + 1;
        };
    };
};
