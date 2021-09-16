weight = float(input('Weight: '))

value = input("(K)g or (L)bs: ")

if value.upper() == 'K':
    converted = weight / 0.45
    print('Weight in Lbs: ' + str(converted))

else:
    converted = weight * 0.45
    print('Weight in Kg: ' + str(converted))
