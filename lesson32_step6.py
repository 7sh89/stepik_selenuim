assert abs(-42) == 42, 'Ошибка в расчетах'
print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))
print(f"{2+3}")


s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')
