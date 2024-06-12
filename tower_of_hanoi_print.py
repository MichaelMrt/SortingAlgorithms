def print_update(list):
    if(list[0]==1):
        print("a: ",list[1])
    if(list[0]==2):
        print("b: ",list[1])
    if(list[0]==3):
        print("c: ",list[1])

def update(a,b,c):
    stacks = [a,b,c]
    ordered_stacks = sorted(stacks,key=lambda x: x[0])

    for i in ordered_stacks:
        print_update(i)
    
def move(plates, a, b, c):  
    if plates > 0:
        move(plates-1, a, c, b) 
        c[1].append(a[1].pop())   
        update(a,b,c)  
        print("\n")
        move(plates-1, b, a, c)  

a = [1,[]]
b = [2,[]]
c = [3,[]]

plates = 4
for i in range(plates):
    a[1].append(plates-i)
update(a,b,c)
print("\n")
move(plates, a, b, c)
