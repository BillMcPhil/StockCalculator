import yfinance as yf
from tkinter import *

stocks = []
num_of_shares = []
beginning_price = []

window = Tk()

label1 = Label(text="Enter a stock")
stock_entry = Entry()
stock_button = Button(text="Enter", command=lambda: add_stock(stock_entry.get()))

label1.pack()
stock_entry.pack()
stock_button.pack()

def add_stock(stock: str) -> None:
    global stock_button
    try:
        if yf.Ticker(stock).fast_info.last_price != None:
            stocks.append(stock)
            reset_page("How many did you buy?")
            stock_button = Button(text="Enter", command=lambda: add_shares(stock_entry.get()))
            stock_button.pack()
        else:
            print("Not a publicly traded stock")
    except:
        print("Not a publicly traded stock")

def calculate_money():
    money_spent = 0
    money_has = 0
    for i in range(len(stocks)):
        money_spent += beginning_price[i] * num_of_shares[i]
        ticker = yf.Ticker(stocks[i]).fast_info
        current_price = ticker.last_price
        money_has += num_of_shares[i] * current_price

    if money_has > money_spent:
        facts_label = Label(text=f"Congrats you made {money_has-money_spent} dollars")
        facts_label.pack()
    elif money_has == money_spent:
        facts_label = Label(text="You've made 0 dollars")
        facts_label.pack()        
    else:
        facts_label = Label(text=f"You lost $" + str((money_has - money_spent) * -1))
        facts_label.pack()
        
def add_shares(num: str) -> None:
    try:
        num = int(num)
        num_of_shares.append(num)
        reset_page("What was the buying price?")
        stock_button = Button(text="Enter", command=lambda: add_prices(stock_entry.get()))
        stock_button.pack()
    except:
        reset_page("How many did you buy?")
        stock_button = Button(text="Enter", command=lambda: add_shares(stock_entry.get()))
        stock_button.pack()
        error_label = Label(text="Must be an integer")
        error_label.pack()

def add_prices(num: str) -> None:
    try:
        num = float(num)
        beginning_price.append(num)
        reset_page("Enter another stock or continue")
        stock_button = Button(text="Another one", command=lambda: add_stock(stock_entry.get()))
        stock_button.pack()
        continue_button = Button(text="Continue", command=calculate_money)
        continue_button.pack()
    except:
        reset_page("What was the buying price?")
        stock_button = Button(text="Enter", command=lambda: add_prices(stock_entry.get()))
        stock_button.pack()
        error_label = Label(text="Must be an integer")
        error_label.pack()

def reset_page(label: str):
    global label1
    global stock_entry
    
    for widget in window.winfo_children():
        widget.destroy()
    
    label1 = Label(text=label)
    label1.pack()
    stock_entry = Entry()
    stock_entry.pack()

window.mainloop()


#if __name__ == '__main__':
    #get_finances()
    #calculate_money()


