def calculate_simple_interest(p,n,r):
       si=(p*n*r)/100
       return si
p=float(input("enter principal amount"))
n=float(input("enter time period"))
r=float(input("enter rate"))
simple_interest=calculate_simple_interest(p,n,r)

print("simple_ interest is :",simple_interest)




