# list method example
# program for getting multiple usernames

# .append()
usernames=[]
for i in range(10):
    name=input(f"Enter your name {i+1}:")
    usernames.append(name)
print(usernames)

# .copy()

list1 = ['hello','welcome']
cplist = list1.copy()
print(cplist)

# .clear()

list2 = ['hello','welcome']
clrlist = list2.clear()
print(clrlist)

# .count()

list3 = [1,2,1,3,1,4]
noElements = list3.count(1)
print(noElements)

# .extend()

list4 = ["apple","mango","banana"]
list5 = ["avengers",2,"tony stark"]
exlist = list4.extend(list5)
print(exlist)


# .index()

list6 = ['luffy', 'zoro', 'sanji', 'brook', 'chopper', 'nami']
indxlist = list6.index('brook')
print(indxlist)

# .insert()

list7 = list6
inslist = list7.insert(2,'robin')
print(list7)

# .pop()

list8 = list6
poplist = list8.pop(2)
print(list8)





