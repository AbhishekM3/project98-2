def swapFileData ():
    with open ("simpleText1.txt","r") as a :
        data_a = a.read()

        
    with open ("simpleText1.txt","w") as a :
        a.write(data_b)

    with open ("simpleText1.txt","r") as b :
        data_b = b.read()
      
    with open ("simpleText1.txt","w") as b :
       b.write(data_a)

    swapFileData()