l = ['magical unicorns',19,'hello',98.98,'world']


def types(list):
    count = 0
    data = type(list[0])
    dataType = ""

    string = ""
    sum = 0

    for i in range(0, len(list)):
        if type(list[i]) != data:
            count +=1
            
        if type(list[i]) == str:
            string += " "+ list[i]

        elif type(list[i]) == int or type(list[i]) == float:
            sum+= list[i]
    
    if count > 0:
        dataType = "mixed"
    
    if dataType != "mixed":
        if data == str:
            dataType = "string"
        elif data == int:
            dataType = "interger"
        elif data == float:
            dataType = "float"
        elif data == bool:
            dataType = "boolean"
    
    print "The list you entered is of " + dataType +" type"
    if dataType == "string":
        print "String: " + string
    if dataType == "interger" or dataType == "float":
        print "Sum: " + str(sum)
    if dataType == "mixed":
        print "String: " + string
        print "Sum: " + str(sum)

    



types(l)




