def is_weekend(fDay):
    weekends = ['Saturday', 'Sunday']
    return bool([day for day in weekends if fDay in day])

def is_weekend2(fDay):
    return fDay in {'Sat', 'Sun'}

print(is_weekend2('Fri'))
