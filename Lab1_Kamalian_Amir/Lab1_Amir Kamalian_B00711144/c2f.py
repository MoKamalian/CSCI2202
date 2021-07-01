

def temp_converter(celsius):
    temp_f = (9 / 5) * int(celsius) + 32
    return temp_f


while True:
    temp_in_c = input('Enter temp in Celsius: ')
    temp_in_f = temp_converter(celsius=temp_in_c)
    print(f'{temp_in_c} degrees Celsius is {temp_in_f} degrees Fahrenheit')


