"""
Question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e.,
buy one and sell one share of the stock multiple times).

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
import unittest
from typing import List


def get_max_profit_multiple_purchases(stock_prices: List[int]) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if len(stock_prices) < 2:
        return 0

    previous_price = stock_prices[0]
    cur_lowest = stock_prices[0]
    cur_profit = 0
    total_profit = 0

    for price in stock_prices[1:]:
        # Run through the list one time. As long as the price is going down adjust the buy in price
        # Once the price starts going lower then we've hit a peak at the previous idx so we sell at that price.
        # After this has happened reset the prices to 0,0 and kick off another search for the next valley/peak

        if price <= previous_price:
            if cur_profit != 0:
                # Explicitly sold as a peak was met. Increment the index to populate the next element
                total_profit += cur_profit
                cur_profit = 0
            cur_lowest = price
        else:
            cur_profit = price - cur_lowest
        previous_price = price

    return total_profit + cur_profit


class TestCase(unittest.TestCase):
    def test_fluctuating_stock_price(self):
        test = [7, 1, 5, 3, 6, 4]
        # Buy at 1 sell at 5 buy at 3 sell at 6 ~> 4 + 3 ~> 7
        expected = 7
        actual = get_max_profit_multiple_purchases(stock_prices=test)
        self.assertEqual(expected, actual)

    def test_stock_price_only_drops(self):
        test = [5, 4, 3, 2, 1]
        # Would never be able to sell after buying at the lowest
        expected = 0
        actual = get_max_profit_multiple_purchases(stock_prices=test)
        self.assertEqual(expected, actual)

    def test_stock_price_only_rises(self):
        test = [1, 2, 3, 4, 5]
        # Buy at 1 and sell at EOD for 5. ~> 4 dollars profit
        expected = 4
        actual = get_max_profit_multiple_purchases(stock_prices=test)
        self.assertEqual(expected, actual)

    def test_stock_price_no_movement(self):
        test = [1, 1, 1, 1, 1, 1]
        # Would buy and never sell, and given that its a back fill test then profit must be >=0
        expected = 0
        actual = get_max_profit_multiple_purchases(stock_prices=test)
        self.assertEqual(expected, actual)

    def test_no_stock_data(self):
        test = []
        expected = 0
        actual = get_max_profit_multiple_purchases(stock_prices=test)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(verbosity=3)
