x=int(input("Enter:"))
n=x
rev=0
while(x>0):
    rev=rev*10+x%10
    x=x//10
if n==rev :
    print ("Palindrome")
else :
    print ("Not Palindrome")