# character input program
# program which reads name and age of a person and tells them the year in which 
# they will be turn 100.

import datetime

today = datetime.date.today()
# print(today.year)

print("Enter your Name:")
user_name = input()
print("Hello,", user_name)
print("\n")

print("Enter your age:")
user_age = int(input())
print("Glad to know you are", user_age, " Years old")
print("\n")

print("Enter current Year")
current_year = int(input())
print("Current year is", current_year)
print("\n")

# logic to calculate years to turn into 100

diff_in_years = 100 - user_age
# print(diff_in_years)

# print(user_name," In year", diff_in_years + current_year, "you will turn 100")
print(user_name," In year", diff_in_years + today.year, "you will turn 100")



