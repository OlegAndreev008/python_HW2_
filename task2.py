# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

summ = int(input("введите сумму чисел "))
multiplic = int(input("введите произведение чисел "))
for i in range(1000):
    for j in range(1000):
        if i + j == summ and i * j == multiplic and i < j:
            print(i)
            print(j)

