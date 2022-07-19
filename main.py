from urllib import response
import qr

def newProduct():
    new=input("What product do you need?")
    text=new.split()
    m=0
    for i in product:
        for j in text:
            if i == j:
                need=i
                m=1
                break
        if m==1:
            break
    return need
def end():
    q=int(input("Shall I take you to the billing section, 1)Yes 2)No"))
    if q==1 or q=="yes":
        print("Go Straight")
        quit=0
        return quit
    elif q==2 or q=="no":
        print("See you next time")
        quit=1
        return quit
    else:
        print("Enter correct response")
        end()

product=['rice','cake','bread','carrot']
print("Welcome")

asd=1
while True:
    if asd == 2:
        need='origin'
    else:
        need=newProduct()
   
    # A=rice B=cake C=bread D=carrot


    l= qr.scan()
    same='z'+need+'Ignore'
    if l == same:
        print('you are standing in the right location, product: '+need+' is in front of you.')
        asd=int(input("1)Continue shopping, 2)End shopping"))
        if asd == 2:
            quit=end()
        if quit ==1:
            break
    elif 'Ignore' in l:
        print('Go Straight')
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