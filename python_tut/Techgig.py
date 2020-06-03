num="1234as"
import re
print(num.isalnum())

print(num.isdigit())


print("for".isidentifier())


print(chr(ord('e')+1))


print("test\example\sample.txt")


print('a'+'10')


lst1=[1.2,3,4]
print(lst1[0])


a=50

def func(a):
    print(a)
    a=2
    print(a)
func(a)
print(a)


s1="1+2-3"

print(tuple(s1))


print(eval(s1))



print("A@ 1,".islower())


sentence='a b c'
matched=re.match(r'(.*)(.*?)(.*)',sentence)
print(matched.group(2)) 