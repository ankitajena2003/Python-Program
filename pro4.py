#swap 2 numbers without using third variable
# a,b=20,30
# a,b=b,a
# print(a,b)

a=int(input("Enter a num : "))
b=int(input("Enter another num : "))
a,b=b,a
print(a,b)

