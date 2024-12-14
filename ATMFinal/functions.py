
import csv
import os






class AccountActions:
        WITHDRAW = 'Withdraw'
        DEPOSIT = 'Deposit'




        def __init__(self, name, amount,action):
            self.__account_name = name
            self.__amount = amount
            self.__action = action
            self.__action_label =''
            self.__new_row = []
            self.__current_balance = self.append_database(self.__account_name)


        def append_database(self, name):
            whole_dataset = []
            user_dataset = []
            file_path = 'database.csv'
            counter = 0
            search_name = name

            with open(file_path, 'a+', newline='') as file:
                file.seek(0)
                contents = csv.DictReader(file)
                new_content = csv.writer(file)

                for row in contents:
                    if row['Name'] == search_name:
                        counter += 1
                        user_dataset.append(row)
                dataset_index = user_dataset[counter - 1]
                self.__current_balance = float(dataset_index['Balance'])

                if self.__action == 1:
                    self.withdraw()
                if self.__action== 2:
                    self.deposit()

                self.set_balance(self.__current_balance)
                new_content_write= self.new_entry(self.__account_name,self.__action_label,self.__current_balance)
                new_content.writerow(new_content_write)
            return self.__current_balance


        def deposit(self):
            self.__action_label = AccountActions.DEPOSIT
            try:
                self.__amount = float(self.__amount)
                if self.__amount > 0:

                    self.__current_balance += self.__amount
                    self.set_balance(self.__current_balance)
                else:
                    raise TypeError
            except TypeError:
                raise TypeError("Values must be positive or trying to overdraw")


        def withdraw(self):
            self.__action_label = AccountActions.WITHDRAW
            try:
                self.__amount = float(self.__amount)
                if self.__amount > 0 and self.__amount < self.__current_balance:

                    self.__current_balance -= self.__amount
                    self.set_balance(self.__current_balance)
                else:
                    raise TypeError
            except TypeError:
                raise TypeError("Values must be positive or trying to overdraw")


        def set_balance(self, value):
            self.__current_balance = value
            return self.__current_balance   #returns

        def get_balance(self):
            return self.__current_balance # returns balance

        def new_entry(self, name, action, balance):
            self.__account_name = name
            self.__current_balance = balance
            self.__action_label = action
            self.__new_row.append(self.__account_name)          # creates new list for file
            self.__new_row.append(self.__action_label)
            self.__new_row.append(self.__current_balance)
            return self.__new_row

        def __str__(self):
            return f"{self.get_balance()}"




