"""x = [4, 6, 1, 3, 5, 7, 25]

def draw_star(list):
    for i in range(0,len(list)):
        temp = ""
        for j in range(0,list[i]):
            temp+="*"
        print temp

draw_star(x)"""

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_star(list):
    for i in range(0,len(list)):
        temp = ""
        if type(list[i]) == str:
            for k in range (0, len(list[i])):
                temp+=list[i][0]
        else:
            for j in range(0, list[i]):
                temp+="*"
        print temp

draw_star(x)

