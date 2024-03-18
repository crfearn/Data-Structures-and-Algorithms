# Charles Fearn
# CSCI 433
# Project 2

def max_price(stockPrices):
    n = len(stockPrices)
    if n < 2:
        print("to little data to trade")
        return
    # Initialize array to store best day to buy, sell, and maximum profit
    buy = 0
    sell = 1
    maxProfit = stockPrices[sell] - stockPrices[buy]

    # loop to find the best buy/sell day
    for i in range(1, n):
        if stockPrices[i] < stockPrices[buy]:
            buy = i
        elif stockPrices[i] - stockPrices[buy] > maxProfit:
            sell = i
            maxProfit = stockPrices[sell] - stockPrices[buy]

    print(f"The stock price list is {stockPrices}")

    if maxProfit > 0:
        print(f"The best purchasing day is day {buy + 1} when stock prices is {stockPrices[buy]}")
        print(f"The selling day is day {sell + 1} when stock price is {stockPrices[sell]}")
        print(f"The maximum profit is {maxProfit:.2f}")
    else:
        print("The maximum profit is 0. Trading stock is not suggested.")


# test cases
stockPrices1 = [7, 1, 5, 3, 6, 4]
stockPrices2 = [9, 8, 7, 6, 5, 4]
stockPrices3 = [2, 4, 11, 1, 5, 8]
stockPrices4 = [2, 4, 1, 11, 5, 8]

max_price(stockPrices1)
max_price(stockPrices2)
max_price(stockPrices3)
max_price(stockPrices4)
