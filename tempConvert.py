def roney():
    temp = input('    What kind of temperature \n    are you trying to convert? \n    Please indicate with fahr, cel, or kel. \n    ')
    d = float(input('    What is the number of degrees \n    to be converted? \n    '))
    if (temp == 'fahr'):
        if (d) < -459.67 :
            print('The lowest Fahrenheit reading is -459.67 degrees. \nPlease enter another number.')
        elif (d) >= -459.67 :
            print('        Converted to Celsius:')
            print(            f"{(d-32)*(5/9):.1f}")
            print('        Converted to Kelvin:')
            print(            f"{((d-32)*(5/9))+273.15:.1f}")
    elif (temp == 'cel'):
        if d < -273.15 :
            print('The lowest Celsius reading is -273.15 degrees. \nPlease enter another number.')
        elif d >= -273.15 :
            print('        Converted to Fahrenheit:')
            print(            f"{(d*1.8)+32:.1f}")
            print('        Converted to Kelvin:')
            print(            f"{(d+273.15):.1f}")
    elif (temp == 'kel'):
        if d < 0 :
            print('The lowest Kelvin reading is 0 degrees. \nPlease enter another number.')
        elif d >= 0 :
            print('        Converted to Celsius:')
            print(            f"{(d-273.15):.1f}")
            print('        Converted to Fahrenheit:')
            print(            f"{((d-273.15)*1.8)+32:.1f}")





