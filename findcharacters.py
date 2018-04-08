word_list = ['hello','world','my','name','is','Anna']
char = 'o'

def charWords(list, char):
    newList = []
    for i in range(0,len(list)):

        if list[i].find(char) >= 0:
            print list[i].find(char)
            newList.append(list[i])
        
    print newList
    return newList

charWords(word_list, char)
