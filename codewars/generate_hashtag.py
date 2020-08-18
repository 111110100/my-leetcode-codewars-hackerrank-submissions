'''
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
'''

def generate_hashtag(s):
    q = s.split(' ')
    t = '#'
    for e in q:
        t += e.capitalize()
    return False if len(t) == 1 or len(t) > 140 else t

print(generate_hashtag(' Hello there thanks for trying my Kata'))
print(generate_hashtag('    Hello     World   '))
print(generate_hashtag('                                  '))
print(generate_hashtag('we' * 100))

'''
def generate_hashtag(s):
    ans = '#'+ str(s.title().replace(' ',''))
    return s and not len(ans)>140 and ans or False

def generate_hashtag(s):
    return '#' + s.title().replace(' ','') if 0<len(s.strip())<140 else False

generate_hashtag=lambda d:(lambda b:d>''<b==b[:139]and'#'+b)(d.title().replace(' ',''))
'''