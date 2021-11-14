var twoSum = function(nums, target) {
    let hashmap = {};
    for (let i = 0; i < nums.length, i++) {
        if(hashmap[nums[i]] >= 0){
	    return [hashmap[nums[i]], i]
	}
	hashmap[target-nums[i]] = i
    }
};
