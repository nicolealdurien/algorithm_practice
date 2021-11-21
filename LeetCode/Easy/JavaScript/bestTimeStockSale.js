const maxProfit = prices => {
    if (prices.length < 2) return 0
    else {
    let profit = 0;
    let lowestPrice  = prices[0];
    for(let i = 1; i < prices.length; i++) {
        lowestPrice = Math.min(prices[i], lowestPrice);
        profit = Math.max(profit, prices[i] - lowestPrice);
    }
    return profit;
    }
};
