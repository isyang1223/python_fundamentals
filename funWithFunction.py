


def oddOrEven():
    for i in range(1,2001):
        if i % 2 != 0:
            print "Number is " + str(i) + ". This is an odd number."
        else:
            print "Number is " + str(i) + ". This is an even number."

oddOrEven()


a = [2,4,10,16]
def multiply(arr, c):
    for i in range(0, len(arr)):
        arr[i]*=c
    return arr

b = multiply(a, 5)
print b




def layered_multiples(arr):
    new_array = []
    for i in range(0,len(arr)):
        temp =[]
        for i in range(0,arr[i]):
            temp+="1"
        new_array.append(temp)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x


