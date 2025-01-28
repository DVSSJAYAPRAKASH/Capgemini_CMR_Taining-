list_a=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5]
print(f"Uniques in the list are:{set(list_a)}")
veg={'carrot','potato','tomato','egg'}
nv={'chicken','mutton','fish','egg'}
print(veg|nv)
print(veg&nv)
print(veg-nv)
print(veg^nv)
print((veg|nv)-veg&nv)
