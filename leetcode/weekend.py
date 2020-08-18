def is_weekend(fDay):
    weekends = ['Saturday', 'Sunday']
    return bool([day for day in weekends if fDay in day])

def is_weekend_set(day):
    weekends = {'Sat', 'Sun'}
    return day in weekends

print(is_weekend_set('Fri'))
