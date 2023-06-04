x=[234,456,1234,456,67,23,4235,445756,2134,345]
y=min(x)

if y<1000:
    p=pow(y,2)
    print(p)
    if p>500:
        q=p*-2
        print("Q = ",q)
        if q<0:
            r=abs(q)
            print(r)
elif y>1000:
    print("Okay, stop here")