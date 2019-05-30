def payroll():
    import math
    import decimal
    decimal.Decimal(value="2", context=None)
    import datetime
    now = datetime.datetime.now()
    print('\t\t\tSun Projects Payroll Processing')
    print(now.strftime(f"\t\t\t\t%B %d, %Y \n\t\t\t\t%a, %I:%M %p"))
    hrs = int(input('How many hours were \nworked this week? \t\t\t'))
    rt = float(input('What is the rate of pay? \t\t$'))
    gp = hrs * rt
    fw = gp * .20	# 20% Fed rate
    fica = gp * .08	# 8% FICA rate
    sw = gp * .02	# 2% State rate
    np = gp - (fw + sw + fica)
    print(f'\nGross Pay \t\t\t${gp:.2f}')
    print(f'Federal Tax Withholding (20%): \t\t-${fw:.2f} ')
    print(f'FICA Withholding (8%): \t\t\t-${fica:.2f}')
    print(f'State Tax Withholding (2%): \t\t\t-${sw:.2f}')
    print(f'Net Pay \t\t\t\t${np:.2f}')
