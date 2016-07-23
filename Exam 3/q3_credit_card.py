#Exam 3
#Benjamin Garness
#bmg74

class CreditCard:

    def __init__(self, card_type, card_holder, interest_rate, balance):
        self.__card_type = card_type
        self.__card_holder = card_holder
        self.__interest_rate = float(interest_rate)
        self.__balance = 0.0

    def __str__(self):
        self.__interest_rate = self.__interest_rate * 100
        return '{}\'s {} card has an interest rate of {}% and a balance of ${:.2f}'.format(
            self.__card_holder, self.__card_type, self.__interest_rate, self.__balance
            )

    def get_card_type(self):
        return self.__card_type

    def get_card_holder(self):
        return self.__card_holder

    def get_interest_rate(self):
        return self.__interest_rate

    def get_balance(self):
        return self.__balance

    def set_card_holder(self, card_holder):
        self.__card_holder = card_holder

    def set_interest_rate(self, interest_rate):
        self.__interest_rate = float(interest_rate)

    def charge(self, charge):
        if charge > 0:
            self.__balance += charge

    def bill(self):
        new_balance = (self.__balance * self.__interest_rate) + self.__balance
        self.__balance = new_balance
        print('Please pay ${:.2f}'.format(self.__balance))

    
