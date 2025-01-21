blocks = int(input("Enter the number of blocks: "))
i = 0

while True:
    blocks -= i
    if blocks >= 0:
        height = i
    else:
        break
    i += 1
print("The height of the pyramid:", height)
