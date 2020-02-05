#!/usr/bin/python
import argparse
# Your function should return the maximum profit that can be made from a single buy and sell. You must buy first before selling
# For this problem, we essentially want to find the maximum difference between the smallest and largest prices in the list of prices, but we also have to make sure that the max profit is computed by subtracting some price by another price that comes _before_ it; it can't come after it in the list of prices.
# So what if we kept track of the `current_min_price_so_far` and the `max_profit_so_far`?
# For example, `find_max_profit([1050, 270, 1540, 3800, 2])` should return 3530, which is the maximum profit that can be made from a single buy and then sell of these stock prices.


# def find_max_profit(prices):
# current_min_value = prices[0]
# print("current_min_value", current_min_value)

# # PLANNING:
# # loop through list of stock prices
# # keep track of current_min_price_so_far
# # for each index, subtract that index value - current_min_price_so_far
# # return whichever profit is the highest from ^ calculation
# # How do we make sure the current min value's index comes before current index value?
# # If current_min_value[x] > [x] pass?
# for x in range(0, len(prices)-1):
#     # print(x) - x is index number
#     # print(prices[x])  # prices[x] is each value at that index number
#     # print(prices[x+1]) # prices[x+1] is each value at index number to the right of it

#     if current_min_value > prices[x+1]:
#         # if int(current_min_value[x]) > int([x]):
#         #     print("Cant sell before you buy")
#         # else:
#         current_min_value = prices[x+1]
#         print("current_min_value updated", current_min_value)
#     max_profit_so_far = prices[x] - current_min_value
#     print("max_profit_so_far", max_profit_so_far)

# print(find_max_profit([1050, 270, 1540, 3800, 2]))

# if __name__ == '__main__':
#     # This is just some code to accept inputs from the command line
#     parser = argparse.ArgumentParser(
#         description='Find max profit from prices.')
#     parser.add_argument('integers', metavar='N', type=int,
#                         nargs='+', help='an integer price')
#     args = parser.parse_args()

#     print("A profit of ${profit} can be made from the stock prices {prices}.".format(
#         profit=find_max_profit(args.integers), prices=args.integers))


# PLANNING:
# loop through prices array
# print out values at each index of the prices array
# keep track of current min value as you go through array
# keep track of current max value as you go through array
# make sure the current min value index comes BEFORE the current max value index
# max profit = current max value - current min value


def find_max_profit(prices):
    print('prices[0]', prices[0])  # 1050
    current_min_value = prices[0]
    print("current_min_value", current_min_value)  # 1050
    for x in range(0, len(prices)-1):
        print('x', x)  # 0, 1, 2, 3, 4
        print("prices[x]", prices[x])  # 1050, 270, 1540, 3800, 2
    # keep track of current min value as you go through array
    # if next value is smaller than current value, update current min value to next value's index
        if prices[x+1] < prices[x]:
            current_min_value = prices[x+1]
            print("current min value", current_min_value)


print(find_max_profit([1050, 270, 1540, 3800, 2]))
