import yfinance as yf
from tkinter import *

stocks = []
num_of_shares = []
beginning_price = []
window = Tk()

def find_stock(stock):
    if yf.Ticker(stock).fast_info.last_price != None:
        stocks.append(stock)

    else:
        print("Not a publicly traded stock")

def get_finances():
    while True:
        while True:
            find_stock(input("Please enter a stock "))
            num = input("How many shares of this stock did you buy? ")

            try:
                num = int(num)
                num_of_shares.append(num)

            except:
                print("Must be a valid integer")
                print("\n")
                continue

            break

        while True:
            price = input("What was the price you bought the shares at? ")

            try:
                price = float(price)
                beginning_price.append(price)

            except:
                print("Must be a valid price")
                print("\n")
                continue

            break

        exit = input("Enter 1 to continue or any other key to enter another stock ")

        if exit == "1":
            break

def calculate_money():
    money_spent = 0
    money_has = 0
    for i in range(len(stocks)):
        money_spent += beginning_price[i] * num_of_shares[i]
        ticker = yf.Ticker(stocks[i]).fast_info
        current_price = ticker.last_price
        money_has += num_of_shares[i] * current_price

    if money_has > money_spent:
        print("Congrats! You've gained $" + str(money_has - money_spent))
    elif money_has == money_spent:
        print("You've gained 0 dollars")
    else:
        print("You lost $" + str((money_has - money_spent) * -1))

if __name__ == '__main__':
     get_finances()
     calculate_money()


