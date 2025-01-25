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
