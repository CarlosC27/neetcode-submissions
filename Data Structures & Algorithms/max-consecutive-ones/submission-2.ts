class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMaxConsecutiveOnes(nums: number[]): number {
        let tempMax =0;
        let max = 0;
        if(nums.length === 1){
            if(nums[0] === 1){
                max =1;
                return max;
            }
        } 
        for(let i =0; i < nums.length; i++){
            if(nums[i] == 0){
                if(max < tempMax){
                    max = tempMax
                }
                tempMax=0;
                continue;
            }
            tempMax += 1;
        }

        if (tempMax > max){
            max = tempMax
        }
        return max
    }
}
