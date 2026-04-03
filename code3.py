age=int(input("enrer age:"))
if(age>=18):
    print("you can vote.")
    print("you can drive.")
else:
    print("you can't vote.")

color=input("enrer color:")
if(color=="red"):
    print("stop.")
    
elif(color=="yellow"):
    print(" ready.")
elif(color=="green"):
    print("go")
else:
    print("wrong color for traffic")

age=int(input("enrer age:"))
if(age<13):
    print("child.")
elif(age>=13 and age<18):
    print("teenager")
else:
    print("adult")

username=input("enetr username")
password=input("enetr password")
if(username=="admin"and password=="pass"):
    print("login successful")
else:
    if(username!="admin"):
        print("wrong user name")
    else:
        print("wrong password")

num=int(input("enter number"))
if(num%5==0):
    print("mutiple of 5")
else:
    print("not multiple of 5")

num=int(input("enter number"))
if(num%2==0):
    print("even")
else:
    print("odd")

color=input("enter color:")
match color:
    case "red":
        print("stop")
    case "yellow":
        print("ready")
    case "green":
        print("go")
    case _:
        print("wrong color")

num=int(input("enter number"))
result="even" if num%2==0 else "odd"
print(result)
i=5
while i>0:
    print(i)
    i-=1

n=int(input("enter"))
i=1
while i<=10:
    print(n*i)
    i+=1

count=0
word="artificialinteligence"
for ch in word:
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' ):
        count+=1
print(count)
    