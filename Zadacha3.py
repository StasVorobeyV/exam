#Вводится 2 числа с клавиатуры (от 1 до 20). Так же генерируется 2 числа рандомно.
#Посчитать, сколько раз пара введенных чисел с клавиатуры окажется больше
#рандомной пары. Проверку выполнить 7 раз.


number1: int = int(input('number1 = '))
number2: int = int(input('number2 = '))

for _ in range(7):
    number3: int = random.randint(1, 20)
    number4: int = random.randint(1, 20)