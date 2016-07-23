' ' ' Homework assignment with three problems. Write three functions'''

import random

def main():
    weekly_sales_analysis()
    calories = [calorie_counter(10, 20, 30), calorie_counter(15, 5, 25), calorie_counter(2, 40, 15)]
    sorted(calories, reverse=True)
    print(calories)
    number_list = []
    for i in range(1, 51):
        number_list.append(i)
    my_number = random.randint(0,50)
    bigger_and_smaller_than(number_list, my_number)




def weekly_sales_analysis():
    sales = []
    for i in range(1, 8):
        daily_sale = float(input('Enter Sales for Day ' + format(i) + ': '))
        sales.append(daily_sale) #Should create a list of 7 elements
    total_sales = sum(sales)
    average_daily_sales = sum(sales)/len(sales)
    highest_sales = max(sales)
    lowest_sales = min(sales)
    print(sales)
    print('Total weekly sales: ${:.2f}'.format(total_sales))
    print('Average daily sales: ${:.2f}'.format(average_daily_sales))
    print('Highest sales day: ${:.2f}'.format(highest_sales))
    print('Lowest sales day: ${:.2f}'.format(lowest_sales))
    # Tried to combine all print statements, ran into problem with to many arguments.



def calorie_counter(fat, protein, carbs):
    total_calories = (9*fat) + (4*protein) + (4*carbs)
    return total_calories


def bigger_and_smaller_than(number_list, my_number):
    numbers_bigger = []
    numbers_smaller = []
    for i in number_list:
        if i > my_number:
            numbers_bigger.append(i)
        elif i < my_number:
            numbers_smaller.append(i)
    print('Numbers bigger than {}: '.format(my_number), numbers_bigger)
    print('Numbers smaller than {}: '.format(my_number), numbers_smaller)

main()
