def exchange():
    import datetime
    now = datetime.datetime.now()
    timestamp = (now.strftime(f"%I:%M %p, %A, %B %d, %Y"))
    ratedate = 'Friday, May 24th 2019'
    from decimal import getcontext
    getcontext().prec = 3
    currency = ['\t\tCanadian Dollars', '\t\tEuro', '\tIndian Rupee', '\tJapanese Yen', '\tMexican Peso', '\tSouth African Rand', '\t\tGreat British Pound']
    rates = [0.744194, 1.120556, 0.014414, 0.009149, 0.052476, 0.069400, 1.271231]
    dollars = int(input('How much money would you like to convert?\n\t\t$'))
    exchanges = []
    exchanges = ['{:.3f}'.format(dollars/r) for r in rates]
    print('Exchanging ${} would yield:\n' .format(dollars))
    for a, b in zip(exchanges, currency):
        print(a, b)
    print('\n\tRates were updated {}. \n\nThis analysis conducted at: \n\n\t{}' .format(ratedate, timestamp))
