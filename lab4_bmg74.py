

def main():
    names = open("names.txt", "r")
    print('--- Calling find_my_name ---')
    find_my_name(names)
    print('--- find_my_name finished ---')
    print('--- Calling appeared_first_in ---')
    print('Jessica first appeared in', appeared_first_in(names, 'Jessica'))
    print('Kharmen first appeared in', appeared_first_in(names, 'Kharmen'))
    print('Orchid first appeared in', appeared_first_in(names, 'Orchid'))
    print('C3P0 first appeared in', appeared_first_in(names, 'C3P0'))
    print('--- appeared_first_in finished ---')
    print('--- Calling get_summary_for_name ---')
    print(get_summary_for_name(names, 'Aragorn'))
    print(get_summary_for_name(names, 'Legolas'))
    print(get_summary_for_name(names, 'Leia'))
    print(get_summary_for_name(names, 'Kelly'))
    print('--- get_summary_for_name finished ---')

def find_my_name(names):
    names.seek(0)
    for line in names:
        if ",Eden," in line:
            print(line)

def appeared_first_in(names, name_value):
    names.seek(0)
    for line in names:
        if name_value in line:
            year = line.split(",")
            return year[0]
    return -1    

def get_summary_for_name(names, name_value):
    names.seek(0)
    first_year = appeared_first_in(names, name_value)
    total = 0 
    count = 0
    for line in names:
        items = line.split(",")
        if name_value == items[1]:
            total += int(items[3])
            count += 1
    return '{}: appears in {} years, first in {}, {:,} total babies'.format(
        name_value, count, first_year, total
        )
       

main()

