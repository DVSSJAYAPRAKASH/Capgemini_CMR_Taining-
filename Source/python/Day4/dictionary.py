D={}
D={'apple':3 ,'Mango':4}
print(D)
D=dict(name='Bob',age=40)
print(D)
D={'food':{'ham':1,'egg':2}}
print(D)
keylist=['apple','banana','Mango']
valuelist=[1,2,3]
D=dict(zip(keylist,valuelist))
print(D['Mango'])
print(D)
list_a=[]
list_a.append(10)
D=dict.fromkeys({'a','b'})
print(D.get('d')) # used to get the value of the key with out error
print(D)
D2={'apple':8}
D.update(D2)
print(D)
D.pop('apple')
print(D)
d2=D.copy()
print(d2)
print(d2.items())
