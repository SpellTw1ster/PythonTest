import random

kokos = random.randint(1, 99 + 1)
print("Random number is " + str(kokos))

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
password = ''

for number in range(kokos):
  number = number
  print(number)
  my_file = open(str(number) + '.txt', 'w')
  for n in range(1):
    password = ''
    for i in range(8):
      password += random.choice(chars)
    print(password)
    text_for_file = password
    my_file.write(text_for_file)
    my_file.close()