'''
Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

Rules for a smiling face:

Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
Every smiling face must have a smiling mouth that should be marked with either ) or D
No additional characters are allowed except for those mentioned.

Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]

Example
countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
Note
In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). Order of the face (eyes, nose, mouth) elements will always be the same.
'''

def countSmileys(a):
    v = 0
    for e in a:
        if len(e) > 1 and len(e) < 4:
            if e[0] in ':;':
                if (len(e) == 3 and e[2] in ')D' and e[1] in '-~') or (len(e) == 2 and e[1] in ')D'):
                    v += 1
    return v

print(countSmileys([':)', ';(', ';}', ':-D']))
print(countSmileys([';D', ':-(', ':-)', ';~)']))
print(countSmileys([';]', ':[', ';*', ':$', ';-D']))

'''
def count_smileys(arr):
    eyes = [":", ";"]
    noses = ["", "-", "~"]
    mouths = [")", "D"]
    count = 0
    for eye in eyes:
        for nose in noses:
            for mouth in mouths:
                face = eye + nose + mouth
                count += arr.count(face)
    return count

def count_smileys(arr):
    valid = ":) :D :-) :-D :~) :~D ;) ;D ;-) ;-D ;~) ;~D".split()
    return sum(face in valid for face in arr)

def count_smileys(arr):
    return len(list(filter(lambda x: x in [':D',':~D',':-D',';D',';~D',';-D',':)',':~)',':-)',';)',';~)',';-)'],arr)))

def count_smileys(arr):
    possible_faces = [":-)", ":-D", ":~)", ":~D", ":)", ":D",
                      ";-)", ";-D", ";~)", ";~D", ";)", ";D"]
    return sum([1 if face in possible_faces else 0 for face in arr])

'''
