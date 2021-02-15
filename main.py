# this is a comment 
print("Hello world\n")
# print(8+5)

'''
This is a multiline commnet
'''

a = 44
b = "James"
c = 45.54
d = 4
print(a + c)
print(a - c)
print(a * d)
print(a / d)
# print(a + b)  we cannot concat int and str type variables 
print("exponantial operation : ",2**3) # exponantial operation : returns power to the result value
print("floor operation : ",4//2)  # floor operation  : returns  divisor
print("module operation :",4%2)  # module operation  : returns remainder



print("a datatype : " , type(a))
print("b datatype : " , type(b))
print("c datatype : " , type(c))
print("d datatype : " , type(d))

e = "34"
e = int(e)
print("typecasting  : ", e + 2) 

#++++++++++++++++============================_++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

x = 12
y = 10.10
z = "James"

#convert int to str and float and then print 
conv_str = str(x)
print("conv_int_str" , type(conv_str))
conv_float = float(x)
print("conv_int_float" , type(conv_float))


#convrt float to str and int 
conv_str = str(y)
print("conv_flt_str" , type(conv_str))
conv_int = int(y)
print("conv_flt_int" , type(conv_int))


#convert str to int and float 
# conv_int = int(z)
# print("conv_str_int" , type(conv_int))
# conv_float = float(z)
# print("conv_str_float" , type(conv_float))


#multiline string 
name = '''James
is a good boy'''
print(name)


# string slicing 
name = "        James   "
print(name[2:6])
print(name[:7])

#string stripping 
print("strng without stripping : ",name)
print("\n strng with stripping : ",name.strip())


#string length
print("length of string :  " , len(name.strip()))

#string lower 
print(name.lower())

#string upper
print(name.upper())

#string replace
print(name.replace('am','e'))

# string replace 
var = "sam , row , joe"
print(var.replace(',',''))

#string formatting 
name1 = "sam"
name2 = "joe"

temp = "this is a {} and he is a very clever boy named {}".format(name1,name1)
print(temp)

# fstring 
temp = f"this is a {name1} and he is a very clever boy as {name2}"
print("fstring : ",temp)

'''
Python Collections :
1. List 
2. Set
3. Tuple 
4. Dictionary

'''

# 1. List 
''' List are mutable(changable) , can arrange in any order '''
print("="*124)
lst = [43,2,4,6,54,7]
print("original list : ",lst)
print(lst[0])
print(lst[2:5])

# append the number 
lst.append(100) # append the given number at the end of the list 
print("list after append:  ",lst)
lst[4] = 50
print(lst)

# insert the number 
lst.insert(2,20)  # insert the given number at perticular index
print("list after insertion :   ",lst)

# removing the number 
lst.remove(2) # remove(value to be removed)
print("list after remove : ---",lst)

# pop  the value
lst.pop(4) # deletes the last value from the list 
print(lst) 

# delete the value
del lst[1]
print(lst)

#delte the entire list
var = lst
print(var)
del var

print("="*124)

# 2. Tuple 
''' Tuples are immutable(Non changable) '''
a = ("James" , "Joy","Joe" , 3,5,7, 8, 6, 7, 8, 7) 
print("tuple : -",a)
print(type(a))
#a[2] = "vishal" # does not support item assignment

# can type-cast from one collection to other
conv_A=  list(a)
print(type(conv_A))

# index() : Search for the first occurrence of the value , and return its position:
index = a.index(7)
print(index)

# count() : Return the number of times the value  appears in the tuple:
cnt = a.count(7)
print(cnt)

print("="*124)

# 3. Set 
s1 = {23,45,54,65,4,243,652,4,652,4,24}
print("origianl set :" ,s1)

# add only one element in the set
s1.add(1000)
print(s1)

# update more than one element in the set
s1.update([12,43,35,45,5,65,77,56])
print(s1)

#copy  the entire set
s2 = s1.copy()
print(s2)

print(s2.clear())

# discard remove the element from the set though it exists or not
s1.discard(23)
print(s1)

#remove : it deletes the element only if it exists
s1.remove(35)
print(s1)

print("="*124)

# 4: Dictionary
SampleDict = {
    "name" : "Joe" , 
    "marks" : 54,
    "class" : "1st"
}

print("origianl dict  : ",SampleDict)

#keys of dictionary
key = SampleDict.keys()
print(key)

#pop removes the value of specified key
SampleDict.pop("name")
print("SampleDict after pop : ----",SampleDict)

# popitme reomves last element from dict
SampleDict.popitem()
print(SampleDict)

print("="*124)

''' if else ladder '''
age = input("enter your age : \t")
age = int(age)
# print(type(age))
if (age > 18):
    print("you can drive a car")
elif(age == 18):
    print("You are ready to drive next year")
else:
    print("You cannot drive ")

print("="*124)

''' for loop '''
for i in range(0,1001):
    print(i)

# for loop to iterate over the list 
li = [1,243,32,"hive"]
for item in li:
    print(item)

# Same we can do for the tuple set and dictionary

print("="*124)


''' while loop '''
i = 0
while i < 100 :
    print(i)
    i = i + 1

print("="*124)


'''break statememt  '''
i = 0
while i < 100 : 
    print(i)
    i = i + 1
    if i == 60:
        break 


''' functions '''
def greet():
    print("Hello world")

greet()