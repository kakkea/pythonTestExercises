def ex2(string):
    newstring = ''
    for letter in string:
        newstring = letter + newstring
    newstring = newstring.upper()
    return (newstring)
word = 'Hello World'
print (ex2(word))
