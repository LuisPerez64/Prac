"""
Question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
 design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
import unittest


def get_max_profit_single_purchase(stock_prices, can_lose=True):
    # Calculate the max profit
    if len(stock_prices) < 2:
        # Initial clause removes the possibility of an empty set of array prices.
        raise Exception("Not enough data to evaluate the profit.")
    lowest_buy = stock_prices[0]
    max_profit = -float('inf') if can_lose else 0

    # Time complexity = O(n) must iterate over the full array.
    for cur_idx in range(1, len(stock_prices)):
        cur_price = stock_prices[cur_idx]

        sell_profit = cur_price - lowest_buy
        max_profit = max(max_profit, sell_profit)

        # If a lower buy in price is met then try to get a better buy
        # in as any price after this point must be better than the previous low.
        lowest_buy = min(lowest_buy, cur_price)

    # If no profit is able to be made then return 0 as no profit could have been made that day.
    # Should it return a - value in this case?
    return max_profit


# Tests
class Test(unittest.TestCase):

    def test_error_with_empty_prices(self):
        with self.assertRaises(Exception):
            get_max_profit_single_purchase([])

    def test_error_with_one_price(self):
        with self.assertRaises(Exception):
            get_max_profit_single_purchase([1])

    def test_price_goes_down_all_day(self):
        actual = get_max_profit_single_purchase([9, 7, 4, 1], can_lose=True)
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day_no_losing_days(self):
        # Don't buy if there was no uptick for that day.
        actual = get_max_profit_single_purchase([9, 7, 4, 1], can_lose=False)
        expected = 0
        self.assertEqual(actual, expected)

    def test_price_goes_up_then_down(self):
        actual = get_max_profit_single_purchase([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit_single_purchase([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit_single_purchase([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit_single_purchase([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
