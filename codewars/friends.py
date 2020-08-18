'''
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
'''

def namelist(f):
    s = ''
    names = []
    for v in f:
        e = v['name'].replace(' ', '').replace('&', ',')
        if ',' in e:
            e = e.split(',')
        if type(e) == list:
            for n in e:
                if n not in names:
                    names.append(n)
        else:
            if e not in names:
                names.append(e)
    for i,v in enumerate(reversed(names)):
        if i == 0:
            s = v
        elif i == 1:
            s = v + ' & ' + s
        else:
            s = v + ', ' + s
    return s

print(namelist([ {'name': 'Homer'}, {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))
print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))
print(namelist([ {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Bart & Bart'} ]))
print(namelist([ {'name': 'Maggie'} ]))
print(namelist([ {'name': 'Bart & Bart'} ]))

'''
def namelist(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]),
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''


def namelist(names):
    if len(names)==0: return ''
    if len(names)==1: return names[0]['name']
    return ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']

def namelist(names):
  return ", ".join([name["name"] for name in names])[::-1].replace(",", "& ",1)[::-1]

def namelist(names):
    return " ".join([names[i]["name"] + (" &" if i == len(names)-2 else "" if i==len(names)-1 else ",") for i in range(len(names))])

def namelist(names):
    nameList = [elem['name'] for elem in names]
    return ' & '.join(', '.join(nameList).rsplit(', ', 1))

namelist=lambda a:' & '.join(', '.join(d['name']for d in a).rsplit(', ',1))
'''
