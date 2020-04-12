import random

words = 'Только вперёд, мой анальный капитан', 'Ваши враги соснут хуйца', 'Саня хуйни не скажет', 'Руслан-бой клёвый такой'
slogan = ''

print('Генератор слоганов')
a = input('Введите слово (название) : ')
for i in range(1):
    slogan += random.choice(words)
    print('Слоган: ', slogan)