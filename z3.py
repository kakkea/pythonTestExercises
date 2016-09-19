def ex3(string):
    words = 0
    sents = 0
    for let in string:
        if let == ' ':
            words += 1
        if let == '.':
            sents += 1
    words += 1
    return (words,sents)
while True:
    print (ex3(input()))
