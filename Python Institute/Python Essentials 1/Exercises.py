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

# Exercise 2.6.1.11
hour = 12 # int(input("Starting time (hours): "))
mins = 17 # int(input("Starting time (minutes): "))
dura = 59 # int(input("Event duration (minutes): "))
# find a total of all minutes
total_minutes = hour * 60 + mins + dura
# find a number of hours hidden in minutes and update the hour
end_hour = (total_minutes // 60) % 24
end_minute = total_minutes % 60

print(end_hour, ":", end_minute, sep='')

# Exercise 3.1.11 (Tax calculator)
# A tax calculator that computes the Personal Income Tax (PIT) 
# based on a citizen's income, applying an 18% rate with a tax relief 
# for incomes up to 85,528 thalers, and a fixed tax amount plus a 
# 32% rate on the surplus for higher incomes, rounding the result to 
# the nearest whole thaler while ensuring no negative tax values.
income = float(input("Enter the annual income: "))

#
# Write your code here.
#
if income <= 85528: tax = .18 * income - 556.2
else: tax = 14839.2 + .32 * (income - 85528)

if tax < 0: tax = 0.0
tax = round(tax, 0)
print("The tax is:", tax, "thalers")