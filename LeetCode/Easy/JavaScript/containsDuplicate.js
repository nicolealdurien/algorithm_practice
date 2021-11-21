const containsDuplicate = nums => {
    let set = new Set(nums)
    return set.length != nums.length
}
