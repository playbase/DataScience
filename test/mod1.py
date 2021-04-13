def printEvenNumbers():
    try:
        num = int(input("Enter a range: "))  
    except Exception as e:
        print("Exception==",e)
    else:
        for i in range(num):
            if (i % 2) == 0:  
                print("{0} is Even number".format(i))  
   