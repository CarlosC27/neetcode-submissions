class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    isConsecutive(nums: number[]): boolean {
        let low = nums[0], high = nums[0];
        const seen = new Set();
        for(const x of nums){
            if(seen.has(x)) return false;
            seen.add(x);
            if (x < low) low = x;
            if (x > high) high = x;
        }
        return high - low + 1 === nums.length;
    }
}
