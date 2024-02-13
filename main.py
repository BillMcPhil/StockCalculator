import yfinance as yf
from tkinter import *

#Initialize lists to store stock info
stocks = []
num_of_shares = []
beginning_price = []

# Initialize Tkinter elements
window = Tk()

label1 = Label(text="Enter a stock")
stock_entry = Entry()
stock_button = Button(text="Enter", command=lambda: add_stock(stock_entry.get()))

label1.pack()
stock_entry.pack()
stock_button.pack()

# Ensures the stock exists and then adds it to the list
def add_stock(stock: str) -> None:
    global stock_button
    try:
        # Make sure the inputted stock exists
        if yf.Ticker(stock).fast_info.last_price != None:
            # Add the stock to the list and update the UI
            stocks.append(stock)
            reset_page("How many did you buy?")
            stock_button = Button(text="Enter", command=lambda: add_shares(stock_entry.get()))
            stock_button.pack()
        else:
            print("Not a publicly traded stock")
    except:
        print("Not a publicly traded stock")
        
# Add the number of shares to the list
def add_shares(num: str) -> None:
    try:
        # Convert the number of shares into an int, then add to the list
        num = int(num)
        num_of_shares.append(num)
        
        # Update the page
        reset_page("What was the buying price?")
        stock_button = Button(text="Enter", command=lambda: add_prices(stock_entry.get()))
        stock_button.pack()
        
    except:
        # If the number of shares bought doesn't convert then throw an error to the user
        reset_page("How many did you buy?")
        stock_button = Button(text="Enter", command=lambda: add_shares(stock_entry.get()))
        stock_button.pack()
        
        error_label = Label(text="Must be an integer")
        error_label.pack()

# Add the buying price to the list
def add_prices(num: str) -> None:
    try:
        # Convert input to a float and add it to the list
        num = float(num)
        beginning_price.append(num)
        
        # Update the UI 
        reset_page("Enter another stock or continue")
        # Button to add another stock
        stock_button = Button(text="Add Stock", command=lambda: add_stock(stock_entry.get()))
        stock_button.pack()
        # Button to continue
        continue_button = Button(text="Continue", command=calculate_money)
        continue_button.pack()
        
    except:
        # If the user enters a wrong value then give them an error
        reset_page("What was the buying price?")
        stock_button = Button(text="Enter", command=lambda: add_prices(stock_entry.get()))
        stock_button.pack()
        error_label = Label(text="Must be an integer")
        error_label.pack()

# Calculate and display the money gained/lost
def calculate_money():
    money_spent = 0
    money_has = 0
    
    # For every stock get the money spent on buying, and then get the current stock price
    for i in range(len(stocks)):
        money_spent += beginning_price[i] * num_of_shares[i]
        ticker = yf.Ticker(stocks[i]).fast_info
        current_price = ticker.last_price
        money_has += num_of_shares[i] * current_price

    # Check to see how much money the user has gained/lost and output result
    if money_has > money_spent:
        facts_label = Label(text=f"Congrats you made ${money_has-money_spent}")
        facts_label.pack()
    elif money_has == money_spent:
        facts_label = Label(text="You've made 0 dollars")
        facts_label.pack()        
    else:
        facts_label = Label(text=f"You lost ${money_spent-money_has}")
        facts_label.pack()

# Reset the UI elements in the window
def reset_page(label: str):
    global label1
    global stock_entry
    
    # Destroy every element in the page
    for widget in window.winfo_children():
        widget.destroy()
    
    # Add the updated UI to the page
    label1 = Label(text=label)
    label1.pack()
    stock_entry = Entry()
    stock_entry.pack()

window.mainloop()

