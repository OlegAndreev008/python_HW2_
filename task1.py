import random

count = int(input("количество монет "))
help_list = []
count_zero = 0
count_one = 0
for i in range(count):
    help_list.append(random.randint(0, 1))
for i in help_list:
    if i == 0:
        count_zero += 1
    else:
        count_one += 1
print(help_list)
print(count_zero, count_one)
if count_zero < count_one:
    print(count_zero)
else:
    print(count_one)