# 1
 .name=input("enter your name:")
 age=input("enter your age:")
 print("Hello"+ name + "you are "+ age + " old!")
# 2
 a=int(input("enter number a:"))
 b=int(input("enter number b:"))
 print("sum:",a+b)
 print("diff:",a-b)
 print("mul:",a*b)
 print("division:",a/b)
 print("mod:",a%b)
# 3
 a=int(input("enter number a:"))
 b=int(input("enter number b:"))
 c=float(input("enter number c:"))
 avg=(a+b+c)/3
 print(avg)
# 4
 a=input("enter a number:")
 b=int(a)
 c=float(b)
 d=str(c)
 print(a,type(a))
 print(b,type(b))
 print(c,type(c))
 print(d,type(d))

# 5
 x=10+3*2**2
 print(x)

 # 6
 a=input("enter number")
 b=input("enter number")
 temp=a
 a=b
 b=temp
 print(a)
 print(b)

# 7
 a=input("enter number")
 a=float(a)
 b=(a*(9/5)+32)
 print(b)

# 8
 r=int(input("enter number"))
 pi=3.14
 area=(pi*r*r)
 print(area)

# 9
 p=float(input("enter number"))
 r=float(input("enter number"))
 t=float(input("enter number"))
 si=(p*r*t)/100
 print(si)

# 10
num = float(input("Enter decimal number: "))
int_part = int(num)
frac_part = num - int_part
print("Integer part:", int_part)
print("Fractional part:", frac_part)
