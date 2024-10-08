"""
author-anna mariya shibu
created on 8/10/2024
program for concatenating
"""
first_name=input("enter your first name:")
last_name=input("enter your last name:")
full_name=first_name+ " " +last_name
print(full_name)
length= len(first_name)
print(length)
extracted_last_name=full_name[length+1:]
print(extracted_last_name)