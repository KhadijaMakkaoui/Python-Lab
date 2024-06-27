rows=5
count=5
for i in range(1,rows+1):
    for z in range(rows-i):
            print(" ",end="")
    for j in range(1,i*2):
        print("*", end="")
    print()