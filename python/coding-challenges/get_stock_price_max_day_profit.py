"""
Question: https://www.interviewcake.com/question/python3/stock-price
First, I wanna know how much money I could have made yesterday if I'd been trading Apple stocks all day.

So I grabbed Apple's stock prices from yesterday and put them in a list called stock_prices, where:

The indices are the time (in minutes) past trade opening time, which was 9:30am local time.
The values are the price (in US dollars) of one share of Apple stock at that time.
So if the stock cost $500 at 10:30am, that means stock_prices[60] = 500.

Write an efficient function that takes stock_prices and returns the best profit I could have made from one purchase
and one sale of one share of Apple stock yesterday.
"""
import unittest


def get_max_profit(stock_prices, can_lose=True):
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
            get_max_profit([])

    def test_error_with_one_price(self):
        with self.assertRaises(Exception):
            get_max_profit([1])

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1], can_lose=True)
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day_no_losing_days(self):
        # Don't buy if there was no uptick for that day.
        actual = get_max_profit([9, 7, 4, 1], can_lose=False)
        expected = 0
        self.assertEqual(actual, expected)

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
