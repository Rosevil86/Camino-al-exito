for i in range(1,101,1):
    if i%3==0 or i%5==0:
        if i%3==0 and i%5==0:
            print("Fizz Fuzz")
        else:
            if i%3==0:
                print("Fizz")
            else:
                print("Fuzz")
    else:
        print(i)
