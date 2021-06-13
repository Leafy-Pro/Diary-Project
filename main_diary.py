'''Created by Leafy-Pro ¯\_(ツ)_/¯'''

import datetime

username = input("Enter Your Name: ") # Taking name of the user

# Creating username file

with open("usernames.txt", "a+"):
    pass

# Reading username file

with open("usernames.txt") as u:
    username_read = u.read()

# Registering name (if needed)

if username in username_read:
    pass
else:
    print("You don't have written anything in this program before.\nPlease enter your name below to create an account.")
            
    username1 = input("Enter Your Name To Register: ")
    username = username1

    # Working with username file

    with open("usernames.txt", "a") as s:
        s.write(f"{username1}, ") # Saves username to register

# Taking multiple lines of input

print("\nNow you can start writing your diary. Press enter two times to save your thoughts...\n\n")

lines = []
while True:
    line = input() # Takes input
    if line:
        lines.append(line) # Appends input sentences in lines list
    else:
        break # If no input then breaks
text = '\n'.join(lines) # Joins the elements of list lines by a separator

ex = str(datetime.datetime.now()) # Prints the current time with date
ex1 = ex.split(" ") # Splits time and date

ex2_1 = ex1[0].split("-") # Splits date
ex2_2 = ex1[1].split(".") # Splits millisecond in time
ex2_2_1 = ex2_2[0].split(":") # Splits time

# Deciding hour, minute and seconds

if int(ex2_2_1[0]) > 12:
    hour = int(ex2_2_1[0]) - 12
else:
    hour = int(ex2_2_1[0])
minute = int(ex2_2_1[1])
second = int(ex2_2_1[2])

# Deciding date, month and year

date = int(ex2_1[2])
month = int(ex2_1[1])
year = int(ex2_1[0])

day = datetime.date(year, month, date).weekday() # Returns day of the date as an integer where Monday is 0 and Sunday is 6

# Checking name of the day

dict_day = {0 : "Monday", 1 : "Tuesday", 2 : "Wednesday", 3 : "Thursday", 4 : "Friday", 5 : "Saturday", 6 : "Sunday"}

for i in dict_day:
    if day==i:
        day_name = dict_day[i] # Name of the day

# Checking name of the month

dict_month = {1 : "January", 2 : "February", 3 : "March", 4 : "April", 5 : "May", 6 : "June", 7 : "July", 8 : "August", 9 : "September", 10 : "October", 11 : "November", 12 : "December"}

for j in dict_month:
    if month==j:
        month_name = dict_month[j]

# Time in a.m. or p.m.?

if int(ex2_2_1[0])==12:
    time = "noon"
elif int(ex2_2_1[0])>11:
    time = "p.m."
else:
    time = "a.m."

# Working with diary of user

with open (f"{username}.txt", "a") as f:
    a = f.write(f"{day_name}, {date} {month_name} {year}\t\t\t\t\t\t{hour}:{minute} {time}\n\n{text}\n\n{username}\n\n\n")
save_help = str(a)

# Almost 100
# lines of
# code