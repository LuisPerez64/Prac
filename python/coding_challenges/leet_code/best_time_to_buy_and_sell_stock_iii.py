"""
Question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii
Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


Constraints:
    1 <= prices.length <= 3 * 10 ^ 4
    0 <= prices[i] <= 10 ^ 4
"""
from typing import List


def get_stock_price_max_profit_with_transaction_limit(prices: List[int], max_transactions=1002) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Building off of the previous problems solution and enacting a constraint
    that the max_profit can only take into account  max_transactions.

    Cant approach it in the same manner as the previous problems as the total peak/valleys need to be measured out

    Method for handling this would be Iterating over the list and for each value find the absolute peaks
    Until a lower value is met than an existing lowest keep ingesting and positioning the peak
    Keep a dict of all of these value/peaks and seek the absolutes from there.

    Constraint is that there are no overlapping peaks in the calculation so local maxima can be ignored
    (can the same be done for local minima?)
    """

    if len(prices) < 2:
        return 0

    profits = [0] * (len(prices))
    last_sell_idx = -1

    # Dynamic programming solution would entail getting the max profit from the buy point at cur_main_idx until a lower
    # element is found (short circuit the operation at this point to trim down the cycles)
    for buy_idx in range(len(prices) - 1):
        if buy_idx < last_sell_idx:
            continue

        buy_price = prices[buy_idx]
        for sell_idx in range(buy_idx + 1, len(prices)):
            sell_price = prices[sell_idx]
            cur_profits = sell_price - buy_price
            if sell_price <= buy_price:
                last_sell_idx = sell_idx - 1
                break  # Found a smaller buy in price so no need to continue evaluating at the current buy in
            profits[buy_idx] = max(profits[buy_idx], cur_profits)
        else:
            # This is met if there is no selling price that is lower than the current buy in, so the delta is maxed.
            break
    max_profit = sum(sorted(profits, reverse=True)[:max_transactions])
    return max_profit


def get_stock_price_max_profit_with_transaction_limit_pulled_from_example(prices, k=2):
    if len(prices) < 2:
        return 0
    n, k = len(prices), 2

    B = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]
    if k > len(prices) // 2:
        return sum(x for x in B if x > 0)

    dp = [[0] * (k + 1) for _ in range(n - 1)]
    mp = [[0] * (k + 1) for _ in range(n - 1)]

    dp[0][1], mp[0][1] = B[0], B[0]

    for i in range(1, n - 1):
        for j in range(1, k + 1):
            dp[i][j] = max(mp[i - 1][j - 1], dp[i - 1][j]) + B[i]
            mp[i][j] = max(dp[i][j], mp[i - 1][j])

    return max(mp[-1])

# print(get_stock_price_max_profit_with_transaction_limit([3, 3, 5, 0, 0, 3, 1, 4], 2))
# print(get_stock_price_max_profit_with_transaction_limit([6, 1, 3, 2, 4, 7], 2))
# print(get_stock_price_max_profit_with_transaction_limit([7,1,5,3,6,4]))
# print(get_stock_price_max_profit_with_transaction_limit_pulled_from_example([3, 3, 5, 0, 0, 3, 1, 4], 2))
# print(get_stock_price_max_profit_with_transaction_limit_pulled_from_example([7,1,5,3,6,4], 1002))
