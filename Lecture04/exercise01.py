fn = input("Enter your frist name: ")
la = input("Enter your last name: ")
sid = input("Enter your student ID number: ")
print("Your system login name is:")
log_name = fn[0:3]+la[0:3]+sid[-3:]
print(log_name)