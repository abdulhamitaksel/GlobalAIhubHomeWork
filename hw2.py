mylist=["","","",""]
name=input("Name:")
mylist[0]=name
surname=input("Surname:")
mylist[1]=surname
age=int(input("Age:"))
mylist[2]=age
birtday=int(input("Birthday(Just year):"))
mylist[3]=birtday

for i in mylist:
    print(i)
    
if age<18:
    print("You can’t go out because it’s too dangerous")
else:
    print("You can go out to the street")
