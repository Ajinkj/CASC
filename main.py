import qr



product=['rice','cake','bread','carrot']

while True:
    print("Welcome")
    t=input("What product do you need?")
    text=t.split()
    m=0
    for i in product:
        for j in text:
            if i == j:
                need=i
                m=1
                break
        if m==1:
            break
    # A=rice B=cake C=bread D=carrot


    l= qr.scan()
    same='z'+need
    if l == same:
        print('you are standing in the right location, product: '+need+' is in front of you.')
    else:
        q=l.split("#")
        right=q[0]
        left=q[1]
        straight=q[2]

        if need in right:
            print("Go right")
        elif need in left:
            print("Go left")
        elif need in straight:
            print("Go straight")