#Exam 3
#Benjamin Garness
#bmg74

import car

def main():
    c = [car.car('Ford', 'F-150', '2010', '1599.99'),
         car.car('Jeep', 'Wrangler', '2001', '7500.99'),
         car.car('Honda', 'Accord', '2016', '31299.00'),
         car.car('Chevrolet', 'Corvette', '1969', '89950.79')]

    for i in c:
        print(i)

    for i in c:
        year = i.get_year()
        if 2006 >= year:
            cost = i.get_price()
            new_cost = (cost * .9) 
            i.set_price(new_cost)

    c[1].set_year(2002)
    print(c[1])
    
main()
    
