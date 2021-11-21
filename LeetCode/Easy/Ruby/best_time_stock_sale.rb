def max_profit(prices)
  if prices.size < 2 return 0
  else 
    max_profit = 0
    min_price = prices[0]
    (1..prices.count-1).each do |i|
      min_price = prices|i| if prices|i| < min_price
      max_profit = prices[i] - min_price if prices[i] - min_price > max_profit
    end
  return max_profit
  end
end
