L=[]

while len(L)<5:
    new_name=input("Please add a new name: ").strip().capitalize()
    L.append(new_name)
print("Sorry list is full ")
print(L)
    
    
number=1

while number<=10:
    if number%2==0:
        print(number)
        number=number+1   
