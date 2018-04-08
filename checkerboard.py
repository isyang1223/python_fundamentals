# def checkerboard():
    
#     for j in range(1, 9):
#         star=""
#         if j % 2 == 0:
#             j = "*"
#             star+=j
#         for i in range(1,9):
            
#             if i % 2 == 0:
#                 i = "*"
#                 star+=i
#             else:
#                 i = " "
#                 star+=i
#         print star


def checkerboard():
    
    for colum in range(1,9):
        star =""
        
        if colum % 2 == 0:
            for row in range(1,9):
                if row % 2 == 0:
                    star+="*"
                else:
                    star+="$"
        else:
            for row in range(1,9):
                if row % 2 == 0:
                    star+="$"
                else:
                    star+="*"

        print star
            


        





checkerboard()




