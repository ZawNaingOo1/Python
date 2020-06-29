Name = input("Enter user name : ")

PassWord = input("Enter user Pass Word : ")
#Trim name & get first name
FirstName = Name.strip().split()

#checking password
if len(PassWord) >= 8:
    print("Welcome %s" %FirstName[0]) 
else:
    print("Password must have at least 8 digits")

#easy problem



    

