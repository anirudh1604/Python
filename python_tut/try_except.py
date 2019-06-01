age = -1
while (age <= 0) :
    try :
        age = int(input(("enter yor age")))
        if (age <= 0) :
            print ("Must be Positive")
    except ValueError :
        print("Invalid response")
        raise
    except EOFError :
        print ("Hello")
        raise