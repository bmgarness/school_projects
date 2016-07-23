seconds = int(input('Enter number of seconds to convert: '))

output = '{} day(s), {} hour(s), {} minute(s), and {} second(s).'

secs_in_min = 60
secs_in_hour = secs_in_min * 60 # 60 minutes per hour
secs_in_day = secs_in_hour * 24 # 24 hours per day

days = 0
hours = 0
minutes = 0

if seconds >= secs_in_day:
    days = seconds // secs_in_day # Interger Division
    seconds = seconds % secs_in_day # Remainder Divsion

if seconds >= secs_in_hour:
    hours = seconds // secs_in_hour # Interger Divsion
    seconds = seconds % secs_in_hour # Remainder Divsion

if seconds >= secs_in_min:
    minutes = seconds //secs_in_min # Interger Divsion
    seconds = seconds % secs_in_min # Remainder Divsion

print(output. format(days, hours, minutes, seconds))
