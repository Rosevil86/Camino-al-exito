i=0
num_1=1
num_2=2
while i<2:
    for i in range(0,3):
        print(i)
else:
    for i in range(3,20):
        fibo=num_1+num_2
        print(fibo)
        if i%2==1:
            num_1=fibo
        else:
            num_2=fibo
