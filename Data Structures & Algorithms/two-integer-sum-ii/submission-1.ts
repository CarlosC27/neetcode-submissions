class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers: number[], target: number): number[] {
        let l = 0;
        let r = numbers.length-1;
        let indexes = [0,0];

        while(l < r){
            if(numbers[l] + numbers[r] > target ){
                r -=1;
            }
            else if(numbers[l] + numbers[r] < target){
                l += 1;
            }
            else {
                indexes[0] = l+1;
                indexes[1] = r+1;
                break;
            }
        }
        return indexes;
    }
}
