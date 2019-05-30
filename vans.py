def vans():
    p = int(input('How many people will \nbe attending the event? \n'))
    s = int(input('How many seats are \navailable in each van? \n'))
    v = int(p//s)
    r = int(p%s)
    print('There will be', v, '\ncompletely full vans, and another ', r, '\npeople will need to \nfind their own way.')
