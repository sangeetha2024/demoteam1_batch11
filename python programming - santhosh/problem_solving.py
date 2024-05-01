#1 to find if the given number is prime or not

def isprime(num):
    if num > 1:
        for i in range(2, (num//2)+1):

            if (num % i) == 0:
                
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
isprime(3)

#2 Non repeating elements in an array

def nonrepeatingelem(arr,n):
    for i in range(n):
        j = 0
        while(j < n):
            if (i != j and arr[i] == arr[j]):
                break
            j += 1
        if (j == n):
            return arr[i]
 
    return -1
 
 
arr = [9, 4, 9, 7, 7, 4,3]
n = len(arr)
print(nonrepeatingelem(arr, n))

#3 reverse of an array

arr1 = (1,2,3,4,5)
print(arr1[::-1])


#4 sum of numbers in an arr

def sumofarr(*list):
    sum = 0
    for i in range(len(list)):
        sum+=list[i]
    return sum
l1=[1,2,3,4,5]
print(sum(l1))

#5 area of a triangle

a = 5
b = 6
c = 7

s = (a + b + c) / 2

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)


#6 to checck a element in a list 
def findelement(num):
    mylist = [1,34,23,7,9,45]
    if num in mylist:
        return True
    else:
        return False

print(findelement(11))

