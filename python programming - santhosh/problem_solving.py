# to find if the given number is prime or not

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

# Non repeating elements in an array

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

