

#1Factorial of a number
  #for Loo
n=8
if n<0:
    print("Negative")
else:
    f=1
    for i in range(1,n+1):
        f *=i
print(f)

#2 Recursive function
def fact(n):
    if n<0:
        print(Negative)
    return 1 if n<=1 else n * fact(n-1)
    

print(fact(6))

#Simple Interest /Lamda function-->Simple anoymous function which has 1 express and no return
#3
p,n,r=1000,2,5
si=lambda p,n,r:(p*n*r)/100
print(si(p,n,r))
#4Leap Year
year=int(input("Enter Year:"))
if(year%4 ==0 and year %100==0 or year%400==0):
    print("year is a leap")
else:
    print("year is nota leap year")


#Fibonacce Series

#number is Prime or NOT


