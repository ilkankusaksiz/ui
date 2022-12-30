for q in range(500,600):
    count = 0
    for i in range(2,q):
        if (q%i)==0:
            break
    if q == i+1:
        print(q)