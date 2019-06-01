fruit="banana"
letter=fruit[1]
print(letter)
word=fruit[2:]
print(word)
print(len(fruit))


try :
    x=fruit[3]
except Exception :
    print("String Index out of Range")
else :
    print(x)


index =0
while index < len(fruit):
    print (index,fruit[index])
    index+=1


sentence='the entire world is full of fools'
word =input("Enter:")
if (word in sentence):
    print ("Found it")
else :
    print ("Soory")


if word =='world' :
    print ("Found world")
elif word < 'world' :
    print ("Came before world")
else :
    print ("Came after world")

if ('w' in sentence) :
    print ("Hiw")
else :
    print ("Lo")

if ('W' in sentence) :
    print ("Hiw")
else :
    print ("Lo")


op='W porządku, dziękuję'+' '


str1=op*5
print(str1)


atr=None
print(type(atr))



