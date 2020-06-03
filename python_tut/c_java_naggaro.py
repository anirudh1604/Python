s1=input()
if ("_" in s1):
    lst=s1.split("_")
    for index,j in enumerate(lst) :
        if (index != 0) :
            lst[index]=j.capitalize()
else :
    lst=[]
    for index,i in enumerate(s1) :
        if (i.isupper()) :
              lst.append("_")
              lst.append(chr(ord(i)+32))
        else :
            lst.append(i)
s1="".join(lst)
print(s1)

    