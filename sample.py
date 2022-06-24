scn="zRight:A,B # zLeft:C,D # zStright:A,D"
q=scn.split("#")
print(q)
need='A'
right=q[0]
left=[1]
straight=q[2]
if need in right & need in left & need in straight:
    print('you are standing in the right location, product: '+need+' is in front of you.')
if need in right:
    print("Go right")
elif need in left:
    print("Go left")
elif need in straight:
    print("Go straight")