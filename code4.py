a=4
b=3
sum=a+b
print("sum of {} & {} is {}".format(a,b,sum))
print(f"sum of {a} & {b} is {a+b} and average {(a+b)/2}")

n=[2,5,6,4,3,6,7]
n.append(9)
print(n)
n.insert(3,7)
print(n)
n.sort()
print(n)
n.reverse()
print(n)

idx=0
x=6
for val in n:
    if(val==x):
        print(f"{x} is found at idx={idx}")
        break
    idx+=1

# student enrolment give a list of tuple with info(name,subject):
#     list all unique unique_course
#     list student enrolled in english
#     create dictionary(student set of courses)
info=[
    ("alice","math"),
    ("bob","science"),
     ("alice","science"),
     ("charli","math"),
    ("bob","math"),
     ("alice","english"),
     ("charli","english"),
]
# list all unique unique_course
unique_course=set()
for tup in info:
    unique_course.add(tup[1])
print(unique_course)

#   list student enrolled in english
for name,course in info:
    if(course=="english"):
        print(name)

# create dictionary(student set of courses)
dic={
}
for name,course in info:
    if(dic.get(name)==None):
        dic.update({name:set()})
        dic[name].add(course)
    else:
        dic[name].add(course)

print(dic)
