name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]



def make_dict(list1, list2):
    new_dict = {}
    temp = list2
    if len(list1) < len(list2):
        list2 = list1
        list1 = temp
    
    new_dict = dict(zip(list1,list2))

    return new_dict

make_dict(name, favorite_animal)