'''
returns the best profit I could have made from one purchase and one sale of one share of Apple stock yesterday.

'''

def get_purchase_price(stock_prices):

    lowest_price = stock_prices[0]
    low_index = 0

    for index, price in enumerate(stock_prices):
        if price < lowest_price:
            lowest_price = price
            low_index = index

    return (lowest_price, low_index)

def get_sale_price(stock_prices):

    highest_price = stock_prices[0]

    for price in stock_prices:
        if price > highest_price:
            highest_price = price

    return highest_price



def get_max_profit(stock_prices):
    
    purchase, index = get_purchase_price(stock_prices)
    sale = get_sale_price(stock_prices[index+1:])
   
    return (abs(sale - purchase))


def main():

    apple_stock_prices = [10, 7, 5, 8, 11, 9]
    google_stock_prices = [11, 2, 5, 4]
    print(get_max_profit(apple_stock_prices))
    print(get_max_profit(google_stock_prices))

if __name__ == "__main__":
    main()