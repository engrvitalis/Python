"""This program simulates the evolution of The Beatles' 
band lineup by creating an empty list, adding and removing members 
using the append(), del, and insert() methods, and prompting the user 
for input."""

# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3
for i in range(2):
    beatles.append(input("Enter a band member: "))
print("Step 3:", beatles)

# step 4
del beatles[-1]
del beatles[-1]
print("Step 4:", beatles)

# step 5
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))
