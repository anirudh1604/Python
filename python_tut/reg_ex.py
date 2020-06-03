import re
s1="we need to inform with the latest information"

if re.search("inform",s1) :
    print("There is inform")

allinform =re.findall("inform",s1)

for i in allinform :
    print(i)   

for i in re.finditer("inform",s1) :
    print(i.span())


str1="SathatatmatelatpattatSatmat1at"

allstr=re.findall("[Shmpt ]at",str1)
 
for i in allstr :
    print(i)

allstr=re.findall("[h-t]at",str1)

for i in allstr :
    print(i,end="/")



print()
allstr=re.findall("[^h-m]at",str1)

for i in allstr :
    print(i,end="/")



s1="mat pat rat hat"
print()
print()
regex=re.compile("[r]at")
print(regex)
s1=regex.sub("food",s1)
print(s1)



a="123445784Aqw"
print(re.findall("\d{4}",a))  
print("Mathes:",len(re.findall("\d{4}",a)))
print("Mathes:",len(re.findall("\d",a)))
print("Mathes:",len(re.findall("\D",a)))