""" Assingment Operator
= --> Assign
+= --> Add & Assign
-= --> sub & Assign
*= --> mul & Assign
**= --> pow & Assign
/= --> div & Assign
//= --> fol div & Assign
%== --> mod & Assign

membership operator
in
not in

identify operator - it is used check the wether two variables refers to same objects in memory
is 
is not

"""
#%%
x = 10
x+= 2
print(x)

# %%
x-= 2
print(x)
#%%
x*= 2
print(x)
#%%
x**= 2
print(x)
#%%
x/= 2
print(x)
#%%
x//=2
print(x)
#%%
x%= 2
print(x)

#%%
l = [5,6,7,8,9]
print(5 in l)
print(10 in l)

#%%
print(5 not in l)
print(10 not in l)

#%%
b = "sampath"
print("s" in b)
print("c" in b)

#%%
print("s" not in b)
print("c" not in b)
# %%
x = [10]
y = 10
z = 10
print(y is z)
print(y is not z)
print(x is z)
print(x is not z)
# %%
a = [1,2,3]
b = [1,2,3]
c = a
print (a is b)
print (a == b)
print ( a is c)
print(a is not c)
print(a is not b)



# %%
s = "python"
print("a" in s)

#%%
l=[1,3,5,7,9]
print(5 in l )

#%%
l = ["python","c","c++"]
print("java" not in l)

#%%
t=(5,10,15,20)
print(10 in t)

#%%
l = ["blue","green","yellow"]
print("red" in l)

#%%
a = 10
c = 10
print(a is c)

#%%
b = [1,2,3,4,5,6,7,2]
c = [1,2,3,4,5,6,7,2]
print(b is c)


#%%
a = [1,2,3]
b = [4,5,6]
print(a is b)

#%%
x= int(input())
print(x>10 and x<50)

#%%
age = int(input())
print(age >= 18 and age < 60)
# %%
