n = int(input('Введите номер вашего места в плацкартном вагоне: '))
print()
if n > 36:
    print('Ваше место - боковое.')
elif n % 2:
    print('Ваше место в кепу внизу.')
else:
    print('Ваше место в купе наверху.')
