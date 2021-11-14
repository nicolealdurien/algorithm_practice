def two_sum(nums, target)
  checked = {}
  nums.each_with_index do |value, i| #for each index and associated value
    diff = target - value
    if checked[diff] # check if diff already exists in 'checked' hash
      return [checked[diff], i]
    else checked[value] = i  # if diff not in hash, add val as key and i as val
    end
  end
end
