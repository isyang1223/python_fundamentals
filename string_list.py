words = "It's thanksgiving day. It's my birthday,too!"

def find(string):
    print string.find("day")

find(words)

def replace(string):
    print string.replace("day", "month")


replace(words)


x = [2,54,-2,7,12,98]

def minimum(list):
    print min(list)

minimum(x)

def maximum(list):
    print max(list)

maximum(x)


x = ["hello",2,54,-2,7,12,98,"world"]

def firstAndLast(list):
    print list[0]
    print list[-1]

    newArr = []
    newArr.append(list[0])
    newArr.append(list[-1])
    print newArr

firstAndLast(x)


x = [19,2,54,-2,7,12,98,32,10,-3,6]

def newList(list):
    list.sort()
    firstHalf = list[0:len(list)/2]
    print firstHalf
    secondHalf = list[len(list)/2:]
    print secondHalf
    
    secondHalf.insert(0, firstHalf)
    print secondHalf




newList(x)
    





