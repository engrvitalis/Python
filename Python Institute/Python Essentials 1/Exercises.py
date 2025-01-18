print("An upward pointing arrow implemented with 8 print statements")
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****\n")

print("An upward pointing arrow implemented with two print statements")
print("    *\n", "   * *\n", "  *   *\n", " *     *", sep="")
print("***   ***\n", "  *   *\n", "  *   *\n", "  *****", sep="")

print("Dubling the size of the arrow")
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("*****       *****")
print("    *       *")
print("    *       *")
print("    *       *")
print("    *       *")
print("    *********\n")

print("Duplicating the arrow")
print("        *          "*2)
print("       * *         "*2)
print("      *   *        "*2)
print("     *     *       "*2)
print("    *       *      "*2)
print("   *         *     "*2)
print("  *           *    "*2)
print(" *             *   "*2)
print("*****       *****  "*2)
print("    *       *      "*2)
print("    *       *      "*2)
print("    *       *      "*2)
print("    *********      "*2)

# Write a one-line piece of code, using the print() function, 
# as well as the newline and escape characters, 
# to match the expected result outputted on three lines.

# Expected output

# "I'm"
# ""learning""
# """Python"""

print("\"I\'m\"", "\"\"learning\"\"", "\"\"\"Python\"\"\"", sep="\n")

# Exercise 2.4.1.7
john = 3
mary = 5
adam = 6

total_apples = john + mary + adam

print(john, mary, adam, sep=",")
print("Total apples: ", total_apples)

# Exercise 2.4.1.9
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

# Exercise 2.4.1.10
x =  -1
x = float(x)
# write your code here
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

# Exercise 2.6.1.10
x = float(input("Enter value for x: "))

# Write your code here.
y = 1/(x + (1/(x + (1/(x + (1/x))))))

print("y =", y)