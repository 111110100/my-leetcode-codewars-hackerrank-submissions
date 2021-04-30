/**
 * @param {number[]} nums
 * @return {boolean}
 */
var checkPossibility = function(nums) {
    let l = nums.length
    if (l < 2) {
        return true
    }
    
    let t = 0
    for (let i = 1; i < l; i++) {
        if (nums[i-1] > nums[i]) {
            t++
            
            if (i == 1 || nums[i-2] <= nums[i]) {
                 nums[i-1] = nums[i]
            } else {
                nums[i] = nums[i-1]
            }
            
            if (t > 1) {
                return false
            }
        }
    }
    return true
};
