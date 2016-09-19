def isfloat(a):
    try:
        float(a)
        return True
    except ValueError:
        return False
def ex4():
    x = input ('Введите число.')
    while isfloat(x) == False :
        x = input ('Введите число!')
    summ = 0
    powe = 1
    for num in x :
        if num == '-' or num == '.':
            continue
        else:
            summ += int(num)
            powe *= int(num)
    return (summ, powe)
print (ex4())
