numbers = [5, -3, 0, 12, -7, 0, 8, -1, 4, 0]

positive = 0
negative = 0
zero = 0

for n in numbers:
    if n > 0:
        positive += 1
    elif n < 0:
        negative += 1
    else:
        zero += 1

print(f"დადებითი: {positive}")
print(f"უარყოფითი: {negative}")
print(f"ნული: {zero}")