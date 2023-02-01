from tkinter import Tk, ttk
from tkinter import *

from PIL import Image, ImageTk

import requests
import json

# colors 
col0 = "#ffffff" # white
col1 = "#333333" # black
col2 = "#EB5D51" # red
col3 = "#FF00FF" # fuchsia

window = Tk()
window.geometry("300x320")
window.title('Currency Converter')
window.configure(bg=col1)
window.resizable(height = False, width = False)

# frames
top = Frame(window, width=300, height=60, bg=col2)
top.grid(row=0, column=0)

main = Frame(window, width=300, height=260, bg=col0)
main.grid(row=1, column=0)

# converter function
def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    # currencies
    currency1 = combo1.get()
    currency2 = combo2.get()
    amount = value.get()

    querystring = {"from":currency1,"to":currency2,"amount":amount}
    
    if currency2 == 'AUD':
        symbol = 'AUD $'
    elif currency2 == 'BRL':
        symbol = 'R$'    
    elif currency2 == 'CAD':
        symbol = 'CAD $'
    elif currency2 == 'EUR':
        symbol = '€'
    elif currency2 == 'GBP':
        symbol = '£'
    elif currency2 == 'INR':
        symbol = '₹'
    elif currency2 == 'MUR':
        symbol = 'Rs'
    elif currency2 == 'NZD':
        symbol = 'NZD $'
    elif currency2 == 'USD':
        symbol = '$'
    elif currency2 == 'ZAR':
        symbol = 'R'
        

    headers = {
        # TODO for you...
        # signup on Rapidapi (Free account) 
        # 'https://rapidapi.com/solutionsbynotnull/api/currency-converter18/' to generate API-Key
        # On the left, under "Search Endpoints", click "Convert"
        # On the right, under "Code Snippets", Python > Requests
        
        "X-RapidAPI-Key": "136fd937f2msh4e17faba1d9eb6ep1c73f7jsnc580a9b146cf", # Api Key
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # json data
    data= json.loads(response.text)

    # converted amount
    converted_amount = data["result"]["convertedAmount"]
    formatted = symbol + " {:,.2f}".format(converted_amount)

    result["text"] = formatted
    print(formatted)
    

# top frame
icon= Image.open('img/icon.png')
icon = icon.resize((40, 40))
icon = ImageTk.PhotoImage(icon)
app_name = Label(top, image= icon, 
                 compound=LEFT, text = "Currency Converter", 
                 height=5, padx=13, pady=30, anchor=CENTER, 
                 font=('Arial 16 bold'), bg=col2, fg=col0)

app_name.place(x=0, y=0)

# main frame
result = Label(main, text = " ", height=2, 
               width=16, pady=7, relief="solid", 
               anchor=CENTER, font=('Ivy 14 bold'), 
               bg=col0, fg=col1)

result.place(x=50, y=10)

currency = [ 'AUD', 'BRL', 'CAD', 'EUR', 'GBP', 'INR', 'MUR', 'NZD', 'USD', 'ZAR' ]

from_label = Label(main, text = " From ", 
                   height=1, width=8, pady=0, 
                   padx=0, relief="flat", anchor=NW, 
                   font=('Ivy 10 bold'), bg=col0, fg=col1)

from_label.place(x=48, y=90)

combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=('Ivy 12 bold'))
combo1[ 'values' ] = (currency)
combo1.place(x=50, y=115)

to_label = Label(main, text = " To ", 
                 height=1, width=8, pady=0, 
                 padx=0, relief="flat", anchor=NW, 
                 font=('Ivy 10 bold'), bg=col0, fg=col1)

to_label.place(x=158, y=90)

combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=('Ivy 12 bold'))
combo2[ 'values' ] = (currency)
combo2.place(x=160, y=115)

value = Entry(main, width=22, justify=CENTER, font=("Ivy 12 bold"), relief="solid")
value.place(x=50, y=155)

button = Button(main, text="Convert", width=19, 
                height=1, padx=5, bg=col2, fg=col0, 
                font=('Ivy 12 bold'), activebackground=col3, 
                command=convert)
button.place(x=50, y=210)

window.mainloop()