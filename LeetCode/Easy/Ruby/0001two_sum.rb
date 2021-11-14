def two_sum(nums, target)
  (0..nums.length-1).each do |i|
    pointer = i + 1
    (pointer..nums.length-1).each do |j|
      if nums[i] + nums[j] == target
        return [i, j]
      end
    end
  end
end
