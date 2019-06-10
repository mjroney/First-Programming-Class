def romeo():
    with open('/home/matt/Desktop/romeo.txt') as romeo:
        juliet = [line.rstrip('\n').lower().split(' ')
        for line in romeo]
    Juliet = [inner for outer in juliet for inner in outer]
    Romeo = []
    for x in Juliet:
        if x not in Romeo:
            Romeo.append(x)
    Romeo.sort()
    print(Romeo)
