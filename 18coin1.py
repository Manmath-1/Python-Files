class pound:

    value=1.00
    color="gold"
    num_edge=1
    diameter=2.25 #mm
    thickness=3.15 #mm
    heads=True



coin1=pound()
coin1.color="greenish"
print(coin1.color)
coin2=pound()
coin2.value=1.25
print(coin2.value)
print(coin1.value)

print(type(coin1))
