numbers = input()
numbers = [int(x) for x in numbers.split()]

if sorted(numbers) == numbers:
    print('Да')
else:
    print('Нет')
