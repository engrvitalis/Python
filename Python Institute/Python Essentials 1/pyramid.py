blocks = int(input("Enter the number of blocks: "))

for i in range(1, blocks+1):
    blocks -= i
    if blocks >= 0:
        height = i
    else:
        break
print("The height of the pyramid:", height)
