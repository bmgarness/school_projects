#Exam 3
#Benjamin Garness
#bmg74

class car:
    
    def __init__(self, make, model, year, price):
        self.__make = make
        self.__model = model
        self.__year = int(year)
        self.__price = float(price)
        
    def __str__(self):
        return '{} {} {} - ${:,.2f}'.format(
            self.__year, self.__make, self.__model, self.__price   
        )
        
    def get_make(self):
        return self.__make
        
    def get_model(self):
        return self.__model
        
    def get_year(self):
        return self.__year

    def get_price(self):
        return self.__price
        
    def set_price(self, price):
        self.__price = float(price)
        
    def set_year(self, year):
        self.__year = int(year)
