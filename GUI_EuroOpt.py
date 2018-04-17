import tkinter as tk 
from tkinter import ttk
import euro_option_pricer as eop


def mainCal(typ, asset_price, strike_price, mature_time, vol, rate, repo_q):
    if typ == 'Call Option':
        tp = 'c'
    elif typ == 'Put Option':
        tp = 'p'
    
    asset_price = float(asset_price)
    strike_price = float(strike_price)
    mature_time = float(mature_time)
    vol = float(vol)
    rate = float(rate)
    repo_q = float(repo_q)

    eopx = eop.euro_opt(tp, asset_price, strike_price, mature_time, vol, rate,repo_q)

    text8['text'] = eopx.value()


def main():
    win = tk.Tk()
    win.title("European Option Pricer")


    text0 = tk.Label(win, text = 'Choose Asset Type: ').grid(row=0) 
    typex = tk.StringVar()
    chooseType = ttk.Combobox(win, width = 26, textvariable = typex)
    chooseType['values'] = ('Call Option', 'Put Option')
    chooseType.grid(row=0, column=1)


    text1 = tk.Label(win, text = 'Asset Price: ').grid(row=1) 
    priceA = tk.StringVar()
    entry1 = tk.Entry(win, textvariable = priceA) 
    entry1.grid(row=1, column=1)


    text2 = tk.Label(win, text = 'Strike Price: ').grid(row=2) 
    priceK = tk.StringVar()
    entry2 = tk.Entry(win, textvariable = priceK)
    entry2.grid(row=2, column=1)


    text3 = tk.Label(win, text = 'Maturity Time: ').grid(row=3) 
    timeM = tk.StringVar()
    entry3 = tk.Entry(win, textvariable = timeM)
    entry3.grid(row=3, column=1)


    text4 = tk.Label(win, text = 'Volatility: ').grid(row=4) 
    vol = tk.StringVar()
    entry4 = tk.Entry(win, textvariable = vol)
    entry4.grid(row=4, column=1)


    text5 = tk.Label(win, text = 'Risk Free Rate: ').grid(row=5)
    rate = tk.StringVar()
    entry5 = tk.Entry(win, textvariable = rate)
    entry5.grid(row=5, column=1)


    text6 = tk.Label(win, text = 'Repo Rate: ').grid(row=6) 
    repoR = tk.StringVar()
    entry6 = tk.Entry(win, textvariable = repoR)
    entry6.grid(row=6, column=1)


    text7 = tk.Label(win, text = 'Price:').grid(row=7) 
    text8 = tk.Label(win)
    text8.grid(row=7, column=1)


    button = tk.ttk.Button(win, text="Calculate", command=lambda : mainCal(typex.get(), priceA.get(), priceK.get(), timeM.get(), vol.get(), rate.get(), repoR.get()))
    button.grid()


    win.mainloop()

