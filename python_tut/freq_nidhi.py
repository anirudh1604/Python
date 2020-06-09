str="babbdc"
d1={}
for i in str:
    if i in d1:
        d1[i]+=1
    else:
        d1[i]=1


# for i in range(97,123):
#     if d1.get(chr(i))!=None and d1.get(chr(i))!=0:
#         print("{}{}".format(chr(i),d1.get(chr(i))),end="")

from string import ascii_lowercase
for c in ascii_lowercase:
    if d1.get(c)!=None and d1.get(c)!=0:
        print("{}{}".format(c,d1.get(c)),end="")
