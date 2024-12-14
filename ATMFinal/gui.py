from tkinter import *
import csv

import functions
from functions import *

class Gui:
    def __init__(self, window):
        self.window = window

        #Name
        self.frame_name = Frame(self.window)
        self.input_name = Entry(self.frame_name, width=20)
        self.label_name = Label(self.frame_name, text='Name')
        self.label_name.pack(side='left')
        self.input_name.pack(padx=5, side='left')
        self.frame_name.pack(anchor='w', padx=10, pady=10)

        # Amount
        self.frame_amount = Frame(self.window)
        self.input_amount = Entry(self.frame_amount, width=20)
        self.label_amount = Label(self.frame_amount, text='Amount')
        self.label_amount.pack(side='left')
        self.input_amount.pack(padx=5, side='left')
        self.frame_amount.pack(anchor='w', padx=10, pady=10)

        # Deposit or Withdraw
        self.frame_radio = Frame(self.window)
        self.radio_answer = IntVar()
        self.radio_answer.set(0)
        self.radio_withdraw = Radiobutton(self.frame_radio, text='Withdraw', variable=self.radio_answer, value=1)
        self.radio_deposit = Radiobutton(self.frame_radio, text='Deposit', variable=self.radio_answer, value=2)
        self.radio_withdraw.pack(side = 'left')
        self.radio_deposit.pack(side='left')
        self.frame_radio.pack()

        # enter button
        self.frame_enter = Frame(self.window)
        self.button_enter = Button(self.frame_enter, text="SAVE", command=self.submit)
        self.button_enter.pack()
        self.frame_enter.pack()

        # bottom lable
        self.frame_bottomtext = Frame(self.window)
        self.lable_bottomtext = Label(self.frame_bottomtext, text='Please fill out all values')
        self.lable_bottomtext.pack()
        self.frame_bottomtext.pack()


    def submit(self):

        try:
            name = self.input_name.get().strip()
            amount = self.input_amount.get().strip()
            action = self.radio_answer.get()


            if action == 1:
                self.lable_bottomtext.config(text=f'Withdraw successful! Remaining amount: {functions.AccountActions(name,amount,action)}')
            elif action == 2:
                self.lable_bottomtext.config(text=f'Deposit successful! New balance: {functions.AccountActions(name,amount,action)}')
            else:
                self.lable_bottomtext.config(text='No operation selected')
        except TypeError:
            self.lable_bottomtext.config(text='Values must be positive or trying to overdraw')





