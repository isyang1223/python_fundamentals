# for i in range(1,1001):
#     if i % 2 !=0:
#         print i

# for i in range(5,1000001):
#     if i % 5 == 0:
#         print i

a = [1, 2, 5, 10, 255, 3]

# def sumList(list):
#     sum = 0
#     for i in range(0, len(list)):
#         sum+=list[i]
#     print sum

# sumList(a)

def avgList(list):
    sum = 0
    for i in range(0, len(list)):
        sum+=list[i]

    avg = sum/len(list)
    print avg


avgList(a)
    
    




