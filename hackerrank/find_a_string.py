def count_substring(string, sub_string):
    l = len(sub_string)
    c = 0
    for i in range(len(string)-l+1):
        if string[i:i+l] == sub_string:
            c += 1
    return c

print(count_substring('ABCDCDC', 'CDC'))