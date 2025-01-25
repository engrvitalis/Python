ls = [8, 10, 6, 2, 4]  # list to sort
swapped = True

while swapped:
    swapped = False
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]:
            swapped = True  # a swap happened
            ls[i], ls[i + 1] = ls[i + 1], ls[i]

print(ls)